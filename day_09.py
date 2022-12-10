from utils import get_input_lines

import numpy as np


class Rope:

    MOVES = {
        'R': lambda pos: [pos[0] + 1, pos[1]],
        'L': lambda pos: [pos[0] - 1, pos[1]],
        'U': lambda pos: [pos[0], pos[1] + 1],
        'D': lambda pos: [pos[0], pos[1] - 1],
    }

    def __init__(self, knots=2) -> None:
        self.knot_pos = [[0, 0] for i in range(knots)]
        self.tail_moves = set()

    def simulate(self, motions):
        for motion in motions:
            dir, num = motion.split()
            steps = int(num)
            for i in range(steps):
                # Move head
                self.knot_pos[0] = self.MOVES[dir](self.knot_pos[0])
                # Move rest of rope
                for k in range(1, len(self.knot_pos)):
                    self.move_knot(k)
                self.tail_moves.add(tuple(self.knot_pos[-1]))

    def move_knot(self, index):
        this_knot = self.knot_pos[index]
        # Find vector from knot at index to knot in front of it
        vector = np.array(self.knot_pos[index-1]) - np.array(this_knot)
        # Only need to move knot if vector length > sqrt(2)
        # (if knot is not touching the knot in front of it)
        if (vector_length := np.linalg.norm(vector)) > 2**0.5:
            # If length is exactly 2, knot is directly up, down, left, or right from knot in front
            if vector_length == 2:
                # Move knot toward other knot
                # Normalize vector so knot moves only one unit
                normalized_vector = vector / vector_length
                # Move knot by normalized vector
                this_knot[0] += int(normalized_vector[0])
                this_knot[1] += int(normalized_vector[1])
            else:
                # Knot needs to move diagonally.
                x_motion = -1 if vector[0] < 0 else 1
                y_motion = -1 if vector[1] < 0 else 1
                this_knot[0] += x_motion
                this_knot[1] += y_motion


if __name__ == '__main__':
    input = get_input_lines(day=9)
    rope = Rope(10)
    rope.simulate(input)
    print(len(rope.tail_moves))
