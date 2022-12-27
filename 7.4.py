# Concatenate two lists in the following order

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
result = []
for x in list1:
    for y in list2:
        result.append(x+y)
print(result)
