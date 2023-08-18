shopping_list=[]
#print(type(shopping_list))

shopping_list=["Nutella","Toothpaste","Pocket knife","Football"]
#print(len(shopping_list))

def print_list(data:list):
    for i in range(len(data)):
        print(data[i])



shopping_list.append(456)
shopping_list.reverse()
print_list(shopping_list)

# create a function using for loop to print all the elements in a list
# create a function using while loop to take input from user
# if user put STOP then the program will stop and print the list elements

def number_snatcher():
    a_list=[] # list created
    user_input=0 # variable created
    while(user_input!="STOP" or user_input!="stop"): # while loop condition
        user_input=input("ENTER the value quickly, I dont have time for drama:") # taking user input
        a_list.append(user_input) # adding element in the list
    
    print_list(a_list) # printing the list

number_snatcher()

