from utils import get_input_lines

import numpy as np


class Rope:

    MOVES = {
        'R': lambda pos: [pos[0] + 1, pos[1]],
        'L': lambda pos: [pos[0] - 1, pos[1]],
        'U': lambda pos: [pos[0], pos[1] + 1],
        'D': lambda pos: [pos[0], pos[1] - 1],
    }

    def __init__(self) -> None:
        self.head_pos = [0, 0]
        self.tail_pos = [0, 0]
        self.tail_moves = set()

    def simulate(self, motions):
        for motion in motions:
            dir, num = motion.split()
            steps = int(num)
            for i in range(steps):
                self.head_pos = self.MOVES[dir](self.head_pos)
                self.move_tail()
                self.tail_moves.add(tuple(self.tail_pos))

    def move_tail(self):
        # Find vector from tail to head
        vector = np.array(self.head_pos) - np.array(self.tail_pos)
        # Only need to move tail if vector length > sqrt(2) (if head and tail not touching)
        if (vector_length := np.linalg.norm(vector)) > 2**0.5:
            # If length is exactly 2, tail is directly up, down, left, or right from head
            if vector_length == 2:
                # Move tail toward head
                # Normalize vector so tail moves only one unit
                normalized_vector = vector / vector_length
                # Move tail by normalized vector
                self.tail_pos[0] += int(normalized_vector[0])
                self.tail_pos[1] += int(normalized_vector[1])
            else:
                # Tail needs to move diagonally.
                x_motion = -1 if vector[0] < 0 else 1
                y_motion = -1 if vector[1] < 0 else 1
                self.tail_pos[0] += x_motion
                self.tail_pos[1] += y_motion


if __name__ == '__main__':
    input = get_input_lines(day=9)
    rope = Rope()
    rope.simulate(input)
    print(len(rope.tail_moves))
