import re

with open("inputs/test.txt", "r") as file:
    contents = file.readlines()

map = [row for row in contents]

antennas = {}
antinodes = set()

for i in range(len(map)):
    for j in range(len(map[i])):
        if re.match(r"\w|\d", map[i][j]):
            if not map[i][j] in antennas:
                antennas[map[i][j]] = []

            antennas[map[i][j]].append((i, j))
        

            for antenna in antennas[map[i][j]]:
                if antenna != (i, j):
                    i_diff = i - antenna[0]
                    j_diff = j - antenna[1]
                    low_i = antenna[0] - i_diff
                    low_j = antenna[1] - j_diff
                    high_i = i + i_diff
                    high_j = j + j_diff

                    if 0 <= low_i and 0 <= low_j:
                        antinodes.add((low_i, low_j))
                    if high_i < len(map) and high_j < len(map[j]):
                        antinodes.add((high_i, high_j))


print(len(antinodes))

