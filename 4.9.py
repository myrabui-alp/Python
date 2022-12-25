# Find the largest item from a given list
def largest_number(numbers):
    max = numbers[0]
    for i in numbers:
        if i > max:
            max = i
    return max


x = [4, 6, 8, 24, 12, 2]
print("The largest number of", x, "is", largest_number(x))
