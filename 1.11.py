# Write a Program to extract each digit from an integer in the reverse order
def extract_integer_digit(number):
    while number > 0:
        c = number % 10
        number = number//10
        print(c, end=" ")


number = int(input("Enter a number "))
extract_integer_digit(number)
