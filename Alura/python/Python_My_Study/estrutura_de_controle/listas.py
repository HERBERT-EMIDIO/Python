
# Listas = estrutura de dados []
# obs: em python é permitido misturar os tipos das variáveis
# coleção de variáveis.


#criacão de uma lista com:  nome_da_lista  = []
notas = [7.9, 9.7, 8.2];

# Lista vazia [] 
listaVazia =[];

#criando uma lista com um metodo/funcao list() "lista vazia também"
listaConverterEmLista= list();

# tipos aleatorios
listaMisturada = [1, 2.3, True, 'Herbert']

#listas de listas... listas dentro de outra lista
lista_de_listas = [10,[1,2,3]];

#indexação e Slides
lista_index = [10,'Herbert', 3.1415,True];
print(lista_index[0]); # elemento 0 = 10
print(lista_index[1]); # elemento 2 = Herbert
print(lista_index[2]); # elemento 3 = 3.1415
print(lista_index[3]); # elemento 4 = True
print(lista_index[-1]); # fuciona como uma roleta. Logo o item -1 é o ultimo elemento 
#print(lista_index[4]); # elemento 5 = ERRO => IndexError: list index out of range

print("===============================================");
# fatiar/varrer lista de elementos:
dadosList = [10,50, 30, 40, 25, 60, 5];
print(dadosList[0:3]); # [10, 50, 30]  começa no 0 e vai até o index 2
print();
print(dadosList[3:6]); #[40, 25, 60] começando do index 3 até o 5. 
print();
print(dadosList[3:]); #[40, 25, 60, 5] começando do index 3 até o fim.
print();
print(dadosList[1:6:2]); #[50, 40, 60] começando do index 1 até o 6 com pulo de 2 em 2.
print();
print("======================= usando o for in==============================");

for elemento in dadosList:
    print(elemento);


print("================== len() =========================");

print("Tamanho da lista: ",len(dadosList)); #7

print(" ========= for ============");

for i in range(len(dadosList)):
    print(dadosList[i]);









