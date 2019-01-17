import pysolr
# https://github.com/django-haystack/pysolr
solr = pysolr.Solr('http://104.248.61.45:8983/solr/#/test', timeout=10)
list(solr.search("from_name:mike"))
