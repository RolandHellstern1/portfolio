file1 = open('/home/roland/projects/advent/puzzle3.data', 'r')
Lines = file1.readlines()
file1.close()


board = []

for line in Lines:
    line = line.replace("\n", "")
    board.append(line)



def countTrees(map, down, right):
    trees = 0
    x = 0
    y = 0
    while True:
        y = y + down
        if y >= len(map):
            break
        x = (x + right) % len(map[y])
        if map[y][x] == '#':
            trees = trees + 1
    return trees

print(countTrees(board, 1, 3))


ergebnis = 1
for slopes in [[1,1],[1,3],[1,5],[1,7],[2,1]]:
    ergebnis = ergebnis * countTrees(board,slopes[0],slopes[1])

print(ergebnis)
