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

    def visit_name(self, node, chidren):
        if node.text in self._ctx :
            val=self._ctx[node.text]
            if isinstance(val, (six.string_types)+ (six.binary_type,)) :
                val = decode(val).lower()
            return val
        elif self._strict:
            raise EvalError('Unknown variable %s'%node.text, node.start)
        else:
            return ''

    def visit_literal(self,node, children):
        return decode(children[1]).lower()

    def visit_chars(self, node, children):
        return node.text

    def binary(fn):  # @NoSelf
        def _inner(self, node, children):
            if isinstance(children[0], bool):
                raise EvalError('Variable is boolean, should not be used here %s'% node.text, node.start)
            return fn(self, node, children)
        return _inner

    @binary
    def visit_contains(self, node, children):
        return children[0].find(children[-1]) > -1

    @binary
    def visit_equals(self, node, children):
        return children[0] == children[-1]

    def visit_expr(self, node, children):
        return children[1]

    def visit_or(self, node, children):
        return children[0] or children[1]

    def visit_more_or(self,node, children):
        return any(children)

    def visit_and(self, node, children):
        return children[0] and (True if children[1] is None else children[1])

    def visit_more_and(self, node, children):
        return all(children)

    def visit_not(self, node, children):
        return not children[-1]

    def visit_bracketed(self, node, children):
        return children[2]

    def generic_visit(self, node, children):
        if children:
            return children[-1]


context = {"name": "test.pdf",
           "mime": "application/pdf",
           "from": "jim@example.com",
           "to": "myself@example.com",
           "attached": True,
           "seen": False
            }

parser=SimpleEvaluator(context)
result= parser.parse('name ~=".pdf" & ( from ~= "johns" | from ~= "tim" )')

print(result)
