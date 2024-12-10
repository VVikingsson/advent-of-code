import re

def is_valid(map, i, j):
    return 0 <= i < len(map) and 0 <= j < len(map[i])

with open("inputs/day08.txt", "r") as file:
    contents = file.readlines()

map = [[e for e in row.strip()] for row in contents]

antennas = {}
antinodes = set()
part2_antinodes = set()

for i in range(len(map)):
    for j in range(len(map[i])):
        current = map[i][j]
        if re.match(r"\w|\d", current):
            if not map[i][j] in antennas:
                antennas[current] = []

            antennas[current].append((i, j))
        

            for antenna in antennas[current]:
                if antenna != (i, j):
                
                    i_diff = i - antenna[0]
                    j_diff = j - antenna[1]
                    low_i = antenna[0] - i_diff
                    low_j = antenna[1] - j_diff
                    high_i = i + i_diff
                    high_j = j + j_diff

                    if is_valid(map, low_i, low_j):
                        antinodes.add((low_i, low_j))
                    if is_valid(map, high_i, high_j):
                        antinodes.add((high_i, high_j))

                    a = antenna[0]
                    b = antenna[1]
                    while is_valid(map, a, b):
                        part2_antinodes.add((a, b))
                        a -= i_diff
                        b -= j_diff

                    a = antenna[0]
                    b = antenna[1]
                    while is_valid(map, a, b):
                        part2_antinodes.add((a, b))
                        a += i_diff
                        b += j_diff



for a in part2_antinodes:
    print(a)
    map[a[0]][a[1]] = "#"
for row in map:
    print("".join(row))                                                                                            

print(len(antinodes))
print(len(part2_antinodes))