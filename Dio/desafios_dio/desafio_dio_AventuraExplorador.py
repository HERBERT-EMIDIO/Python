# Desafio: A Aventura do Explorador

# Entrada de um número inteiro positivo representando a quantidade de passos
quantidade_passos = int(input())

# TODO: Adicione uma condição para verificar se a quantidade de passos é positiva.
# O programa deve imprimir uma mensagem indicando o progresso do explorador na floresta.
# Utilize um laço de repetição para simular os passos do explorador.

for i in quantidade_passos:
    print(f"Explorador: {i+1} passo")
    i+=1

#  Se a quantidade de passos for zero, imprima "Nenhum passo dado na floresta."
#  Caso contrário, utilize um loop for para imprimir a mensagem do explorador, indicando o número do passo.