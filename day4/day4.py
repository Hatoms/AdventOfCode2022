with open('input.txt') as f:
    input = [line.strip() for line in f.readlines()]

def clean_ids(ids):
    return [clean_id(id) for id in ids.split(',')]

def clean_id(id):
    return [int(num) for num in id.split('-')]

assignements = [clean_ids(line) for line in input]

def is_overlapping_completly(elves):
    elf1, elf2 = elves
    return ((elf1[0] >= elf2[0] and elf1[1] <= elf2[1]) or (elf2[0] >= elf1[0] and elf2[1] <= elf1[1]))

def is_overlapping(elves):
    elf1, elf2 = elves
    return not(elf1[1] < elf2[0] or elf2[1] < elf1[0])

overlapping = filter(is_overlapping, assignements)

print(len(list(overlapping)))
