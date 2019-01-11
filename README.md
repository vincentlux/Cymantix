# Cymantix
## Pilot study on email retrieval system
* [A query language based on MDL which can be used to for email retrieval](cymantix_grammar.py)
* [A web-based email retrieval service using self-built language](/solr-vm)
* [Project page](http://cymantix.unc.edu/projects/mdl/)

## Run
* `git clone https://github.com/vincentlux/Cymantix.git`
* `pip install -r requirements.txt`
*  Modify command


## Part1: Grammar
### EBNF (with regexes):
```
    all             ::= space op space sc
    sc              ::= sc_EMAIL_from | sc_EMAIL_attach | sc_EMAIL_piece | space
    sc_EMAIL_piece  ::= "EMAIL last" space op_LAST_piece
    sc_EMAIL_from   ::= "EMAIL from" space op_lit_name
    sc_EMAIL_attach ::= "EMAIL" space sc_attach
    sc_attach       ::= "MSWORD" | "PDF" | "GIF"
    op              ::= op_trig space op_first space
    op_first        ::= op_TOTAL | op_LAST | op_lit_ON | op_lit_name 
    op_lit_ON       ::= op_lit_name* op_ON space op_lit_topic space sc_attach* space op_LAST*
    op_lit_topic    ::= "'" chars "'"
    op_lit_name     ::= ("'" chars "'" space)+
    op_ON           ::= "ON"
    op_LAST         ::= "LAST" space (op_LAST_time | op_LAST_piece)
    op_LAST_piece   ::= ~"[0-9]*" 
    op_LAST_time    ::= ~"[0-9]*" space ~"[a-z]+"
    op_TOTAL        ::= "TOTAL"
    op_trig         ::= "?"
    space           ::= " "*
    chars           ::= ~"[A-z0-9]*"
```

### Done:
* Literature review and base language selection
* Finish ?TOTAL, "name" (1025)
* Test example of NodeVisitor (1026)
* Finish SimpleEvaluator(parsimonious.NodeVisitor) to test (1026, 1029)
* Finish ?TOTAL, ON "topic", "LAST", "name" (1029)
* Finish main Cymantix grammar

### Todo:
* Debug:
    * Add double quote compatibility
    * Date issue
    * Instance vs Class issue
* ~~Convert email to xml~~ 
* Web-based retrieval system

### Design notes
* Desired result
    * Save all emails in MongoDB
    * Input: 
        * Json file, each one represents an email (key-value)
        * Cymantix Command

            `?”Mike” ON “picnic” MSWORD LAST`
    * Output: 
        * Parsed Cymantix command

            `{'from': "'Mike' ", 'topic': "'Soccer'", 'attachment': 'MSWORD', 'piece': '1'}`
        * Use parsed Cymantix command to retrieve corresponding emails



## Part2: Web app
* Technologies:  
    * react.js; node.js; Solr

### Done:
* Node.js workflow (1105-1111)
* Solr installation on vm (1112)
* Finish converting all emails to xml (1114-1118)

### Todo:
* Modify Cymantix output grammar
    * [Field type](https://lucene.apache.org/solr/guide/6_6/field-types-included-with-solr.html)
* Research on Solr search grammar (0110,0111)
    * [Simple solr search over multiple fields](https://stackoverflow.com/questions/8089947/solr-search-query-over-multiple-fields)
    * [Json request API](https://lucene.apache.org/solr/guide/7_5/json-request-api.html#json-request-api)
* [__date time conversion__](https://lucene.apache.org/solr/guide/6_6/working-with-dates.html#working-with-dates)
* Escape special characters in mail2xml.py

### Useful links
[Schema API](https://lucene.apache.org/solr/guide/7_5/schema-api.html#modify-the-schema) (0110,0111)

[Difference between StrField and TextField](http://lucene.472066.n3.nabble.com/Difference-between-textfield-and-strfield-td3986916.html)


