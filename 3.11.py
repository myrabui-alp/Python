# Write a program to display all prime numbers within a range
# Check a prime number
def check_prime_number(a):
    i = 2
    while i <= a/2:
        if a % i == 0:
            return False
        i += 1
    return True

# List the prime numbers in a range


def list_prime_numbers(a, b):
    if a > b:
        return False
    else:
        j = a
        while j <= b:
            if check_prime_number(j) == True:
                print(j)
            j += 1


start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
list_prime_numbers(start, end)
