#by using For loop
print("FOR LOOP")

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")

#by using While loop
print("WHILE LOOP")

num = int(input("Enter a number: "))

if num <= 1:
    print("Not Prime")
else:
    i = 2

    while i < num:
        if num % i == 0:
            print("Not Prime")
            break
        i += 1
    else:
        print("Prime")