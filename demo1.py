def add(x, y): return x + y
def substrct(x,y): return x -y
def multiply(x,y): return x * y
def divide(x,y): return x / y
#def printHello(): print("Hello")
#def print_with_argument(username,job) : print ("Hello %s , wellcome to %s"%(username,job))
  print_with_argument("DonPaw","CDC")

  #MenuList
print("Select the Method")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")
#print("5.Simple print")
#print("6.Print with Argument")

choice = input("Pick the number of menu   ")

num1 = int(input("First number : "))
num2 = int(input("Second number : "))

if choice == '1' : print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2' : print(num1,"-",num2,"=", substrct(num1,num2))
elif choice == '3' : print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4' : print(num1,"/",num2,"=", divide(num1,num2))
#elif choice == '5' : printHello
#elif choice == '6' : print_with_argument
else: print("invalid input")



         








