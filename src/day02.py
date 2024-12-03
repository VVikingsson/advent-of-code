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
    if j < len(nums):
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
                else:
                    direction = None
        return direction

def solution_two():
    with open("test.txt", "r") as file:
    #with open("inputs/day02.txt", "r") as file:
        contents = file.readlines()
    
    safe_reports = 0

    for line in contents:
        nums = [int(n) for n in line.split()]

        safe = True
        tolerant = True
        direction = "undecided"
        directions = ["undecided", "ascending", "descending"]
        i = 0

        while safe and direction != None and i < len(nums) - 1:
            if is_safe(nums, i, i+1, direction):
                if i == 0:
                    direction = is_safe(nums, i, i+1, direction)
            elif tolerant:
                tolerant = False
                if i >= 2:
                    if len(nums) - 2 == i:
                        pass
                    elif is_safe(nums, i-1, i+1, direction) and is_safe(nums, i+1, i+2, direction):
                        pass
                    elif is_safe(nums, i, i+2, direction) and is_safe(nums, i+2, i+3, direction):
                        i += 1
                    else:
                        safe = False
                
                elif i == 1:
                    if is_safe(nums, i-1, i+1, "undecided"):
                        direction = is_safe(nums, i-1, i+1, "undecided")
                        if is_safe(nums, i+1, i+2, direction):
                            i += 1
                        elif is_safe(nums, i, i+2, "undecided"):
                            direction = is_safe(nums, i, i+2, "undecided")
                            i += 1
                        
                        
                    elif is_safe(nums, i, i+2, "undecided"):
                        direction = is_safe(nums, i, i+2, "undecided")
                        i += 1
                    else:
                        safe = False
                
                elif i == 0:
                    if is_safe(nums, i+1, i+2, "undecided"):
                        direction = is_safe(nums, i+1, i+2, "undecided")
                        i += 1
                    else:
                        safe = False
            else:
                safe = False
            i += 1
                    
        if safe:
            safe_reports += 1


           
        

    return safe_reports


    


if __name__ == "__main__":
    print(solution_two())