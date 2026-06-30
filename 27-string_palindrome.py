string = input("Enter a string: ").lower()

reverse = ""

for char in string:
    reverse = char + reverse

if string == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")