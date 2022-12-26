# Create a string made of the first, middle and last character
def string_first_middle_last(a):
    newString = a[0] + a[len(a)//2] + a[len(a)-1]
    return newString


string = "James"
print(string_first_middle_last(string))
