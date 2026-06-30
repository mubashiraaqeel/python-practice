#by using For loop
print("FOR LOOP")

n = int(input("How many terms? "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

#by using While loop
print("WHILE LOOP")

n = int(input("How many terms? "))

a = 0
b = 1
i = 1
while i <= n:
   print(a, end=" ")
   c = a + b
   a = b
   b = c
   i += 1

