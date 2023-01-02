with open('input.txt') as f:
    input = [line.strip() for line in f.readlines()]

score1 = {
    'A X':4,
    'A Y':8,
    'A Z':3,
    'B X':1,
    'B Y':5,
    'B Z':9,
    'C X':7,
    'C Y':2,
    'C Z':6,
}

score2 = {
    'A X':3,
    'A Y':4,
    'A Z':8,
    'B X':1,
    'B Y':5,
    'B Z':9,
    'C X':2,
    'C Y':6,
    'C Z':7,
}

total_score = sum([score2[i] for i in input])
print(total_score)
