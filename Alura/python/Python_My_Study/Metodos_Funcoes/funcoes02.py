
# FUNÇÕES
# reutilizar codigos:
# 1. O que é uma função?
# 2. Como Usar uma função? 
"""
#imprimi uma mensagem( int, float, str) no console (terminal, cmd)
print()

#Retornar um dado informado pelo usuário(entrada padrão) e pode receber uma String
input()

#Recebe uma lista e retorna o tamanho dessa lista
len()

#Retorna o maior valor de uma lista
max()
"""

# 3. Criação de Funções:
# 3.1 Função inicial

# cria-se com def nomeFuncao():
print()

def saudacao():
    print("Seja bem-vindo!!!")
    print("Olá !!!")


# chamando a função    nomeFuncao()
saudacao()#Seja bem-vindo!!! Olá !!

print()

# parametros na função
def instrumento(modelo, marca):
   print(f"Gitarra: {modelo}, {marca}")

instrumento('LesPaul','Guibson')

print()

# parametros na funcão 2
def escolaSaudacao(nome,curso):
    print(f"Olá, {nome}, o seu curso é {curso}")


escolaSaudacao("Herbert", "Python")

print()

# Funções com parametros default = por padrão
def escola(nome, curso = "Java"):
    print(f"Olá, {nome}, o seu curso é {curso}")


escola("Herbert", "py")#se não passar ocorrerá erro
print()
print()
# Funções com retorno:
# Retornando um print
def soma(num1, num2):
    print(num1+num2)

soma(12,12)
print()
# Função retornando uma soma:
#obs: não há possibilidade de leitura de cód após o return

def mult(numberOne, numberTwo):
    return numberOne*numberTwo

result = mult(12,2)

print(result)

print("=========exercício calculadora =============")
print()

def calculadora(number1,number2, operação ='+'):
    if operação =='+':
        return number1 + number2
    elif operação =='-':
        return number1 - number2
    elif operação =='*':
        return number1 * number2
    elif operação =='/':
        return number1 / number2
    
calc = calculadora(12,2,'/')  
print(f"Calculadora {calc}")  