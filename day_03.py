from string import ascii_letters


def find_common_item(rucksack):
    assert len(rucksack) % 2 == 0
    middle = int(len(rucksack) / 2)
    first_compartment = set(rucksack[:middle])
    second_compartment = set(rucksack[middle:])
    common = first_compartment.intersection(second_compartment)
    assert len(common) == 1
    return common.pop()


def get_priority(item):
    return ascii_letters.index(item) + 1


def find_badge(rucksacks):
    assert len(rucksacks) == 3
    common = set(rucksacks[0]) & set(rucksacks[1]) & set(rucksacks[2])
    assert len(common) == 1
    return common.pop()


if __name__ == '__main__':
    with open('input.txt') as f:
        input = [line.strip() for line in f.readlines()]

    # Part 1
    print(sum([get_priority(find_common_item(rucksack))
          for rucksack in input]))

    # Part 2
    print(sum([get_priority(find_badge(input[i:i+3]))
          for i in range(0, len(input), 3)]))
