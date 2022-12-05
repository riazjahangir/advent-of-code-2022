from parse import *

stacks = [
    'BVWTQNHD',
    'BWD',
    'CJWQST',
    'PTZNRJF',
    'TSMJVPG',
    'NTFWB',
    'NVHFQDLB',
    'RFPH',
    'HPNLBMSZ'
]


def move(num_crates, from_stack, to_stack):
    # Zero-index the indexes
    from_stack = from_stack - 1
    to_stack = to_stack - 1

    # Take crates off the from stack
    crates = stacks[from_stack][:num_crates]
    stacks[from_stack] = stacks[from_stack][num_crates:]

    # Reverse the order
    # (commented out for Part 2)
    # crates = crates[::-1]

    # Put crates on the to stack
    stacks[to_stack] = crates + stacks[to_stack]


if __name__ == '__main__':
    # Easier to hand-copy the intial stacks than to parse out,
    # so input.txt is just the moving instructions
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    instructions = [parse('move {:d} from {:d} to {:d}', line)
                    for line in lines]

    for i in instructions:
        move(*i)

    print(f'Top crates: {"".join([s[0] for s in stacks])}')
