#without third variable

a = int(input("enter number:"))
b = int(input("enter number:"))

a , b = b, a

print("After Swapping")
print("a =", a)
print("b =", b)

#with third variable

a = int(input("enter number:"))
b = int(input("enter number:"))

c = a
a = b 
b = c

print("After Swapping")
print("a =", a)
print("b =", b)