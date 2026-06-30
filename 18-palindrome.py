#by using For loop
print("FOR LOOP")

num = input("Enter a number: ")

reverse = ""

for digit in num:
    reverse = digit + reverse

if num == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")

#by using While loop
print("WHILE LOOP")

num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if original == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")