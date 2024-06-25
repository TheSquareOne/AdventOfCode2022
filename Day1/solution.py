
def getInput(input_path : str):
    with open(input_path) as f:
        input = f.readlines()
    return input


def solution_one(input):
    mostCalories = 0
    sumOfCalories = 0

    for data in input:
        if data != '\n':
            sumOfCalories += int(data.rstrip())
        else:
            if sumOfCalories > mostCalories:
                mostCalories = sumOfCalories
            sumOfCalories = 0

    print(mostCalories)


def solution_two(input):
    threeMostCalories = [0, 0, 0]
    sumOfCalories = 0

    for data in input:
        if data != '\n':
            sumOfCalories += int(data.rstrip())
        else:
            if sumOfCalories > threeMostCalories[0]:
                threeMostCalories[0] = sumOfCalories
                threeMostCalories.sort()
            sumOfCalories = 0

    print(sum(threeMostCalories))


def main():
    input = getInput("puzzle_input.txt")
    solution_one(input)
    solution_two(input)


if __name__ == "__main__":
    main()