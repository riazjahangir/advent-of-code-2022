from utils import get_input_lines


class Program:

    def __init__(self, instructions) -> None:
        self.X = 1
        self.cycle = 1
        self.instructions = instructions
        self.history = {1: 1}
        self.display = ''

    def step(self):
        draw_pos = self.cycle - 1
        self.display += '#' if draw_pos % 40 in (
            self.X-1, self.X, self.X+1) else '.'

        if self.cycle % 40 == 0:
            self.display += '\n'

        self.history[self.cycle] = self.X
        self.cycle += 1

    def run(self):
        for instruction in self.instructions:
            if instruction == 'noop':
                self.step()
            else:
                addend = int(instruction.split()[1])
                self.step()
                self.step()
                self.X += addend

    def get_signal_strength(self, cycle):
        return cycle * self.history[cycle]


if __name__ == '__main__':
    input = get_input_lines(day=10)
    p = Program(input)
    p.run()

    print('Part 1: '
          f'{sum(p.get_signal_strength(x)for x in [20, 60, 100, 140, 180, 220])}')

    print(f'Part 2:\n{p.display}')
