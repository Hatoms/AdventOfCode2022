import re

with open('input.txt') as f:
    input = f.readlines()



input = [line.strip() for line in input]
moves = [[line[0], int(re.findall(r'\d+', line)[0])] for line in input]

visited_square = ['0/0']

nodes = [[0,0] for i in range(10)]

h_x = 0
h_y = 0
t_x = 0
t_y = 0

def move_tail(h_x, h_y, t_x, t_y):
    diff_x = h_x - t_x
    diff_y = h_y - t_y
    
    if abs(diff_x) < 2 and  abs(diff_y) < 2:
        return t_x, t_y

    if h_x == t_x:
        t_y = t_y + diff_y // 2
    elif h_y == t_y:
        t_x = t_x + diff_x // 2
    elif abs(diff_x) == 2:
        t_x = t_x + diff_x // 2
        t_y = t_y + diff_y
    else:
        t_x = t_x + diff_x
        t_y = t_y + diff_y // 2
    return t_x, t_y


for dir, nb_case in moves:
    if dir == 'U':
        for i in range(nb_case):
            nodes[0][1] += 1
            for n in range(1, 10):
                nodes[n][0],nodes[n][1] = move_tail(nodes[n-1][0],nodes[n-1][1], nodes[n][0], nodes[n][1])
            visited_square.append(str(nodes[9][0]) + '/' + str(nodes[9][1]))

    elif dir == 'D':
        for i in range(nb_case):
            nodes[0][1] -= 1
            for n in range(1, 10):
                nodes[n][0],nodes[n][1] = move_tail(nodes[n-1][0],nodes[n-1][1], nodes[n][0], nodes[n][1])
            visited_square.append(str(nodes[9][0]) + '/' + str(nodes[9][1]))
            
    elif dir == 'R':
        for i in range(nb_case):
            nodes[0][0] += 1
            for n in range(1, 10):
                nodes[n][0],nodes[n][1] = move_tail(nodes[n-1][0],nodes[n-1][1], nodes[n][0], nodes[n][1])
            visited_square.append(str(nodes[9][0]) + '/' + str(nodes[9][1]))
    
    else :
        for i in range(nb_case):
            nodes[0][0] -= 1
            for n in range(1, 10):
                nodes[n][0],nodes[n][1] = move_tail(nodes[n-1][0],nodes[n-1][1], nodes[n][0], nodes[n][1])
            visited_square.append(str(nodes[9][0]) + '/' + str(nodes[9][1]))
    
print(visited_square)
print(len(set(visited_square)))