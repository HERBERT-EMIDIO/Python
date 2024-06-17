#Enquanto = while

# =======  sem While ========
"""
numberAny = int(input("Enter Any Number: "));

password = 12;

if numberAny == password:
    print("Congratulations!");
else:
    print("wrong passoword!");

"""

# ======= Com While ======== repeticao de codigo === loop === ctrl + c

numberAny = int(input("Enter Any Number: "));

password = 12;

while  numberAny != password:
    print("wrong passoword!");
    numberAny = int(input("Enter Any Number: "));

print("Congratulations!");

# ========= Exemplo 2 ====  estrutura While com contador:

contador = 0;

while contador <=5:
    print(contador);

    contador+= 1;

print("End of repeating loop!");

