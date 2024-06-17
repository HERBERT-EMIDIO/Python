

"""
idade = 20;

if idade >= 18:
        print("You are of legal age!");
else:
        print("you are not of legal age!");
"""


#===== I received a value, I converted the value and conditioned.
"""
age = int(input("Enter you age: "));
if age >=18 :
    print("you are legal age:");
else: 
    print("you not are legal age:");

"""

# ====== exercise two: ======  Student Average
# if / else if = elif / conparacao conjunta com and / or

gradeOne = float(input("Enter the first test score: "));
gredeTwo =float(input("Enter the second test score: "));
presece = True;
                
testAverage = (gradeOne + gredeTwo) /2;
   
   
if testAverage >= 7.0 and presece:
    print("Approved");
    print("Congratulations");
elif testAverage >= 5.0 and presece:
    print("Recovery");
else:
    print("Desapproved");