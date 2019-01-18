import pysolr
import requests

url="http://104.248.61.45:8983/solr/test/"
requests.get(url, params="select?q=*:*&rows=1&sort=date%20desc")


list(solr.search(q="from_name:mike", sort="date asc", rows=1))


# # https://github.com/django-haystack/pysolr
# solr = pysolr.Solr('http://104.248.61.45:8983/solr/#/test/', timeout=10)
# results = solr.search('mike')

# print("Saw {0} result(s).".format(len(results)))

# # Just loop over it to access the results.
# for result in results:
#     print("The title is '{0}'.".format(result['title']))
