#BY using for loop

print("FOR LOOP")

num = int(input("Enter natural numbers:"))
sum = 0 

for i in range(1, num + 1):
   sum += i
print("Sum = " ,sum)

#BY using while loop

print("WHILE LOOP")

num = int(input("Enter natural numbers:"))
sum = 0
i = 1

while i <= num:
   sum += i 
   i += 1

print("Sum = ", sum)
  