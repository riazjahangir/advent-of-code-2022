def get_shape(letter):
    if letter in 'AX':
        return 'rock'
    elif letter in 'BY':
        return 'paper'
    elif letter in 'CZ':
        return 'scissors'
    else:
        raise RuntimeError('bad letter')


def get_score(round):
    opponent_shape, my_shape = [get_shape(letter) for letter in round]
    order = ['rock', 'paper', 'scissors']
    # R R draw  0 0
    # R P win   0 1
    # R S lose  0 2
    # P R lose  1 0
    # P P draw  1 1
    # P S win   1 2
    # S R win   2 0
    # S P lose  2 1
    # S S draw  2 2
    #
    # => modulo math outcomes:
    #  them - me mod 3:
    #    0 = draw
    #    1 = lose
    #    2 = win
    outcome_scores = [3, 0, 6]

    # Start score with shape I picked
    score = order.index(my_shape) + 1

    # Add outcome score
    outcome = (order.index(opponent_shape) - order.index(my_shape)) % 3
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
