# usando o prompt do python 
# ctr + shift + ' para abrir o terminal
# py no terminal para entrar no prompt de comando
 
 


#input => obs: o input retorna uma str

nome = input("Digite seu nome: ") 

# Casting conversão do tipo de dados do recebimento do input()=str para int

idade = int(input("Digite sua idade: ")) 
 
# criando uma função de apredsentacao():
# o nome e a idade = recebido do input fica como default 

def apresentacao(nome=nome, idade=idade):
     print(f"Meu nome é {nome} e tenho {idade} anos de idade.")
    
    

#chamando a função
apresentacao()


# operadores
""" 
    # ==
    # > ou >=
    # < ou <=
    # (!=)
    
"""

# função print()

valor = 1233.126
print(f"valor:{valor: .2f}") #valor: 1233.13 arredonda aparti do 6 para cima. 

     
 
 