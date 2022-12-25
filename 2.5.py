# Accept a list of 5 float numbers as an input from the user

numbers = []
i = 0
while i < 5:
    number = float(input(f"Enter the number {i}: "))
    numbers.append(number)
    i += 1

print("The result is: ", numbers)
