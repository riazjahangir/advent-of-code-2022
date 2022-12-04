def get_elf_sections(assignment):
    # E.g. assignment is "2-4"
    start, end = assignment.split('-')
    return set(range(int(start), int(end) + 1))


def one_assignment_fully_contains_other(assignment_pair):
    first_elf, second_elf = assignment_pair.split(',')
    first_elf_sections = get_elf_sections(first_elf)
    second_elf_sections = get_elf_sections(second_elf)
    return (len(first_elf_sections.intersection(second_elf_sections)) in
            [len(first_elf_sections), len(second_elf_sections)])


def assignments_overlap(assignment_pair):
    first_elf, second_elf = assignment_pair.split(',')
    first_elf_sections = get_elf_sections(first_elf)
    second_elf_sections = get_elf_sections(second_elf)
    return first_elf_sections.intersection(second_elf_sections)


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(
        f'Part 1: {len([x for x in lines if one_assignment_fully_contains_other(x)])}')

    print(
        f'Part 2: {len([x for x in lines if assignments_overlap(x)])}')
