# Operadores de Comparacoes => Tomada de decisão

"""
Os operadores de decisão, também conhecidos como operadores condicionais ou operadores de comparação,
são utilizados na programação para tomar decisões baseadas em condições específicas.
Eles comparam valores e retornam um resultado booleano (True ou False).
"""
"==========================================================="




# um (=) para atribuição e (==) para Comparação
# a = 1
# b = 2
# c = a == b
# print("São iguais? ", c, '\n') # diz false e pula uma linha


a = 5 
b = 5
print(a == b)  # True

"==========================================================="

# Diferente de (!=):
a = 5
b = 3
print(a != b)  # True

"==========================================================="

# Maior que (>): e Menor ou igual a (<=):
a = 5
b = 3
print(a > b)  # True

a = 5
b = 3
print(a < b)  # False

"==========================================================="

# Maior ou igual a (>=): e Menor ou igual a (<=)
a = 5
b = 5
print(a >= b)  # True

a = 3
b = 5
print(a <= b)  # True

"==========================================================="
print("======================================================")
""" 
Os operadores de decisão são frequentemente usados em estruturas condicionais,
como if, elif, e else, para controlar o fluxo do programa com base em condições.
"""
x = 10
y = 20

if x < y:
    print("x é menor que y")
elif x == y:
    print("x é igual a y")
else:
    print("x é maior que y")
print("======================================================")


print("======================================================")
""" 
Combinação de Operadores de Decisão com Operadores Lógicos
Os operadores de decisão podem ser combinados com operadores
lógicos (and, or, not) para formar condições mais complexas.
"""
a = 10
b = 20
c = 30

if a < b and b < c:
    print("a é menor que b e b é menor que c")

if a < b or a < c:
    print("a é menor que b ou a é menor que c")

if not a == b:
    print("a não é igual a b")
print("======================================================")
