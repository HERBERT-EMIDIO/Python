# Métodos de Listas
print("============ Lista original ====================")
lista =[1, 3, 12, 8, 2]
print("Lista antes do append:", lista)

print("============== append (100) no final ==================")
lista.append(100) # adiciona o elemento 100 ao final
print(lista)

print("============== insert (200) na posição após que eu determinar ============")
lista.insert(3, 200)
print(lista)

print("======= extend (lista2) add a lista toda criada ao final da lista antiga  ======")
lista2 = [12,13,14]
lista.extend(lista2)
print(lista)


print("======= .pop() para eliminar o último elemento nao precisa passar o indice ======")
lista.pop()
print(lista) # eliminando o elemento 14

print("======= .pop(1) para eliminar o elemento do índice ======")
lista.pop(1) # eliminando o elemento 3
print(lista)

print("======= .remove(200) para eliminar o elemento que vc disser ======")
lista.remove(200)
print(lista)


print("======= .count(100) para contar quanto elemento eu tenho na minha lista ======")
lista.count(100)
print("Quantas vezes aparece o número 100 na minha lista: ", lista.count(100))


print("======= .sort() colocar minha lista em ordem crescente ======")
lista.sort()
print(lista)

print("======= .sort(reverse = True) colocar minha lista em ordem decrescente ======")
lista.sort(reverse=True)
print(lista)


# Funcões Para Listas

# len() para tamanho da minha lista
print("Função len():",len(lista))

# sum() para somar todos os elementos da lista
print("Função sum():",sum(lista))

# max() máximo elemento da minha lista 
print("função Max():",max(lista))

# min() mínimo elemento da minha lista
print("Função min():",min(lista))

