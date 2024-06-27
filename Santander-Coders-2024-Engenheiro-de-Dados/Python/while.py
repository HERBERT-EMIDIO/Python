numero_sorteado = 15

numero_escolhido = int(input("Informe um número entre 1 e 20: "))

while numero_escolhido != numero_sorteado:
     print('VocÊ errou o número')
     
     numero_escolhido = int(input("Informe um número entre 1 e 20: "))
     # obs: ctr+c para o loop
     

print('Parabéns número correto!')    



# Estrutura com o contador:
contador = 0
while contador < 5:
    print(contador)
    contador = contador + 1 