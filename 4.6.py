# Create a recursive function
def recursive_sum(a):
    result = 0
    if a > 0:
        result = recursive_sum(a-1) + a
    else:
        result = 0
    return result


number = int(input("Enter a number: "))
print("The recursive result is:", recursive_sum(number))
