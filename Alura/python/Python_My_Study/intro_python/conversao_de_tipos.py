# Conversão de Tipos

age ='26' #str
numberOne ='10'#str
numberTwo =1

print(age + numberOne);#2610 concatenação
#print(age + numberTwo); #ERRO ao tentar concatenar um str com um int

#================ aplicando a conversão para int() and str() and float() and bool() ====================#

age2 = '27'
print(age, type(age)); # str

age2_inteira = int(age);
print(age2_inteira, type(age2_inteira)); #int


input_height = input("Enter your heigth: ");
print(input_height, type(input_height)); #str
print();

input_height = int(input_height);
print(input_height,type( input_height)); #int
#=================== outra forma mais simples ===============
input_height2 = float(input("Enter your heigth: "));
print(input_height2,type(input_height2));

