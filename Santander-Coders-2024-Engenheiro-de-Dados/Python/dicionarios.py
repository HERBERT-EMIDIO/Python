# Dicionário { chave : valor }

# Criando Dicionário com {} ou dict()
# Ex:
print("****************** Imprimindo o Dicionário *******************************")
dicionario = {}
dicionario = dict()
dicionario = {'nome': 'Herbert', 'idade': 40, 'altura': 1.83}

print(dicionario) #{'nome': 'Herbert', 'idade': 40, 'altura': 1.83}


print("********************* Acesso ao valor com[chave]****************************")
# Imprimir determinada posição com o nomeDicionario[chave]
print(dicionario['nome'])
print(dicionario['idade'])


print("********************** add elemento ***************************")
# Adicionar elementos
dicionario['programador'] = True
print(dicionario) # {'nome': 'Herbert', 'idade': 40, 'altura': 1.83, 'programador': True}

print("****************** sobrescrevendo ******************************")
# Sobrescrever o conteúdo - atribuindo um valor novo a uma chave já existente
dicionario['nome'] = 'Felipe'
print(dicionario['nome']) # Felipe

print("****************** usando o for para percorrer *******************************")
# Percorrer as chaves de um Dicionário com o for
for percorrer in dicionario:
    print(percorrer)
    
    
    
print("************* Percorrer a chave e o valor do Dicionário *********************")
for chave in dicionario:
    print(chave,':', dicionario[chave])
    
    
print('****** Verificando se existe uma chave ********')   
print('peso' in dicionario)   #False
print('altura' in dicionario) #True  