# Cymantix
## Pilot study on email retrieval system
1. A web-based service which has a database of emails and can be queried for email retrieval
2. A query language based on MDL which can be used to query the cymantix web service

Done:
* Successfully distinguished from ?TOTAL and ?"name" (1025)

Todo:
* Write SimpleEvaluator(parsimonious.NodeVisitor) to test (1026, 1029)

Design notes
* Explicitly design keywords(nonchange) and literal("varchar")
* Desired result
    * Save all emails in MongoDB
    * Input: 
        1. Json file, each one represents an email (key-value)
        2. Cymantix Command
    * Output: 
        1. parsed Cymantix command
        2. Use parsed Cymantix command to retrieve corresponding emails

