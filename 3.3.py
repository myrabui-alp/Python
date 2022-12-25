# Calculate the sum of all numbers from 1 to a given number
count = int(input("Enter the amount of numbers: "))
i = 0
sum = 0
numbers = []
while i < count:
    value = int(input(f"Enter the number {i} "))
    numbers.append(value)
    i += 1
for number in numbers:
    sum += number
print("The sum is: ", sum)
