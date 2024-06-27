# Listas [] -> permite str, float, int, listas de listas

print("========== Criando Listas [] ==============")
# Criando Listas
notas = [7.9, 9.7, 8.2]

print("========== Como converter com  variavel = list() ==============")
# Converter em lista
lista_vazia = list()

print("========== Listas dentro de listas ==============")
# Lista de listas
lista_lista = [10,['herbert', 1.83]]

print("========== Consultar lista lista[índice] ==============")
# Índice
print(lista_lista[0])
print('===================')
print(lista_lista[1])
print('===================')
print(lista_lista[1:1])

print("========== fatiamento  ==============")
# Slices = fatiamento

print("========================")
# começa no indice x e vai até :y
valores =[10,50,30,40,70]
print(valores[0:3])
print(valores[0:]) # até o final
print(valores[0:5:2]) # de posição 0: até o :4º :pulando de  

print("========== Usando For para percorrer ==============")
# Lista com 7 usando for para percorrer uma lista
lista7 = [10, 50, 30, 40, 25, 60, 5]
for elemento in range(len(lista7)):
    print(elemento)
    
print("========== Quantos elementos tem na lista ==============")
print(len(lista7))

print("========== acesso a cada elemento com o indice i ==============")

for i in range(len(lista7)):
    print(lista7[i])