numbers = []

n = int(input("How many numbers? "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

largest = max(numbers)
smallest = min(numbers)

print("Largest =", largest)
print("Smallest =", smallest)