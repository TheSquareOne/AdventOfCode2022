def getInput(input_path : str):
    with open(input_path) as f:
        input = f.readlines()
    return input


def solution_one(input):
    count = 0
    for pair in input:
        elf_1, elf_2 = pair.rstrip().split(',')
        elf_1 = list(map(int, elf_1.split('-')))
        elf_2 = list(map(int, elf_2.split('-')))

        if(elf_1[0] <= elf_2[0] and elf_1[1] >= elf_2[1] or 
            elf_1[0] >= elf_2[0] and elf_1[1] <= elf_2[1]):
            count += 1

    print(count)


def solution_two(input):
    count = 0
    for pair in input:
        elf_1, elf_2 = pair.rstrip().split(',')
        elf_1 = list(map(int, elf_1.split('-')))
        elf_2 = list(map(int, elf_2.split('-')))

        if(elf_1[0] >= elf_2[0] and elf_1[0] <= elf_2[1] or
            elf_1[1] >= elf_2[0] and elf_1[1] <= elf_2[1] or
            elf_1[0] >= elf_2[0] and elf_1[1] <= elf_2[1] or
            elf_1[0] <= elf_2[0] and elf_1[1] >= elf_2[1]):
            count += 1

    print(count)


def main():
#    input = getInput("Day4\\test.txt")
    input = getInput("Day4\puzzle_input.txt")
    solution_one(input)
    solution_two(input)


if __name__ == "__main__":
    main()