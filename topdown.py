#a_simple = ["integer","char","num dotdot num"]
#a_type = [a_simple, "array ["+a_simple+"] of"+a_type, "point id"]
from adt import Case, adt
import sys

@adt
class Simple:
    INTEGER: Case[int]
    CHAR: Case[str]
    DOTDOT: Case[(int,int)]

@adt
class Complex:
    SIMPLE: Case["Simple"]
    ARRAY_OF: Case[["Simple"],"Complex"]
    POINTR: Case

@adt
class Tree:
    NIL: Case
    NODE: Case["Complex","Tree","Tree"]

expr = sys.argv[1].split()
#primero cargar la primera palabra dentro del tipo Simple adecuado
#despues cargarlo dentro de un Complex
root = Complex.SIMPLE(expr[0])

parse_tree = Tree.NODE(root, Tree.NIL, Tree.NIL)
for words in expr:
    print(words)
print(type(parse_tree.node()[0]))#.match(simple=print("hola"),)
