# Find the intersection (common) of two sets and remove those elements from the first set
def intersection(set1, set2):
    intersectionSet = set1.intersection(set2)
    newSet1 = set1
    for x in intersectionSet:
        for y in set1:
            if x == y:
                newSet1.remove(x)
    print(
        f"\nIntersection is {intersectionSet}\nFirst Set after removing common element {newSet1}")


first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
intersection(first_set, second_set)
