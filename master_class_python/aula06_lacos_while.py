

numero = 1

while numero < 10:
    print(numero ,  end =',') # 1,2,3,4,5,6,7,8,9,
    numero +=1



print("===============================================")

while numero < 10:
    print(numero)
    numero +=1
    
    
print("=================== pergunta o nome para X usuarios ============================")

nome = None
num = 1

#bloco infinito
while True:
    print()
    nome = input("Digite seu nome ou (S) para Sair do programa: ")
    if (nome.lower() != 's'):
        print(f"Nome do {num}º usuário: {nome.upper()}")
        num += 1
    else:
        print("Fim") 
        break
           
        

    