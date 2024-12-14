import re

with open("inputs/day03.txt", "r") as file:
    contents = file.read()

pattern_1 = r"mul\((\d{1,3},\d{1,3})\)"

matches = re.findall(pattern_1, contents)

total_1 = sum([int(split_match[0]) * int(split_match[1]) for split_match in [match.split(",") for match in matches]])


pattern_2 = r"mul\((\d{1,3},\d{1,3})\)|(do\(\))|(don't\(\))"

matches = re.findall(pattern_2, contents)

total_2 = 0

enabled = True
for factors, do, dont in matches:
    if do == "do()":
        enabled = True
    elif dont == "don't()":
        enabled = False
    elif enabled:
        n, m = factors.split(",")
        total_2 += int(n)*int(m)

print([match for match in matches])



print(total_1)
print(total_2)