#Group: Sahiti Moduga, Cameron Wall, Jeffrey Xu

row = input("Enter a row number from 1 to 5: ")
row = int(row)

col = input("Enter a column number from 1 to 5: ")
col = int(col)

grid = [[0 for x in range(5)] for y in range(5)]
grid[row - 1][col - 1] = 1

for i in range(5):
    for j in range (5):
        print(grid[i][j], end = ' ')
    print()