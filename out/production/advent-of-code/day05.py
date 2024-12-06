instructions = []
updates = []

def sort_update(l):
    for i in range(len(l)):
            for j in range(i + 1, len(l)):
                if [l[j], l[i]] in instructions:
                    l[j], l[i] = l[i], l[j]

def parse(contents):
    for line in contents:
        if line == "\n":
            all_instructions_found = True
        elif all_instructions_found:
            updates.append(line.strip().split(","))
        else:
            instructions.append(line.strip().split("|"))

def main():    
    with open("inputs/day05.txt", "r") as file:
        contents = file.readlines()

    total_ordered = 0
    total_unordered = 0
    
    all_instructions_found = False

    # Parse input
    parse(contents)
            
    # Check if any pair violates instructions
    
    for update in updates:
        new = update.copy()
        sort_update(new)
        if update == new:
            total_ordered += int(update[len(update) // 2])
        else:
            total_unordered += int(new[len(new) // 2])

    print(total_ordered)
    print(total_unordered)

if __name__ == "__main__":
    main()