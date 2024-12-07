import itertools

def is_producable(y, xs):
    
    procedures = itertools.permutations(("+" * (len(xs) - 1) + "*" * (len(xs) - 1)), len(xs) - 1)
    calculation = ""


    print(procedure)
    #for procedure in procedures:
    #    for i in range(len(xs) - 1):
     #       calculation += xs[i] + procedure[i]
#
 #       calculation += xs[-1]
#
 #       print(calculation)
  #      print("--------------------------------------------------------")

def main():
    with open("inputs/day07.txt", "r") as file:
        equations = file.readlines()

    total = 0

    for equation in equations:
        y, xs = equation.split(":")
        xs = xs.strip().split()
        y = int(y)

        if is_producable(y, xs):
            total += 1

    print(total)

if __name__ == "__main__":
    main()