def getInput(input_path : str):
    with open(input_path) as f:
        input = list(map(lambda s: s.strip('\n'), f.readlines()))
    return input


def solution_one(input):

    divider = input.index('')
    stackPositions = list()

    # Create the initial state of crates.
    for x in input[divider-1]:
        if str(x).isnumeric():
            xPos = input[divider-1].index(x)
            boxStack = list()

            for y in range(divider-1, 0-1, -1):
                if str(input[y][xPos]).isalpha():
                    boxStack.append(input[y][xPos])

            stackPositions.append(boxStack)

    # Get the moving instructions.
    for moves in input[divider+1:]:
        moves = [int(s) for s in moves.split() if s.isdigit()]
        
        # Move the crates.
        for i in range(moves[0]):
            stackPositions[moves[2]-1].append(stackPositions[moves[1]-1].pop())

    # Get the top crates.
    for top in stackPositions:
        print(top[-1], end='')
    print()


def solution_two(input):
    divider = input.index('')
    stackPositions = list()

    # Create the initial state of crates.
    for x in input[divider-1]:
        if str(x).isnumeric():
            xPos = input[divider-1].index(x)
            boxStack = list()

            for y in range(divider-1, 0-1, -1):
                if str(input[y][xPos]).isalpha():
                    boxStack.append(input[y][xPos])

            stackPositions.append(boxStack)

    # Get the moving instructions.
    for moves in input[divider+1:]:
        moves = [int(s) for s in moves.split() if s.isdigit()]
        
        # Get the numbers of caretes to be moved.
        numberOfCrates = len(stackPositions[moves[1]-1])-moves[0]

        # Move the crates.
        for i in range(moves[0]):
            stackPositions[moves[2]-1].append(stackPositions[moves[1]-1].pop(numberOfCrates))

    # Get the top crates.
    for top in stackPositions:
        print(top[-1], end='')
    print()


def main():
    # input = getInput("Day5\\test.txt")
    input = getInput("Day5\puzzle_input.txt")
    solution_one(input)
    solution_two(input)


if __name__ == "__main__":
    main()