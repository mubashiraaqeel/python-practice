def average(numbers):
    return sum(numbers) / len(numbers)

numbers = []

n = int(input("How many numbers? "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

print("Average =", average(numbers))