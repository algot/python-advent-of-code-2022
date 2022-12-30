opponent_moves = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}
my_tips = {'X': 'Defeat', 'Y': 'Draw', 'Z': 'Win'}
shape_scores = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
outcomes = {'Defeat': 0, 'Draw': 3, 'Win': 6}


def get_inputs(filename: str) -> list:
    with open(filename, 'r', encoding='utf-8') as r:
        return r.read().splitlines()


def main():
    input_file = get_inputs('example.txt')
    total_score = 0

    for line in input_file:
        opponent_move, my_tip = line.split()
        opponent_move = opponent_moves[opponent_move]
        my_tip = my_tips[my_tip]

        if opponent_move == 'Rock':
            if my_tip == 'Draw':
                my_move = 'Rock'
            elif my_tip == 'Win':
                my_move = 'Paper'
            else:
                my_move = 'Scissors'
        elif opponent_move == 'Paper':
            if my_tip == 'Draw':
                my_move = 'Paper'
            elif my_tip == 'Win':
                my_move = 'Scissors'
            else:
                my_move = 'Rock'
        elif opponent_move == 'Scissors':
            if my_tip == 'Draw':
                my_move = 'Scissors'
            elif my_tip == 'Win':
                my_move = 'Rock'
            else:
                my_move = 'Paper'

        round_score = shape_scores[my_move] + outcomes[my_tip]
        total_score += round_score
        pass

    print(total_score)


if __name__ == '__main__':
    main()
