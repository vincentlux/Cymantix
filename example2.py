from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor

class EntryParser(NodeVisitor):
    def __init__(self, grammar, text):
        self.entry = {}
        ast = Grammar(grammar).parse(text)
        self.visit(ast)
    def visit_name(self, n, vc):
        self.entry['name'] = n.text
    def visit_gender(self, n, vc):
        self.entry['gender'] = n.text
    def visit_age(self, n, vc):
        self.entry['age'] = n.text
    def generic_visit(self, n, vc):
        pass

grammar = """\
entry = name sep gender? (sep age)?
sep = ws "," ws
ws = " "*
name = ~"[A-z]*"
gender = "male" / "female"
age = ~"[0-9]*"
"""

text = """\
Bob, male, 26
Kim,female,30
Joe,male
"""

for line in text.splitlines():
    print("text: ",text)
    print(EntryParser(grammar, line).entry)