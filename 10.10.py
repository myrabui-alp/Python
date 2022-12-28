# Check if all items in the tuple are the same

tuple1 = (45, 45, 45, 45)


def check_all_items(a):
    i = a[0]
    for x in tuple1:
        if i != x:
            return False
        return True


print(check_all_items(tuple1))
