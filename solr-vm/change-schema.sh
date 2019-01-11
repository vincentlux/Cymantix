curl -X POST -H 'Content-type:application/xml' --data-binary '{"add-field":{"name":"from","type":"string","stored":true }}' http://104.248.61.45:8983/solr/test/schema
curl -X POST -H 'Content-type:application/xml' --data-binary '{"add-field":{"name":"message_id","type":"string","stored":true }}' http://104.248.61.45:8983/solr/test/schema
curl -X POST -H 'Content-type:application/xml' --data-binary '{"add-field":{"name":"subject","type":"text_general","stored":true }}' http://104.248.61.45:8983/solr/test/schema
curl -X POST -H 'Content-type:application/xml' --data-binary '{"add-field":{"name":"from_name","type":"text_general","stored":true }}' http://104.248.61.45:8983/solr/test/schema
curl -X POST -H 'Content-type:application/xml' --data-binary '{"add-field":{"name":"to_name","type":"text_general","stored":true }}' http://104.248.61.45:8983/solr/test/schema
curl -X POST -H 'Content-type:application/xml' --data-binary '{"add-field":{"name":"content","type":"text_general","stored":true }}' http://104.248.61.45:8983/solr/test/schema

# need to add date after date being preprocessed through mail2xml.py

