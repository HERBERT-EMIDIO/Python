# Com 1 parâmetro no meu Range() -> Rodando 10 vezes com o início no zero até 9
for variavel in range(10):
    print(variavel)
    
print("==============================================")

#  Com 2 parâmetro no meu Range() -> Rodando 10 vezes - início no 1 até 9
for variavel2 in range(1, 10):
    print(variavel2)
    
print("==============================================")
#  Com 3 parâmetro no meu Range() -> Rodando 10 vezes - início no 1 até 9 - pulando 3
for variavel_pula_3 in range(1, 10, 3):
    print(variavel_pula_3)
    
    
print("=================== Uso Prático ===========================")
# 3 notas de alunos, tirar a média.
soma = 0

for i in range(1, 4):
    nota = float(input(f"Digite a {i}º nota do aluno: "))
    
    soma = soma + nota


print(soma/3)    