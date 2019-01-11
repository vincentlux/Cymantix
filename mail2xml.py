# Aim to go into all dirs under maildir/ and convert all files into correspondind xml file and saved into xml_dir/
import os
import time
import re
from xml.sax.saxutils import escape

# Tags
start           = '<add>\n<doc>\n'
f_message_id    = '<field name="message_id">'
f_date          = '<field name="date">'
f_from          = '<field name="from">'
f_to            = '<field name="to">'
f_subject       = '<field name="subject">'
f_from_name     = '<field name="from_name">'
f_to_name       = '<field name="to_name">'
f_content       = '<field name="content">'
close           = '</field>\n'
end             = '</doc>\n</add>'

debug = []
def txt2xml(filepath):
    with open (filepath, errors="ignore", mode="r") as f:
        lines = f.readlines()
        temp_dict = {}
        
        split_line = []
        content = False
        for line in lines:
            if (not line.startswith("\n")) and not content: # Not yet to the content
                
                if ":" in line:
                    split_line = line.strip().split(":", 1)
                    split_line[1] = xmlescape(split_line[1].strip())
                else:
                    split_line[1] += xmlescape(re.sub(r"[\s+]", ' ', line))
                temp_dict[split_line[0]] = split_line[1]
            else:
                # Email content processing
                content = True
                try:
                    temp_dict["content"] += xmlescape(line)
                except:
                    temp_dict["content"] = ""
                    temp_dict["content"] += xmlescape(line)
        # Convert dictionary to xml
        global start, f_message_id, f_date, f_from, f_to, f_subject, f_from_name, f_to_name, f_content, close, end, debug
        xml = ""
        try:
            _message_id = f_message_id + temp_dict["Message-ID"] + close
            _date = f_date + temp_dict["Date"] + close
            _from = f_from + temp_dict["From"] + close
            try: # Should try except all but only to and x-form have missing fields for this dataset
                _to = f_to + temp_dict["To"] + close
            except KeyError:
                temp_dict["To"] = ""
                _to = f_to + temp_dict["To"] + close
            _subject = f_subject + temp_dict["Subject"] + close
            try:
                _from_name = f_from_name + temp_dict["X-From"] + close
            except KeyError:
                temp_dict["X-From"] = ""
                _from_name = f_from_name + temp_dict["X-From"] + close
            try:
                _to_name = f_to_name + temp_dict["X-To"] + close
            except KeyError:
                temp_dict["X-To"] = ""
                _to_name = f_to_name + temp_dict["X-To"] + close
            _content = f_content + temp_dict["content"] + close
            xml = start + _message_id + _date + _from + _to + _subject + _from_name + _to_name + _content + end
        except Exception as e:
            debug.append((filepath, e))
        return xml
            
def xmlescape(data):
    return escape(data, entities={
        "'": "&apos;",
        "\"": "&quot;"
    })


def main(rootdir="./maildir", targetdir="./xmldir"):
    count = 0
    cwd = os.getcwd()
    for subdir, dirs, files in os.walk(rootdir):
        print("Start processing ", subdir)
        for file in files:
            if file != ".DS_Store":
                xml = txt2xml(os.path.join(subdir, file))
                if not os.path.exists(targetdir):
                    os.makedirs(targetdir)
                else:
                    # make name and save
                    save_name = os.path.join(subdir.split("./maildir/", 1)[1], file).replace("/", "_") + "xml"
                    save_name = os.path.join(targetdir, save_name)
                    with open(save_name, "w") as f:
                        f.write(xml)
                        print("finished writing into "+ save_name)

    print(debug)
    return

main()
