# function
def print_yourName():
    name=input("Enter your name:")
    print(f"Your name is {name}")

def find_meReminder(num1:int,num2:int):
    print(f"[if we divide {num1} and {num2} then the remainder will be {num1%num2}")

find_meReminder(num1=5, num2=5)

def add(num1,num2):
    print(f"{num1}+{num2}={num1+num2}")

def sub(num1,num2):
    print(f"{num1}-{num2}={num1-num2}")

def mul(num1,num2):
    print(f"{num1}x{num2}={num1*num2}")

def div(num1,num2):
    print(f"{num1}/{num2}={num1/num2}")

def calculator():
    repeat="Y"
    while(repeat=="Y" or repeat=="y"):
        numA=int(input("Enter the 1st number:"))
        numB=int(input("Enter the 2nd number:"))
        sign=input("Enter a sign:")
        if(sign=="+"):
            add(num1=numA,num2=numB)
        elif(sign=="-"):
            sub(num1=numA,num2=numB)
        elif(sign=="x"):
            mul(num1=numA,num2=numB)
        elif(sign=="/"):
            if(numB==0):
                print("0 can not be a divisor!")
            else:
                div(num1=numA,num2=numB)
        elif(sign=="%"):
            find_meReminder(num1=numA,num2=numB)
        else:
            print("This is not a valid input")
        repeat=input("Repeat?(Y/N):")

calculator()

