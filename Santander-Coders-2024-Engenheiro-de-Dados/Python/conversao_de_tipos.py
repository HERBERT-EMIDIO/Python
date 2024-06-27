# Conversão de Tipos
idade = '26'

print(idade, type(idade))

idade_convertida_int = int(idade)
print(idade_convertida_int, type(idade_convertida_int))

# Tipos para converter
# int()
# str()
# float()
# bool()

# Por converção o que é capturado pelo input() é armazendo como str

altura = float(input('Qual sua altura? ')) #recebendo em str e já convertendo para float
print(altura, type(altura))
