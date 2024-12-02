def solution_one():
    with open("inputs/day02.txt", "r") as file:
        contents = file.readlines()
    
    safe_reports = 0

    for line in contents:
        nums = line.split(" ")
        print(nums)
        if all([int(nums[i]) + 1 <= int(nums[i + 1]) <= int(nums[i]) + 3 for i in range(len(nums) - 1)]):
            safe_reports += 1
        elif all([int(nums[i]) - 1 >= int(nums[i + 1]) >= int(nums[i]) - 3 for i in range(len(nums) - 1)]):
            safe_reports += 1
    return safe_reports

def is_safe(nums, i, j, direction="undecided"):
    match direction:
        case "ascending":
            return nums[i] < nums[j] <= nums[i] + 3
        case "descending":
            return nums[i] > nums[j] >= nums[i] - 3
        case "undecided":
            if is_safe(nums, i, j, "ascending"):
                return "ascending"
            elif is_safe(nums, i, j, "descending"):
                return "descending"

    
def dampen_problem(nums, i, direction):
    if i > 2:
        if direction := is_safe(nums, i - 1, i+1, direction):
            return 0
        elif is_safe(nums, i, i+2, direction):
            return 1
    elif i == 0:
        if direction := is_safe(nums, i, i+2) == is_safe(nums, i+2, i+3):
            if direction in ["descending", "ascending"]:
                return 1, direction
        elif direction := is_safe(nums, i+1, i+3) == is_safe(nums, i+3, i+4):
            if direction in ["descending", "ascending"]:
                return 2, direction
            
        


def solution_two():
    with open("inputs/day02.txt", "r") as file:
        contents = file.readlines()
    
    safe_reports = 0

    for line in contents:
        nums = [int(n) for n in line.split()]

        safe = True
        tolerant = True
        direction = "undecided"
        i = 0

        while safe and i < len(nums) - 1:

            if is_safe(nums, i, i+1, direction):
                direction = "ascending"

            elif is_safe(nums, i, i+1, direction):
                direction = "descending"

            elif tolerant:
                if instruction := dampen_problem(nums, i, direction):
                    i += instruction[0]
                    if len(instruction) == 2:
                        direction = instruction[1]

                tolerant = False


            else: 
                safe = False

            i += 1
                    
        if safe:
            safe_reports += 1


           
        

    return safe_reports


    


if __name__ == "__main__":
    print(solution_two())