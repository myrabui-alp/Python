# Slice list into 3 equal chunks and reverse each chunk

def slice_list(list1):
    first = list1[:len(list1)//3:1]
    print(f"\nChunk 1 {first}")
    first.reverse()
    print(f"\nAfter reversing it {first}")

    second = list1[len(list1)//3:len(list1)//3*2:1]
    print(f"\nChunk 1 {second}")
    second.reverse()
    print(f"\nAfter reversing it {second}")
    third = list1[len(list1)//3*2::1]
    print(f"\nChunk 1 {third}")
    third.reverse()
    print(f"\nAfter reversing it {third}")


listDemo = [11, 45, 8, 23, 14, 12, 78, 45, 89]
slice_list(listDemo)
