# Funções

# Exemplos:
'''
print() 
max()
min()
len()
input()
'''

# Criando uma função -> def nomeDaFuncao():
def saudação():
    print("Seja bem-vindo(o)!")
    nome = input('Qual seu nome? ')
    print(f"Olá, {nome} é um prazer ter você fazendo parte deste curso de python!")
    
saudação()    
    



# Com parâmetros
def saudacao2(nome, curso):
    print(f"Olá, {nome} que bom ter você fazendo o curso de {curso}.")
    
saudacao2('Herbert', 'Python')    
    

# Com Parâmetros default = deixar por padrao o curso = Python
def saudacao3(nome, curso = 'Python'):
    print(f"Olá, {nome} que bom ter você fazendo o curso de {curso}.")
    
saudacao3('Herbert')    
    
    
    
# Funções com retorno => não devemos imprimir, devemos trabalhar com resultado 
def soma(num1, num2):
    return num1 + num2   



valor_calculo = soma(5,7) 
print(f'Soma:',valor_calculo) 


# Calculadora

def calculadora(num1, num2, operacao ='+'):
    if(operacao == '+'):
        return num1 + num2
    elif(operacao == '-'):
        return num1 - num2
    elif(operacao == '*'):
        return num1 * num2 
    
    
calc = calculadora(2,2,'*')    
print(calc)
calc2 = calculadora(12,2)    
print(calc2)