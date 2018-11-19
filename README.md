# Cymantix
## Pilot study on email retrieval system
* A query language based on MDL which can be used to for email retrieval
* A web-based email retrieval service using self-built language

## Run
* `git clone https://github.com/vincentlux/Cymantix.git`
* `pip install -r requirements.txt`
*  Modify command


## Part1: Grammar
### Done:
* Literature review and base language selection
* Finish ?TOTAL, "name" (1025)
* Test example of NodeVisitor (1026)
* Finish SimpleEvaluator(parsimonious.NodeVisitor) to test (1026, 1029)
* Finish ?TOTAL, ON "topic", "LAST", "name" (1029)
* Finish main Cymantix grammar

### Todo:
* ~~Write more grammar~~
    * ~~?LAST all/month/1 month~~
    * ~~compatibility of "name" and "topic"~~
    * ~~Scope level grammar~~
* Debug:
    * Add double quote compatibility
    * Date issue
    * Instance vs Class issue
* Convert email to Json 
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
* Finish converting all emails to xml (1114, 1118)

### Todo:
* Modify managed-schema
