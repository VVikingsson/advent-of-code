# This code is one big mess. I 8888888888888 ,m m m m m m m m m m m m m m m m 
# sorry my cat walked across the keyboard.
# This code is one big mess. I hereby promise myself not to create such a monstrosity again.

def solution_one():
    with open("inputs/day02.txt", "r") as file:
        contents = file.readlines()
    
    safe_reports = 0

    for line in contents:
        nums = line.split(" ")
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
    #with open("test.txt", "r") as file:
    with open("inputs/day02.txt", "r") as file:
        contents = file.readlines()
    
    safe_reports = 0

    for line in contents:
        nums = [int(n) for n in line.split()]

        if all([nums[i] + 1 <= nums[i + 1] <= nums[i] + 3 for i in range(len(nums) - 1)]):
            safe_reports += 1
        elif all([nums[i] - 1 >= nums[i + 1] >= nums[i] - 3 for i in range(len(nums) - 1)]):
            safe_reports += 1

        else:
            direction = "undecided"
            tolerant = True
            skip_i = []
            for i in range(len(nums) - 1):
                if i in skip_i:
                    continue

                elif is_safe(nums, i, i+1, direction):
                    continue
                    
                elif tolerant:
                    tolerant = False

                    if i == 0:
                        # try skipping i=1
                        if is_safe(nums, i, i+2, direction):
                            direction = is_safe(nums, i, i+2, direction)
                            if is_safe(nums, i+2, i+3):
                                skip_i.append(i+1)
                                skip_i.append(i+2)
                            # restart from i=1
                            else:
                                direction = "undecided"
                                continue
                    elif i == 1:
                        # try skipping i=0
                        if is_safe(nums, i, i+1, "undecided"):
                            direction = is_safe(nums,i,i+1, "undecided")
                        # try skipping i=1
                        elif is_safe(nums, i-1, i+1, "undecided"):
                            direction = is_safe(nums, i-1, i+1, "undecided")
                        # try skipping i=2
                        elif is_safe(nums, i, i+2, direction):
                            skip_i.append(i+1)

                    elif i == len(nums) - 2:
                        continue

                    elif i == len(nums) - 3:
                        # try skipping i
                        if is_safe(nums, i-1, i+1, direction):
                            continue
                        # try skipping i+1
                        elif is_safe(nums, i, i+2, direction):
                            skip_i.append(i+1)

                    else:
                        # try skipping i
                        if is_safe(nums, i-1, i+1, direction):
                            continue
                        # try skipping i+1
                        elif is_safe(nums, i, i+2, direction):
                            skip_i.append(i+1)

                else:
                    break

            else:
                safe_reports += 1
            
        


           
        

    return safe_reports


    


if __name__ == "__main__":
    print(solution_two())
    print(solution_one())