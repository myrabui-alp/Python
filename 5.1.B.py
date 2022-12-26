# Create a string made of the middle three characters
def string_first_middle_last(a):
    newString = a[len(a)//2-1] + a[len(a)//2] + a[len(a)//2+1]
    return newString


string1 = "JhonDipPeta"
print(string_first_middle_last(string1))
string2 = "JaSonAy"
print(string_first_middle_last(string2))
