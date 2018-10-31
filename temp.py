from parsimonious.grammar import Grammar
import parsimonious
import six

"""
op_how: HOW level
    include: 
        keywords: TOTAL, LAST, ON
        literal: "name_here"
    
"""


# might consider change keyword part from / to ?xxx
# note: only when "xxx" after ON keywords could it represent the topic
    # sc_EMAIL_from   = "EMAIL"? "from"? '" chars "'"

grammar = Grammar(
    """
    all             = space op space sc
    sc              = sc_EMAIL_from / space
    sc_EMAIL_from   = "EMAIL from" space op_lit_name
    op              = op_trig space op_first space
    op_first        = op_TOTAL / op_LAST / op_lit_ON / op_lit_name
    op_lit_ON       = op_ON space op_lit_topic
    op_lit_topic    = "'" chars "'"
    op_lit_name     = ("'" chars "'" space)+
    op_ON           = "ON"
    op_LAST         = "LAST" space (op_LAST_time / op_LAST_piece)
    op_LAST_piece   = ~"[0-9]*" 
    op_LAST_time    = ~"[0-9]*" space ~"[a-z]+"
    op_TOTAL        = "TOTAL"
    op_trig         = "?"
    space           = " "*
    chars           = ~"[A-z0-9]*"
    """
)

class EntryParser(parsimonious.NodeVisitor):
    """
    Recognize one command and convert it to json format
    Check on:
        op_lit_topic:   "topic"                 str
        op_lit_name:    "from" (might be multiple;needs to deal with it later)      str
        op_LAST:        "last"                  bool
        op_TOTAL:       "total"                 bool
 
    Example use case:
        text = '''?TOTAL '''
        print(EntryParser(grammar,line).entry)
    """
    def __init__(self, grammar, text):
        self.entry = {}
        # self.grammar = parsimonious.Grammar(grammar)
        ast = grammar.parse(text)
        self.visit(ast)
    def visit_op_lit_topic(self, node, vc):
        self.entry['topic'] = node.text

    def visit_op_lit_name(self, node, vc):
        self.entry['from'] = node.text

    def visit_op_TOTAL(self, node, vc):
        self.entry['TOTAL'] = True
    
    def visit_op_LAST(self, node, vc):
        self.entry['LAST'] = True

    def visit_op_LAST_time(self, node, vc):
        self.entry['LAST_time'] = node.text

    def visit_op_LAST_piece(self, node, vc):
        self.entry['LAST_piece'] = node.text
    
    def generic_visit(self, node, visited_children):
        pass


"""
example command:
?ON 'haha' 
?'mike' 
?'Mike' 'Drake' 'Jim' EMAIL
?LAST
?LAST 1 month EMAIL
?LAST 1 EMAIL
?LAST EMAIL from 'Drake' 'Jim'
?TOTAL
"""
if __name__ == "__main__":
    command =  """ ?ON 'soccer'"""
    print(EntryParser(grammar,command).entry)
    print(grammar.parse(command))
