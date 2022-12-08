from utils import get_input_lines

TEST_GRID = [
    [3, 0, 3, 7, 3],
    [2, 5, 5, 1, 2],
    [6, 5, 3, 3, 2],
    [3, 3, 5, 4, 9],
    [3, 5, 3, 9, 0],
]


def get_trees_visible_from_left(trees: list):
    # Set of 1D indices of visible trees
    visible_trees = {0}
    tallest_tree = trees[0]
    for i in range(1, len(trees)):
        if trees[i] > tallest_tree:
            visible_trees.add(i)
            tallest_tree = trees[i]
        if trees[i] == 9:
            # No more trees wil be visible from the left
            break

    return visible_trees


def get_visible_trees(grid):
    # Set of 2D (tuple) indices of visible trees in grid
    visible_trees = set()

    # Trees visible from left/right
    for row in range(len(grid)):
        left = get_trees_visible_from_left(grid[row])
        visible_trees.update([(row, i) for i in left])
        # Visible from the right is the same as visible
        # from the left for the reversed list of trees
        right = get_trees_visible_from_left(grid[row][::-1])
        visible_trees.update([(row, len(grid[row]) - i - 1) for i in right])

    # Trees visible from top/bottom
    for col in range(len(grid[0])):
        tree_column = [grid[row][col] for row in range(len(grid))]
        top = get_trees_visible_from_left(tree_column)
        visible_trees.update([(i, col) for i in top])
        # And reversed for bottoms-up
        bottom = get_trees_visible_from_left(tree_column[::-1])
        visible_trees.update([(len(grid) - i - 1, col) for i in bottom])

    return visible_trees


def get_trees_in_view_to_left(trees: list, from_index: int):
    # Leftmost tree can't see anything to its left
    if from_index == 0:
        return 0

    num = 0
    for i in range(from_index-1, -1, -1):
        num += 1
        if trees[i] >= trees[from_index]:
            break

    return num


def get_scenic_score(grid, from_row, from_col):
    # Trees in view to left
    left = get_trees_in_view_to_left(grid[from_row], from_col)
    # Reverse this for trees in view to right
    right = get_trees_in_view_to_left(
        grid[from_row][::-1], len(grid[from_row]) - from_col - 1)

    # Trees in view from top
    tree_column = [grid[row][from_col] for row in range(len(grid))]
    top = get_trees_in_view_to_left(tree_column, from_row)
    # Reverse this for trees in view to bottom
    bottom = get_trees_in_view_to_left(
        tree_column[::-1], len(grid) - from_row - 1)

    return left * right * top * bottom


def get_highest_scenic_score(grid):
    max_score = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            score = get_scenic_score(grid, row, col)
            if score > max_score:
                max_score = score
    return max_score


def make_grid():
    grid = []  # 99x99
    for line in get_input_lines(day=8):
        grid.append([int(digit) for digit in line])
    return grid


if __name__ == '__main__':
    # Part 1 Test
    # visible_trees = get_visible_trees(TEST_GRID)
    # print(sorted(list(visible_trees), key=lambda x: x[0] * 10 + x[1]))

    grid = make_grid()
    visible_trees = get_visible_trees(grid)
    print(f'Part 1: {len(visible_trees)}')

    # Part 2 Test
    # print(get_scenic_score(TEST_GRID, 1, 2))
    # print(get_scenic_score(TEST_GRID, 3, 2))
    print(f'Part 2: {get_highest_scenic_score(grid)}')
