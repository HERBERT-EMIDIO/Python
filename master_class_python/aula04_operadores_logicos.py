# 1. AND (and)

a = 10
b = 20
c = 30

if a < b and b < c:
    print("Ambas as condições são verdadeiras.")
else:
    print("Pelo menos uma das condições é falsa.")

# 1. or

a = 10
b = 20
c = 5

if a < b or b < c:
    print("Pelo menos uma das condições é verdadeira.")
else:
    print("Ambas as condições são falsas.")
    
print("======================Operador or ===============================")    


"========================"
porta = 'F'
janela ='V'

disparou_alarme = (porta.lower() != 'f') or (janela.lower() != 'f')
msg = "O alarme foi ativado; porta ou janela ou as duas abertas? " + str(disparou_alarme)

print(msg)
"========================"

print("======================== not ==============================")    

tem_dinheiro = True
msg = " tenho dinheiro: " + str(tem_dinheiro)
print(msg) # True

tem_dinheiro = not tem_dinheiro
msg = " tenho dinheiro: " + str(tem_dinheiro)
print(msg) # False