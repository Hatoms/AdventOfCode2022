with open('input.txt') as f:
    input = f.readlines()

GRID_SIZE = 99

# with open('input_test.txt') as f:
#     input = f.readlines()

# GRID_SIZE = 5

grid = [[int(x) for x in line.strip()] for line in input]

# LVL 1

# visible = [[0 for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]

# for i in range(GRID_SIZE):
#     line = grid[i]
    
#     highest_tree = -1
#     for j in range(GRID_SIZE):
#         if line[j] > highest_tree:
#             visible[i][j] = 1
#             highest_tree = line[j]
#             if highest_tree == 9:
#                 break
    
    
#     highest_tree = -1
#     for j in range(GRID_SIZE-1, -1, -1):
#         if line[j] > highest_tree:
#             visible[i][j] = 1
#             highest_tree = line[j]
#             if highest_tree == 9:
#                 break

# for j in range(GRID_SIZE):
#     column = [grid[i][j] for i in range(GRID_SIZE)]

#     highest_tree = -1
#     for i in range(GRID_SIZE):
#         if column[i] > highest_tree:
#             visible[i][j] = 1
#             highest_tree = column[i]
#             if highest_tree == 9:
#                 break

#     highest_tree = -1
#     for i in range(GRID_SIZE-1, -1, -1):
#         if column[i] > highest_tree:
#             visible[i][j] = 1
#             highest_tree = column[i]
#             if highest_tree == 9:
#                 break


# sum_visible_trees = sum([sum(l) for l in visible])
# print(sum_visible_trees)


## LVL 2

def compute_scenic_score(i,j):
    ref = grid[i][j]

    k = 1
    nb_trees_left = 0

    while i-k >= 0:
        nb_trees_left += 1
        if grid[i-k][j] >= ref:
            break
        k += 1

    k = 1
    nb_trees_right = 0

    while i+k < GRID_SIZE:
        nb_trees_right += 1
        if grid[i+k][j] >= ref:
            break
        k += 1

    k = 1
    nb_trees_below = 0

    while j+k < GRID_SIZE:
        nb_trees_below += 1
        if grid[i][j+k] >= ref:
            break
        k += 1

    k = 1
    nb_trees_top = 0

    while j-k >= 0:
        nb_trees_top += 1
        if grid[i][j-k] >= ref:
            break
        k += 1

    return nb_trees_left * nb_trees_right * nb_trees_below * nb_trees_top

max_scenic_score = 0
for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        new_score = compute_scenic_score(i,j)
        max_scenic_score = new_score if new_score > max_scenic_score else max_scenic_score


print(max_scenic_score)
