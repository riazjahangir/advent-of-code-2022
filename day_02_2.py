shapes = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors'
}


def get_score(round):
    opponent_shape = shapes[round[0]]
    outcome = round[1]
    order = ['rock', 'paper', 'scissors']
    outcome_scores = {
        'X': 0,
        'Y': 3,
        'Z': 6,
    }

    # Figure out shape I need to pick
    # X lose = i pick opponent shape - 1
    # Y draw = i pick opponent shape
    # Z win = i pick opponent shape + 1
    opponent_index = order.index(opponent_shape)
    if outcome == 'X':
        my_shape = order[opponent_index - 1]
    elif outcome == 'Y':
        my_shape = opponent_shape
    elif outcome == 'Z':
        my_shape = order[(opponent_index + 1) % 3]
    else:
        raise RuntimeError('bad letter')

    # Start score with shape I picked
    score = order.index(my_shape) + 1

    # Add outcome score
    score += outcome_scores[outcome]

    return score


if __name__ == '__main__':
    with open('input.txt') as f:
        input = f.readlines()

    score = 0
    for line in input:
        round_score = get_score(line.split())
        print(f'Round score: {round_score}')
        score += round_score

    print(f'Final score: {score}')
