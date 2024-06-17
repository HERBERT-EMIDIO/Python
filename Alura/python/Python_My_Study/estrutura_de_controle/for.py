
# for = Para a variavel i dentro da determinada faixa de 10 valores faça!
for i in range(10):# contagem de i=0 até 10 logo de 0 até 9
    print(i);
print("===================")

#range = faixa de contagem

# com 2 parametros: até 5

for j in range(1,5):#1 até 4
    print(j);
print("================");

# com tres parametros: pulos de 3

for b in range(1, 12, 3):
    print(b);

print("=============== exercício =============");
# exercios: pegar 3 notas de um aluno: tirar uma media das 3 notas:
"""
media1Aluno=float(input("Digite a primeira nota: "));
media2Aluno=float(input("Digite a segunda nota: "));
media3Aluno=float(input("Digite a terceira nota: "));
"""
mediaAlunoTotal=0;  # variavél acumuladora.
for index in range(1,4):
    mediaAluno=float(input(f"Digite a primeira nota{index}: "));
    mediaAlunoTotal +=mediaAluno;
    
print(mediaAlunoTotal / index);
    

