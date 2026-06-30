#BY using for loop

print("FOR LOOP")

num = int(input("Enter natural numbers:"))
fact = 1
for i in range(1, num + 1):
     fact *= i
print("factorial of number is ", fact)

#BY using while loop

print("WHILE LOOP")

num = int(input("Enter natural numbers:"))
fact = 1
i = 1

while i <= num:
     fact *= i
     i += 1
print("factorial of number is ", fact)
     
