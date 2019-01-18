import pysolr
import requests
import argparse
import cymantix_grammar as cg


parser = argparse.ArgumentParser()
parser.add_argument('--command', type=str, default='',
        help='Cymantix command eg. ?LAST all EMAIL from "Mike" ')
args = parser.parse_args()

# Get json file 
c_json = cg.c_json(args.command)
print(c_json)

# convert json to solr query 
# define field
try:
    # '&' for multiple person
    c_json["from"] = ' '.join(c_json["from"].split())
    c_json["from"] = c_json["from"].replace("' '", "&")
    from_name = "from_name:"+c_json["from"]
except:
    from_name = "from_name:*"

try:
    subject = "subject"+c_json["topic"]
except:
    subject = "subject:*"

try:
    content = "content:" + c_json["attachment"]
except:
    content = "content:*"

try:
    if c_json["total"]:
        num_rows = 10000
except:
    pass

try:
    num_rows = c_json["piece"]
except:
    # if not specified last x piece, return all results
    num_rows = 10000

try:
    date = c_json["time"]
    if "all" in date:
        num_rows = 10000
        date = "date:*"

    try:
        num = eval(''.join([n for n in c_json["time"] if n.isdigit()]))
    except:
        num = 1
    
    if "day" in c_json["time"].lower():
        date = "date:[2002-03-07T00:00:00Z-{:d}DAY TO NOW]".format(num)
    elif "month" in c_json["time"].lower():
        num *= 30
        date = "date:[2002-03-07T00:00:00Z-{:d}DAY TO NOW]".format(num)
    elif "year" in c_json["time"].lower():
        num *= 365
        date = "date:[2002-03-07T00:00:00Z-{:d}DAY TO NOW]".format(num)
    else:
        num = 10000
        print("Cannot recognize time; output all filtered data")
except:
    date = "date:*"

# combine string
query = from_name
fquery = subject + " AND " + content + " AND " + date
print(query)
print(num_rows)
print("date:",date)

# https://github.com/django-haystack/pysolr
solr = pysolr.Solr("http://104.248.61.45:8983/solr/test/")
# results = solr.search(q="from_name:Yates, Mike AND subject:* AND to_name:*", sort="date desc", rows=100)
results = solr.search(q=query, fq=fquery, sort="date desc", rows=num_rows)


print("Saw {0} result(s).".format(len(results)))

# Just loop over it to access the results.
for result in results:
    print("The name is '{0}'.".format(result['from_name']))
    print("The subject is '{0}'.".format(result['subject']))


