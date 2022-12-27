# Get all values from the dictionary and add them to a list but don’t add duplicates

def get_unique(a):
    newSet = set()

    for x in a:
        newSet.add(a[x])
    newList = list(newSet)
    print(newList)


speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44,
         'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

get_unique(speed)
