import sys

expr = list(sys.argv[1])
digits = [str(n)for n in list(range(10))]

""" example from infix to postfix notation
            9-5+2
             ...
            95-2+
"""
result = []
n = 0
while n < len(expr):
    if expr[n] in digits:
        result.append(expr[n])
        n+=1
    else:
        result.append(expr[n+1])
        result.append(expr[n])
        n+=2
posfix=""
for letter in result:
    posfix += letter
print(posfix)
