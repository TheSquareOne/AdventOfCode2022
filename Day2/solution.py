def getInput(input_path : str):
    with open(input_path) as f:
        input = f.readlines()
    return input


def solution_one(input):
    score = 0
    for round in input:
        round = round.split()
        
        # A & X = Rock
        # B & Y = Paper
        # C & Z = Scissor
        if round[1] == 'X': score += 1
        elif round[1] == 'Y': score += 2
        elif round [1] == 'Z': score += 3
        else: print("Not Rock, Paper or Scissor")

        # Win:       Draw:       Lose:
        #   X & C        X & A       X & B
        #   Y & A        Y & B       Y & C
        #   Z & B        Z & C       Z & A
        if round[0] == 'C' and round[1] == 'X' or \
            round[0] == 'A' and round[1] == 'Y' or \
            round[0] == 'B' and round[1] == 'Z':
                score += 6

        elif round[0] == 'A' and round[1] == 'X' or \
            round[0] == 'B' and round[1] == 'Y' or \
            round[0] == 'C' and round[1] == 'Z':
                score += 3
        
    print(score)


def solution_two(input):
    score = 0
    for round in input:
        round = round.split()
        
        # X = Lose
        # Y = Draw
        # Z = Win
        if round[1] == 'Z': score += 6
        elif round[1] == 'Y': score += 3

        if round[1] == 'X' and round[0] == 'B' or \
            round[1] == 'Y' and round[0] == 'A' or \
            round[1] == 'Z' and round[0] == 'C':
                score += 1

        elif round[1] == 'X' and round[0] == 'C' or \
            round[1] == 'Y' and round[0] == 'B' or \
            round[1] == 'Z' and round[0] == 'A':
                score += 2

        elif round[1] == 'X' and round[0] == 'A' or \
            round[1] == 'Y' and round[0] == 'C' or \
            round[1] == 'Z' and round[0] == 'B':
                score += 3

    print(score)


def main():
    input = getInput("Day2\puzzle_input.txt")
    solution_one(input)
    solution_two(input)


if __name__ == "__main__":
    main()