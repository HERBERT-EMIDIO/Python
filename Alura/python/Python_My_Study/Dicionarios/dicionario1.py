# Dicionários:

# Criando dicionários
lista= []; # lista
dicionario ={}; # dicionario vazio
dicionario_vaizo = dict(); # usando dict para criar um dicionário vazio por padrão

# criando Dicionario com conteúdo: chave, valor

dicionario02 = {'name': 'Herbert', 'age':39, 'height':1.83}
print(dicionario02);
print("==========")
# acesso ao dicioário:
# acessar a idade

print("====idade======")
print(dicionario02['age']) #39


print("====add======")
# Adicionando elementos em um Dicionário
dicionario02['Developer']=True
print(dicionario02) #{'name': 'Herbert', 'age': 39, 'height': 1.83, 'Emidio': True}

# obs: se já existir a chave irá sobrescrever-la.
dicionario02['age']=40
print("New age is:  ", dicionario02['age'])
print('=============')


# Percorrendo um dicionário 
print("percorrendo o dicionario com o for")
for varChave in dicionario02:
    print(varChave, dicionario02[varChave])


# Testando a existência de uma chave
print("====== Teste existencia de valor =========")
print('peso' in dicionario02);# a chave peso esta dentro de Dicionario02? False
print('age' in dicionario02);# a chave age esta dentro de Dicionario02?True

