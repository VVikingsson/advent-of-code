from collections import defaultdict
def get_perimeter_value(garden, i, j):
    l = garden[i][j]
    perimeter = 4   
    perimeter -= (i - 1 >= 0 and garden[i-1][j] == l) 
    perimeter -= (i + 1 < len(garden) and garden[i+1][j] == l)
    perimeter -= (j - 1 >= 0 and garden[i][j-1] == l)
    perimeter -= (j + 1 < len(garden[i]) and garden[i][j+1] == l)
    return perimeter

def get_sides_no(region, total_perimeter, valued_cells):
    #print("BEFORE:", total_perimeter)
    leftmost = min([cell[1] for cell in valued_cells])
    rightmost = max([cell[1] for cell in valued_cells])
    upmost = min([cell[0] for cell in valued_cells])
    downmost = max([cell[0] for cell in valued_cells])
    sides = total_perimeter

    # Count down-facing surfaces
    covered = set()
    #print("DOWN_FACING")
    for i in range(downmost, upmost - 1, -1):
        checked = set()
        for cell in region:
            if cell in valued_cells:
                if cell[0] == i:
                    if cell not in covered:
                        for c in checked:
                            if c not in covered and abs(cell[1] - c[1]) == 1:
                                #print("Subtracting because cell", c, "is next to", cell)
                                sides -= 1

                        checked.add(cell)
            covered.add((cell[0] - 1, cell[1]))
            
    # Count up-facing surfaces
    covered = set()
    #print("UP_FACING")
    for i in range(upmost, downmost + 1):
        checked = set()
        for cell in region:
            if cell in valued_cells:
                if cell[0] == i:
                    if cell not in covered:
                        for c in checked:
                            if c not in covered and abs(cell[1] - c[1]) == 1:
                                #print("Subtracting because cell", c, "is next to", cell)
                                sides -= 1
                    
                        checked.add(cell)
            covered.add((cell[0] + 1, cell[1]))

    # Count right-facing surfaces
    covered = set()
    #print("RIGHT_FACING")
    for j in range(rightmost, leftmost -1, -1):
        checked = set()
        for cell in region:
            if cell in valued_cells:
                if cell[1] == j:
                    if cell not in covered:
                        for c in checked:
                            if c not in covered and abs(cell[0] - c[0]) == 1:
                                #print("Subtracting because cell", cell, "is next to", c)
                                sides -= 1
                        checked.add(cell)
            covered.add((cell[0], cell[1] - 1))

    # Count left-facing surfaces
    covered = set()
    #print("LEFT_FACING")
    for j in range(leftmost, rightmost + 1):
        checked = set()
        for cell in region:
            if cell in valued_cells:
                if cell[1] == j:
                    if cell not in covered:
                        for c in checked:
                            if c not in covered and abs(cell[0] - c[0]) == 1:
                                #print("Subtracting because cell", c, "is next to", cell)
                                sides -= 1
                        checked.add(cell)
            covered.add((cell[0], cell[1] + 1))

    #print("AFTER", sides)

    return sides



def is_part_of(list, i, j):
    if list == 0:
        return False
    for pair in list:
        a, b = pair
        if (a, b) == (i+1, j) or (a, b) == (i-1, j):
            return True
        elif (a, b) == (i, j+1) or (a, b) == (i, j-1):
            return True
    return False


with open("inputs/day12.txt", "r") as file:
    garden = [line.strip() for line in file.readlines()]

explored = defaultdict(list)

for i in range(len(garden)):
    for j in range(len(garden[i])):
        added = False
        letter = garden[i][j]

        for region in explored[letter]:
            
            if is_part_of(region, i, j):
                
                region.add((i, j))
                added = True

        if not added:
            
            explored[letter].append(set([(i, j)]))

# Ensure no duplicates
for letter, regions in explored.items():
    for region in regions:
        other_regions = regions.copy()
        other_regions.remove(region)
        for other_region in other_regions:
            if region.intersection(other_region) != set():
                region.update(other_region)
                regions.remove(other_region)


# Calculate result part 1
total = 0
total_discounted = 0

for letter, regions in explored.items():

    for region in regions:

        area = 0
        perimeter = 0
        valued_cells = set()
        for coords in region:
            
            area += 1
            value = get_perimeter_value(garden, coords[0], coords[1])
            if value > 0:
                valued_cells.add(coords)
            perimeter += value

        total += area * perimeter
        sides = get_sides_no(region, perimeter, valued_cells)
        total_discounted += area * sides
        print("letter", letter, area, "*", sides, "=", area*sides)

print(total)
print(total_discounted)




        

        
        