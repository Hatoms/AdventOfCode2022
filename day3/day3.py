from string import ascii_lowercase, ascii_uppercase

with open('input.txt') as f:
    input = [line.strip() for line in f.readlines()]

priorities_lower = {letter: ord(letter)-96 for letter in ascii_lowercase}
priorities_upper = {letter: ord(letter)-38 for letter in ascii_uppercase}
priorities = {**priorities_lower, **priorities_upper}

# def split_list(a_list):
#     half = len(a_list)//2
#     return a_list[:half], a_list[half:]
#
#
# duplicates_item = []
# for items in input:
#     first_comp, second_comp = split_list(items)
#     duplicates_item.append([l for l in first_comp if l in second_comp][0])

duplicates_item = []
for i in range(0, len(input)-2, 3):
    group = input[i:i+3]
    item = [l for l in group[0] if l in group[1] and l in group[2]]
    duplicates_item.append(item[0])
    print(i)

sum_prio = sum([priorities[l] for l in duplicates_item])
print(sum_prio)
