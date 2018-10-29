from parsimonious.grammar import Grammar
import parsimonious
import six
'''
op_how: HOW level
next thing:  build nodevisitor http://jeffrimko.blogspot.com/2013/05/parsing-with-parsimonious.html
'''

grammar = Grammar(
    """
    op_how          = op_trig space op_first space
    op_first        = op_TOTAL / op_literal
    op_literal      = "'" chars "'"
    op_TOTAL        = "TOTAL"
    op_trig         = "?"
    space           = " "*
    chars           = ~"[A-z0-9]*"
    """
)

class SimpleEvaluator(parsimonious.NodeVisitor):
    def __init__(self, grammar, text):
        self.entry = {}
        # self.grammar = parsimonious.Grammar(grammar)
        ast = grammar.parse(text)
        self.visit(ast)
    def visit_op_trig(self, node, vc):
        print(vc)
        self.entry['trig'] = node.text

    def visit_op_TOTAL(self, node, vc):
        print(vc)
        self.entry['TOTAL'] = node.text
    
    def visit_op_literal(self, node, vc):

        self.entry['literal'] = node.text
    
    def generic_visit(self, node, visited_children):
        pass
    
"""
next thing to do:
    1. find a way to input a email instead of a line
    2. enrich grammar
""" 



text = """?TOTAL """

for line in text.splitlines():
    print(SimpleEvaluator(grammar,line).entry)

print(grammar.parse("?TOTAL "))
