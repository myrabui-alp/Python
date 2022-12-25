# Print the following pattern
col = int(input("Enter the maximum start: "))

for i in range(0, col):
    for j in range(0, i+1):
        print("*", end=" ")
    print("\n")
for i in range(col-1, 0, -1):
    for j in range(0, i):
        print("*", end=" ")
    print("\n")
