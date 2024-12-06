with open("inputs/day04.txt", "r") as file:
    contents = file.readlines()

# Remember tehres a new line at the end of every line

total = 0
for i in range(len(contents)):
    for j in range(len(contents[i])):
        
        if contents[i][j] == "X":
            
            east, west, north, south = False, False, False, False
            
            if j + 3 < len(contents[i]):
                east = True
            if j - 3 >= 0:
                west = True
            if i + 3 < len(contents):
                south = True
            if i - 3 >= 0:
                north = True
            
            # check east
            if east:
                # true east
                if contents[i][j+1:j+4] == "MAS":
                    total += 1
                # north east
                if north:
                    if contents[i-1][j+1] + contents[i-2][j+2] + contents[i-3][j+3] == "MAS":
                        total += 1
                # south east
                if south:
                    if contents[i+1][j+1] + contents[i+2][j+2] + contents[i+3][j+3] == "MAS":
                        total += 1

            # check west
            if west:
                # true west
                if contents[i][j-3:j] == "SAM":
                    total += 1
                # north west
                if north:
                    if contents[i-3][j-3] + contents[i-2][j-2] + contents[i-1][j-1] == "SAM":
                        total += 1
                # south west
                if south:
                    if contents[i+3][j-3] + contents[i+2][j-2] + contents[i+1][j-1] == "SAM":
                        total += 1

            # check true north
            if north and contents[i-3][j] + contents[i-2][j] + contents[i-1][j] == "SAM":
                total += 1
            
            # check true south
            if south and contents[i+1][j]+ contents[i+2][j] + contents[i+3][j] == "MAS":
                total += 1

print(total)

total = 0

# iterate through possible answers only
for i in range(1, len(contents) - 1):
    for j in range(1, len(contents[i - 1])):
        
        # solution using sets
        if contents[i][j] == "A":
            if {"M", "S"} == {contents[i-1][j-1], contents[i+1][j+1]} == {contents[i-1][j+1], contents[i+1][j-1]}:
                total += 1 


print(total)
