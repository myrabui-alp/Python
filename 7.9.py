# Replace list’s item with new value if found

list1 = [5, 10, 15, 20, 25, 50, 20]
for x in list1:
    if x == 20:
        list1[list1.index(x)] = 200
        break
print(list1)
