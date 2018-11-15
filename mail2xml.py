# Aim to go into all dirs under maildir/ and convert all files into correspondind xml file and saved into mail_xml/
import os
import time
import re

# tags
f_message_id    = '<field name="message_id">'
f_date          = '<field name="date">'
f_from          = '<field name="from">'
f_to            = '<field name="to">'
f_subject       = '<field name="subject">'
f_from_name     = '<field name="from_name">'
f_to_name       = '<field name="to_name">'
f_content       = '<field name="content">'

close           = '</field>\n'


def txt2xml(filepath):

    with open (filepath, "r") as f:
        lines = f.readlines()
        temp_dict = {}
        
        split_line = []
        content = False
        for line in lines:
            if (not line.startswith("\n")) and not content: # not yet to the content
                
                if ":" in line:
                    split_line = line.strip().split(":", 1)
                else:
                    split_line[1] += re.sub(r"[\s+]", ' ', line)
                temp_dict[split_line[0]] = split_line[1]
            else:
                print("email content processing here!")
                content = True
                try:
                    temp_dict["content"] += line
                except:
                    temp_dict["content"] = ""
                    temp_dict["content"] += line
        # next to do: convert dictionary to xml
        return temp_dict
            
            
        

def main(rootdir="./maildir", targetdir="./xmldir"):
    count = 0
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if file != ".DS_Store":
                print("addf")
                xml = txt2xml(os.path.join(subdir, file))
                print(xml)
                if not os.path.exists(targetdir):
                    os.makedirs(targetdir)
                    # make name and save
                # return xml
            else:
                print(file)
    return

main()
