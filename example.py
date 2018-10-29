# Minimal example credit to http://zderadicka.eu/writing-simple-parser-in-python/
import six
import parsimonious
from parsimonious.grammar import Grammar

GRAMMAR=r""" # Test grammar
expr = space or space
or = and   more_or
more_or = ( space "|" space and )*
and = term  more_and
more_and = ( space "&" space term )*
term = not / value
not = "!" space value
value =  contains  / equals / bracketed / name
bracketed = "(" space expr space ")"
contains  =  name space "~="  space literal
equals =  name space "="  space literal
name       = ~"[a-z]+"
literal    = "\"" chars "\""
space    = " "*
chars = ~"[^\"]*"
"""

class EvalError(Exception):
    def __init__(self, text, pos=0):
        super(EvalError, self).__init__(text+ ' at position %d'%pos)

def decode(s):
    if isinstance(s, six.binary_type):
        return s.decode('UTF-8')
    return s

class SimpleEvaluator(parsimonious.NodeVisitor):
    def __init__(self, ctx, strict=True):
        self.grammar = parsimonious.Grammar(GRAMMAR)
        self._ctx = ctx
        self._strict = strict

    def visit_name(self, node, children):
        print("name: ", children)
        # print(node)
        # print(node.text)
        if node.text in self._ctx :
            val=self._ctx[node.text]
            if isinstance(val, (six.string_types)+ (six.binary_type,)) :
                print("isinstance, ", val)
                val = decode(val).lower()
                print("val: ",val)
            return val
        elif self._strict:
            raise EvalError('Unknown variable %s'%node.text, node.start)
        else:
            return ''

    def visit_literal(self,node, children):
        # print("literal: ", children)
        # print(decode(children))
        return decode(children[1]).lower()

    def visit_chars(self, node, children):
        # print("braketed", children)
        # print(decode(children))
        return node.text

    def binary(fn):  # @NoSelf
        def _inner(self, node, children):
            if isinstance(children[0], bool):
                raise EvalError('Variable is boolean, should not be used here %s'% node.text, node.start)
            return fn(self, node, children)
        return _inner

    @binary # pass the following func as a param to the above func
    def visit_contains(self, node, children):
        print("contains: ", children)
        return children[0].find(children[-1]) > -1

    @binary
    def visit_equals(self, node, children):
        print("equals: ", children)
        return children[0] == children[-1]

    def visit_expr(self, node, children):
        print("expr: ", children)
        return children[1]

    def visit_or(self, node, children):
        print("or: ", children)
        return children[0] or children[1]

    def visit_more_or(self,node, children):
        print("more or: ", children)
        return any(children)

    def visit_and(self, node, children):
        print("and: ", children)
        return children[0] and (True if children[1] is None else children[1])

    def visit_more_and(self, node, children):
        print("more and: ", children)
        return all(children)

    def visit_not(self, node, children):
        print("not: ", children)

        return not children[-1]

    def visit_bracketed(self, node, children):
        print(node)
        print("braketed", children)
        return children[2]

    def generic_visit(self, node, children):
        print("generic", children)
        if children:
            return children[-1]


context = {"name": "test.pdf",
           "mime": "application/pdf",
           "from": "jim@example.com",
           "to": "myself@example.com",
           "attached": True,
           "seen": False
            }
print(1)
parser=SimpleEvaluator(context)
print(2)
result= parser.parse('name ~=  ".pdf" & ( from ~= "tim" | to ~= "myself" )')
print(3)
print(result)
# test
# grammar = parsimonious.Grammar(GRAMMAR)
# print(grammar.parse('name ~=  ".pdf" & ( from ~= "jim" | from ~= "tim")'))
