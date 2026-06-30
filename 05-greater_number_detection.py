num1 = int(input("Enter number :"))
num2 = int(input("Enter number :"))
num3 = int(input("Enter number :"))

if(num1 >= num2 and num1 >= num3):
    print( " num1 is greater", num1)
elif(num2 >= num1 and num2 >= num3):
    print("num2 is greater", num2)
else:
    print("num3 is greater", num3)