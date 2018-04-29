def add(x, y): return x + y
def substrct(x,y): return x -y
def multiply(x,y): return x * y
def divide(x,y): return x / y

print("Select the Method")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

choice = input("Pick the number of menu   ")

num1 = int(input("First number : "))
num2 = int(input("Second number : "))

if choice == '1' : print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2' : print(num1,"-",num2,"=", substrct(num1,num2))
elif choice == '3' : print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4' : print(num1,"/",num2,"=", divide(num1,num2))
else: print("invalid input")






