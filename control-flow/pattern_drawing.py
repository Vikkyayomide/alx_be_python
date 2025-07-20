size = int(input("Enter the size of the pattern: "))
row = 0

while row < size:
    for _ in range(size):
        print("*", end="")
    print()  # Move to next line after printing one row
    row += 1
