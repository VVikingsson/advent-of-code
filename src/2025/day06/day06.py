def parse_input():
    with open("src/2025/day06/input.txt", "r") as file:
        data = file.read().splitlines() # \n
        return data

def part1():
    data = parse_input()
    rows = [row.split() for row in data]

    total = 0

    for j in range(len(rows[0])):
        col_total = 0 if rows[-1][j] == "+" else 1
        for i in range(len(rows) - 1):
            if rows[-1][j] == "+":
                col_total += int(rows[i][j])
            else:
                col_total *= int(rows[i][j])
        total += col_total

    print("Total:", total)

def update_col_total(operator, col_total, curr_number):
    if not curr_number: 
        return col_total

    if operator == "+":
        col_total += int(curr_number)
    elif operator == "*":
        col_total *= int(curr_number)
    
    return col_total

def part2():
    rows = parse_input()
    operator = "+"
    col_total = 0
    total = 0

    for j in range(len(rows[0])):
        if rows[-1][j] == "+":
            operator = "+"
            print(col_total)
            total += col_total
            col_total = 0
        elif rows[-1][j] == "*":
            operator = "*"
            print(col_total)
            total += col_total
            col_total = 1

        curr_number = ""

        for i in range(len(rows) - 1):
            curr_number += rows[i][j] if rows[i][j].isnumeric() else ""

        col_total = update_col_total(operator, col_total, curr_number)

    
    if operator == "+":
        print(col_total)
        total += col_total
        col_total = 0
    elif operator == "*":
        print(col_total)
        total += col_total
        col_total = 1
        
    print("Cephalopod total:", total)



def main():
    part1()
    part2()

if __name__ == "__main__":
    main()