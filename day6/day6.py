with open('input.txt') as f:
    input = f.readlines()

code = input[0]
# box = code[:3]
# for i in range(3, len(code)):
#     if len(set(box)) != 3 or code[i] in box:
#         box = code[i-2:i+1]
#         continue
#     print(i+1)
#     break


box = code[:13]
for i in range(13, len(code)):
    if len(set(box)) != 13 or code[i] in box:
        box = code[i-12:i+1]
        continue
    print(i+1)
    break