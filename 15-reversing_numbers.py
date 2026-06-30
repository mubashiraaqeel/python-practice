#by using For loop
print("FOR LOOP")

num = int(input("Enter a number: "))

reverse = 0

for i in str(num):
     digit = num % 10
     reverse = reverse * 10 + digit
     num //= 10
     print("Reversed Number =", reverse)


#by using While loop
print("WHILE LOOP")

num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reversed Number =", reverse)
