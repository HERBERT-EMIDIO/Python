# interacao de sequencia de dados

# """
# para cada item em sequencia impria o item
# for item in sequencia:
#     instrucoes para item da sequencia

# """
print("============EX2==============")
# lista_valores = [12,23,34,45,54,60]

# for i in lista_valores:
#     print(i)
    
    

# palavra = 'herbert'    

# for letra in palavra:
#     print(letra) 
    
    
    
print("============EX2 Range ==============")


# for i in range(palavra,10):
#     print(i)


print("============ pegar 10 vez um nome ==============")


# nome = input("Digite seu nome: ")

# for valor in range(10):
#     print(f"{valor+1}º {nome}")



print("============ pegar 10 vez um nome para lista de aniversario ==============")


# lista_aniver = []

# for valor in range(10):
#     nomes_lista = input("Nome Ccnvidado: ")
#     lista_aniver.append(nomes_lista)


# print(lista_aniver)
    
    
    
print("============ pegar só os pares com o range usando 3 incrementos(inicio, fim, salto) ==============")

# for x in range(2,22,2):
#     print(x, end="<") #2>4>6>8>10>12>14>16>18>20>
# print()
    
print("============ pegar só os pares com o range usando 3 incrementos(inicio, fim, salto) ==============")

# print()
# for x in range(22, 2, -2):
#     print(x, end = ">")    
# print()
    
print("============ Lista com nomes de pedras usando o continue=============")

#tupla
pedras_listas = ( 'Rubi','Esmeralda','Quartzo','Safira','Diamente', 'Turmalina')

for i in pedras_listas:
    if i == "Diamente":
        continue # true? ele passa e vai ignorar o Diamente
    print(i)
    
    # tempo: video : 2:39 (https://www.youtube.com/watch?v=-VeVq64Fgw0) 
        
    