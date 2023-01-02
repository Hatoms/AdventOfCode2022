with open('puzzle_input.txt') as f:
    input = [line.strip() for line in f.readlines()]


calories = list(map(lambda i : int(i) if i else 0, input))

# PART ONE

# i = 0
# max_elf = 0
#
# while i < len(calories):
#     new_elf = 0
#     while calories[i] != 0:
#         new_elf += calories[i]
#         i += 1
#         if i == len(calories):
#             break
#     max_elf = max(max_elf, new_elf)
#     i += 1
#
# print(max_elf)


# PART TWO

def update_top_three(max_elves, new_elf):
    if new_elf > max_elves[0]:
        return [new_elf, max_elves[0], max_elves[1]]
    elif new_elf > max_elves[1]:
        return [max_elves[0], new_elf, max_elves[1]]
    elif new_elf > max_elves[2]:
        return [max_elves[0], max_elves[1], new_elf]
    else:
        return max_elves

i = 0
max_elves = [0,0,0]

while i < len(calories):
    new_elf = 0
    while calories[i] != 0:
        new_elf += calories[i]
        i += 1
        if i == len(calories):
            break
    max_elves = update_top_three(max_elves, new_elf)
    i += 1

print(sum(max_elves))
