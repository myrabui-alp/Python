# Write a program to count occurrences of all characters within a string
def check_unique(char, a):
    for x in char:
        if x == a:
            return False
        else:
            return True


def string_count_occurrences(a):
    char = []
    i = 0
    while i < len(a):
        if check_unique(char, a[i]) == True:
            char.append(a[i])
    for x in char:
        print(f"x: {a.count(x)}", end="")


string = "Apple"
string_count_occurrences(string)
