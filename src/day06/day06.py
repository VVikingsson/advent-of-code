import re
from copy import deepcopy

def inbounds(map, i, j):
    return 0 <= i < len(map) and 0 <= j < len(map[i])

def solve(map, direction, location, is_real):
    i, j = location
    traps = 0
    done = False

    counter = 1
    while inbounds(map, i, j):
        if is_real:
            (print(100 * (counter // 5000)))

        counter += 1
        match direction:
            case "up":
                if is_real and solve(deepcopy(map), "right", (i, j), False) == "TRAPPED":
                    traps += 1
                if 0 <= i - 1:
                    if "#" in map[i-1][j]:
                        direction = "right"
                    elif "u" in map[i][j]:
                        return "TRAPPED"
                    else:
                        map[i][j].add("u")
                        i -= 1
                else:
                    map[i][j].add("u")
                    done = True
            
            case "down":
                if is_real and solve(deepcopy(map), "left", (i, j), False) == "TRAPPED":
                    traps += 1

                if i + 1 < len(map):
                    if "#" in map[i+1][j]:
                        direction = "left"
                    elif "d" in map[i][j]:
                        return "TRAPPED"
                    else:
                        map[i][j].add("d")
                        i += 1
                else:
                    map[i][j].add("d")
                    done = True
                
            case "left":
                if is_real and solve(deepcopy(map), "up", (i, j), False) == "TRAPPED":
                    traps += 1

                if 0 <= j - 1:
                    if "#" in map[i][j-1]:
                        direction = "up"
                    elif "l" in map[i][j]:
                        return "TRAPPED"
                    else:
                        map[i][j].add("l")
                        j -= 1
                else:
                    map[i][j].add("l")
                    done = True

            case "right":
                if is_real and solve(deepcopy(map), "down", (i, j), False) == "TRAPPED":
                    traps += 1

                if j + 1 < len(map[i]):
                    if "#" in map[i][j+1]:
                        direction = "down"
                    elif "r" in map[i][j]:
                        return "TRAPPED"
                    else:
                        map[i][j].add("r")
                        j += 1
                else:
                    map[i][j].add("r")
                    done = True
    
        if done:
            if not is_real:
                return "NOT TRAPPED"
            
            covered_ground = 0
            for i in range(len(map)):
                for set in map[i]:
                    if any([char in set for char in "udrl"]):
                        covered_ground += 1
            
            return covered_ground, traps

# Parse file
with open("inputs/day06.txt", "r") as file:
    contents = file.readlines()

map = [[set(element) for element in row.strip()] for row in contents]

# Find starting state
direction = ""
location = (0,0)

for i in range(len(map)):
    for j in range(len(map[i])):
        if "^" in map[i][j]:
            direction = "up"
            location = (i, j)
        if "v" in map[i][j]:
            direction = "down"
            location = (i, j)
        if "<" in map[i][j]:
            direction = "left"
            location = (i, j)
        if ">" in map[i][j]:
            direction = "right"
            location = (i, j)


print(solve(map, direction, location, True))

#print(covered_ground)
#print(traps)