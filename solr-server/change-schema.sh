curl -X POST -H 'Content-type:application/xml' --data-binary '{
  "add-field-type" : {
     "name":"tdate",
     "class":"solr.TrieDateField",
     "positionIncrementGap":"0"}
}' http://104.248.61.45:8983/solr/mdl/schema


curl -X POST -H 'Content-type:application/xml' --data-binary '{"add-field":{"name":"from","type":"text_general","stored":true }}' http://104.248.61.45:8983/solr/mdl/schema
curl -X POST -H 'Content-type:application/xml' --data-binary '{"add-field":{"name":"to","type":"text_general","stored":true }}' http://104.248.61.45:8983/solr/mdl/schema
curl -X POST -H 'Content-type:application/xml' --data-binary '{"add-field":{"name":"message_id","type":"string","stored":true }}' http://104.248.61.45:8983/solr/mdl/schema
curl -X POST -H 'Content-type:application/xml' --data-binary '{"add-field":{"name":"subject","type":"text_general","stored":true }}' http://104.248.61.45:8983/solr/mdl/schema
curl -X POST -H 'Content-type:application/xml' --data-binary '{"add-field":{"name":"from_name","type":"text_general","stored":true }}' http://104.248.61.45:8983/solr/mdl/schema
curl -X POST -H 'Content-type:application/xml' --data-binary '{"add-field":{"name":"to_name","type":"text_general","stored":true }}' http://104.248.61.45:8983/solr/mdl/schema
curl -X POST -H 'Content-type:application/xml' --data-binary '{"add-field":{"name":"content","type":"text_general","stored":true }}' http://104.248.61.45:8983/solr/mdl/schema
curl -X POST -H 'Content-type:application/xml' --data-binary '{"add-field":{"name":"date","type":"tdate","stored":true }}' http://104.248.61.45:8983/solr/mdl/schema

# need to add date after date being preprocessed through mail2xml.py

