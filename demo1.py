def add(x, y): return x + y
def substrct(x,y): return x -y
def multiply(x,y): return x * y
def divide(x,y): return x / y
def printHello(): print("Hello")
def print_with_argument(username,job): print ("Hello %s , wellcome to %s"%(username,job))

  #MenuList
print("Select the Method")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")
print("5.Simple print")
print("6.Print with Argument")

choice = int(input("Pick the number of menu   "))

if choice <= 4 :
    num1 = int(input("First number : "))
    num2 = int(input("Second number : "))
else :
    num3 = str(input("char1: "))
    num4 = str(input("char2 : "))
    print_with_argument(num3,num4)

if choice == 1 : print(num1,"+",num2,"=", add(num1,num2))
elif choice == 2 : print(num1,"-",num2,"=", substrct(num1,num2))
elif choice == 3 : print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == 4 : print(num1,"/",num2,"=", divide(num1,num2))
elif choice == 5 : printHello
elif choice == 6 : print_with_argument
else: print("invalid input")









