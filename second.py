def add(p, q):
    return p + q

def subtract(p, q):
    return p - q

def multiply(p, q):
    return p * q

def divide(p, q):
    return p / q

print("please select the operation,")
print ("a. Add")
print("b. sumtract")
print("c .multiply")
print("d. divide")

choice = str(input("please enter the operation from above "))

a = int (input ("please enter the first number: "))
b = int(input ("please enter the second number"))

if choice == 'a':
    print(add(a,b))

elif choice == 'b':
    print(subtract(a,b))   

elif choice == 'c':
    print(multiply(a,b))     

elif choice == 'd':
    print (divide(a,b))

else:
    print("this is a invalid option please try again using a , b , c , d")   
        