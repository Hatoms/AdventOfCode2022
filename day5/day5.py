import re

with open('input.txt') as f:
    input = f.readlines()

# READ INPUT
STACK_MAX = 8
NB_STACK = 9

stacks = [[] for i in range(NB_STACK)]

for i in range(STACK_MAX):
    row = input[i]
    for j in range(NB_STACK):
        if row[j*4 + 1] != ' ':
            stacks[j].append(row[j*4 + 1])
        

def move_crates1(s_from, s_dest, nb_crates):
    temp = stacks[s_from][:nb_crates]
    stacks[s_from] = stacks[s_from][nb_crates:] 
    temp.reverse()
    stacks[s_dest] = temp + stacks[s_dest]

def move_crates2(s_from, s_dest, nb_crates):
    temp = stacks[s_from][:nb_crates]
    stacks[s_from] = stacks[s_from][nb_crates:] 
    stacks[s_dest] = temp + stacks[s_dest]



for moves in input[STACK_MAX+2:]:
    nb_crates, s_from, s_dest = re.findall(r'\d+', moves)
    move_crates2(int(s_from)-1, int(s_dest)-1, int(nb_crates))

print(stacks)

ans = ""
for s in stacks:
    ans = ans+s[0]

print(ans)
