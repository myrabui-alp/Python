# Write a program to count occurrences of all characters within a string
string = "Apple"
new_dict = dict()
i = 0
while i < len(string):
    new_dict[string[i]] = string.count(string[i])
    i += 1
print(new_dict)
