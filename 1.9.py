# Check Palindrome Number

def check_palindrome(a):
    b = 0
    d = a
    c = d % 10
    while c > 0:
        b = b*10+c
        d = d//10
        c = d % 10

    if a == b:
        print(f"Yes. The given number is palindrome number")
    else:
        print(f"No. The given number is not palindrome number")


number = int(input("Enter a number "))
check_palindrome(number)
