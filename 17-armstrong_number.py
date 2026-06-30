#by using For loop
print("FOR LOOP")

num = int(input("Enter a number: "))

power = len(str(num))
sum = 0

for digit in str(num):
    sum += int(digit) ** power

if sum == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")


#by using While loop
print("WHILE LOOP")

num = int(input("Enter a number: "))

num1 = num
power = len(str(num))
sum = 0

while num1 > 0:
    digit = num1 % 10
    sum += digit ** power
    num1 //= 10

if sum == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")