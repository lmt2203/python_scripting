# One way to create a 2D list is to create a list whose items are themselves lists.
L = [[1,2,3],
     [4,5,6],
     [7,8,9]]

# Indexing: we use 2 indices to access individual items. E.g, to get the entry in row r, column c, use L[r][c]

# Count how many entries are even:
count = 0
for r in range(3):
    for c in range(3):
        if L[r][c] %2 == 0:
            count = count + 1

count = sum([1 for r in range(3) for c in range(3) if L[r][c] % 2 == 0])

# Flattening a list:
[r for row in L for r in row]
