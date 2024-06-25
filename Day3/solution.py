def getInput(input_path : str):
    with open(input_path) as f:
        input = f.readlines()
    return input


def solution_one(input):
    # Dictionary: letter:priority
    priorityRules = dict()
    priority = 1
    summaryOfPriorities = 0

    # Create dictionary that defines letter with they priorities.
    for x in range(ord('a'), ord('z')+1):
        priorityRules[chr(x)] = priority
        priority += 1
    for x in range(ord('A'), ord('Z')+1):
        priorityRules[chr(x)] = priority
        priority += 1

    for rucksack in input:
        firstCompartment = set(rucksack[:int(len(rucksack)/2)])
        secondCompartment = set(rucksack[int(len(rucksack)/2):])
        commonElement = (firstCompartment & secondCompartment).pop()
        summaryOfPriorities += priorityRules.get(commonElement)
        
    print(summaryOfPriorities)


def solution_two(input):
    # Dictionary: letter:priority
    priorityRules = dict()
    priority = 1
    summaryOfPriorities = 0

    # Create dictionary that defines letter with they priorities.
    for x in range(ord('a'), ord('z')+1):
        priorityRules[chr(x)] = priority
        priority += 1
    for x in range(ord('A'), ord('Z')+1):
        priorityRules[chr(x)] = priority
        priority += 1

    for x in range(0, len(input), 3):
        firstRucksack = set(input[x].strip())
        secondRucksack = set(input[x+1].strip())
        thirdRucksack = set(input[x+2].strip())
        commonElement = (firstRucksack & secondRucksack & thirdRucksack).pop()
        summaryOfPriorities += priorityRules.get(commonElement)

    print(summaryOfPriorities)        


def main():
    input = getInput("Day3\puzzle_input.txt")
    solution_one(input)
    solution_two(input)


if __name__ == "__main__":
    main()