# Métodos de Listas
# Métodos = é uma "função" atrelada a uma variável
lista =[1, 3, 12, 8, 2]
# append serve para adiciona um item ao final da lista.

print("Lista antes do append: ",lista) # [1, 3, 12, 8, 2]
lista.append(3.1415)
print("Usando append para adicionar ao final da lista: ", lista) # [1, 3, 12, 8, 2, 3.1415]
print();

# escolher a posição com insert(index, elemento):
lista.insert(0,'Herbert');
print("Usando o insert para adicionar na posição que desejo: posicao, elemento: ",lista) # ['Herbert', 1, 3, 12, 8, 2, 3.1415]
print()

#Juntar duas listas com extend():

lista2=[222,333,444]
lista.extend(lista2) # jogando os elemento criados na lista 2 no final da lista
print("Usando extend para juntar 2 listas: ", lista) #['Herbert', 1, 3, 12, 8, 2, 3.1415, 222, 333, 444]

print()

#Rermover o elemento com o pop: 
lista2.pop(); # sem parâmetros remove o último elemento
print(lista2); #[222, 333]
print()

print();
lista2.pop(0); #posição [0]
print("Removendo o elemento [0]=222 com o pop: ",lista2); #[333] o elemento que ficou
print()

# Usando o remove para excluir elemento específico: 
#obs : elementos iguais, o remove retira the first element 
lista3=["Herbert", "Felipe", "Emidio", 39, 39, 39, 39, True]
print()


lista3.remove("Emidio") 
print("REMOVENDO O ELEMENTO 'Emidio' COM O REMOVE: ",lista3)
print()

# Contar elementos de uma lista com Count:
print("Contar quantos elementos '39' minha lista possui: ", lista3.count(39));#4
print()
# Usando o index para saber a posição do elemento:
print("Qual a poisição do elemento 'Herbert'", lista3.index("Herbert")) #0
print("Qual a poisição do elemento True", lista3.index(True)) #6
print()

# Organização de uma lista com o sort:
lista4 =[10,90,50,70,3,26,1,1.25] 
lista4.sort(reverse=True) 
print(lista4);# [90, 70, 50, 26, 10, 3, 1.25, 1]
lista4.sort()
print(lista4);# [1, 1.25, 3, 10, 26, 50, 70, 90]
print()






 


