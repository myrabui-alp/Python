# Calculate the multiplication and sum of two numbers
def mult_or_sum(a, b):
    if a*b >= 1000:
        return a+b
    else:
        return a*b


number1 = 20
number2 = 30
given = mult_or_sum(number1, number2)
print(f"number1: {number1} \nnumber2: {number2} \nThe result is {given}")

number1 = 30
number2 = 40
given = mult_or_sum(number1, number2)
print(f'\nnumber1: {number1} \nnumber2: {number2} \nThe result is {given}')
