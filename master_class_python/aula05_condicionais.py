# Condicionais + Simples, Composto, Encadeado

print("=================Média================")

nota1 = (input("Digite a primeira nota: "))
nota2 = (input("Digite a segunda nota: "))


def calc_media(nota1 = nota1, nota2 = nota2):
    media = (float(nota1) + float(nota2))/2
    print(media)
    if (media>=7.0):
        print(f"Aluno foi aprovado com média: {media}")
    elif(media > 5.0) and (media<7.0):
        print(f"Aluno em recuperação com média: {media}")    
    else:
        print(f"Aluno reprovado com a média {media}")    


calc_media()