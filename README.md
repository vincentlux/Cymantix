# Cymantix
## Pilot study on email retrieval system
1. A query language based on MDL which can be used to for email retrieval
2. A web-based service which has a database of emails and can be queried for email retrieval

### Done:
* Literature review and base language selection
* Finish ?TOTAL, "name" (1025)
* Test example of NodeVisitor (1026)
* Finish SimpleEvaluator(parsimonious.NodeVisitor) to test (1026, 1029)
* Finish ?TOTAL, ON "topic", "LAST", "name" (1029)

### Todo:
* Write more grammar
    * ?LAST all/month/1 month
    * compatibility of "name" and "topic"
    * Scope level grammar

### Design notes
* Explicitly design keywords(nonchange) and literal("varchar")
* Desired result
    * Save all emails in MongoDB
    * Input: 
        1. Json file, each one represents an email (key-value)
        2. Cymantix Command
    * Output: 
        1. Parsed Cymantix command
        2. Use parsed Cymantix command to retrieve corresponding emails

