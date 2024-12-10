import itertools

def is_producable(y, xs):
    
    # gets all applicable combinations of the + and * operators
    procedures = itertools.product("+*|", repeat = (len(xs) - 1))

    for procedure in procedures: 
        calculation = xs[0]

        for i in range(len(procedure)):
            if procedure[i] == "|":
                calculation = "(" * calculation.count(")") + calculation
                calculation = str(eval(calculation)) + xs[i+1]

            else:
                calculation += procedure[i] + xs[i + 1] + ")"
        

        calculation = "(" * calculation.count(")") + calculation

        if y == eval(calculation):
            return True
    
    return False


def main():
    with open("inputs/day07.txt", "r") as file:
        equations = file.readlines()

    total = 0

    for i in range(len(equations)):
        y, xs = equations[i].split(":")
        xs = xs.strip().split()
        y = int(y)

        print("Entering line", i + 1)
        if is_producable(y, xs):
            total += y

    print(total)

if __name__ == "__main__":
    main()