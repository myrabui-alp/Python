# Count all letters, digits, and special symbols from a given string
def string_count_letter_digit_symbol(a):
    i = 0
    char = 0
    digit = 0
    symbol = 0
    while (i < len(a)):
        if a[i].isdigit() == True:
            digit += 1
        elif a[i].isalpha() == True:
            char += 1
        else:
            symbol += 1
        i += 1
    print(
        f"Total counts of chars, digits, and symbols\nChars = {char}\nDigits = {digit}\nSymbol = {symbol}")


string_count_letter_digit_symbol("P@#yn26at^&i5ve")
