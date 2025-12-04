def parse_grid():
    grid = []
    with open("src/2025/day04/input.txt", "r") as file:
        for line in file.read().splitlines():
            grid.append(line)
    
    return grid


def count_accessible_paper_rolls(grid, new_grid):
    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "@":
                if is_accessible(i, j, grid):
                    new_grid[i][j] = "x"
                    count += 1

    return new_grid, count

def is_accessible(i, j, grid):
    row_start = i - int(i > 0)
    row_end = i + int(i < len(grid) - 1)
    col_start = j - int(j > 0)
    col_end = j + int(j < len(grid[i]) - 1)

    neighbors = 0
    for k in range(row_start, row_end+1):
        for l in range(col_start, col_end+1):
            if grid[k][l] == "@":
                neighbors += 1
            
            if neighbors >= 5:
                return False
    
    return True

def part1(grid):
    new_grid = [[x for x in grid[i]] for i in range(len(grid))]
    print(grid)
    print(new_grid)
    
    new_grid, count = count_accessible_paper_rolls(grid, new_grid)
    for row in new_grid:
        print("".join(row))

    print(count)

def remove_paper_rolls(grid):
    count = 0
    prev = -1

    while prev < count:
        prev = count
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "@":
                    if is_accessible(i, j, grid):
                        grid[i] = grid[i][:j] + "x" + grid[i][j + 1:]
                        count += 1

    return count

def part2(grid):
    print(remove_paper_rolls(grid))

def main():
    grid = parse_grid()
    part1(grid)
    part2(grid)

if __name__ == "__main__":
    main()