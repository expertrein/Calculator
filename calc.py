
print("Welcome")
print("what do you want to do?")

sele = input("select one  \n M for multiplication \n D for division \n A for addition \n S for substraction \n put your selection here: ")
select = sele.upper()   

num1 = int(input("Enter First number "))
num2 = int(input("Enter Second number "))

def addition():
        add = num1 + num2
        print("The answer is: " , add)

def Subtraction():
        subt = num1-num2
        print("The answer is: " , subt)

def Division():
        div = num1 / num2
        print("The answer is: " , div)

def Multiplication():
        mul = num1 * num2
        print("The answer is: " , mul)

if select == "A":
    addition()
elif select == "S":
    Subtraction()
elif select == "D":
    Division()
elif select == "M" :
    Multiplication()








