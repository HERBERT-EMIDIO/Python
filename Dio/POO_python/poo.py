# estudo em POO

class FantasmaPacman:
    
    def __init__(self, nome, cor, apelidio):
        self.nome = nome
        self.cor = cor
        self.apelidio = apelidio



    def apresentar(self):
        print(f"Olá, eu sou o fantasma {self.nome}, conhecido como {self.apelidio}") 

    
    def mover(self, direcao):
        print(f"{self.nome} está se movendo para {direcao}.")



# Criando => instanciando os fantasmas (pac-man)

blink = FantasmaPacman("Blink", "vermelho", "Perseguidor")
pink = FantasmaPacman("Pinky", "rosa", "Acelerador")
inky = FantasmaPacman("Inky", "azul", "T/rapaceiro")
clyde = FantasmaPacman("Clyde", "laranja", "Assustador")


blink.apresentar()        
        