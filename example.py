from adt import Case, adt

@adt
class Simple:
    INTEGER: Case[int]
    CHAR: Case[str]

@adt
class Complex:
    SIMPLE: Case["Simple"]
    COMPLEX: Case[("Simple","Simple")]

x1 = Simple.CHAR("a")
x2 = Simple.INTEGER(1)
xs = Complex.SIMPLE(x1)
ys = Complex.COMPLEX(x1,x2)

print(x1.char())
print(ys.complex()[0].char(),ys.complex()[1].integer())

