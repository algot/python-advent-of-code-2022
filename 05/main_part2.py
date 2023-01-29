import sys
import os


class Move:
    def __init__(self, number_of_crates_to_move: int, move_from: int, move_to: int):
        self.move_from = move_from - 1  # convert stack number to index
        self.move_to = move_to - 1      # convert stack number to index
        self.number_of_crates_to_move = number_of_crates_to_move


def get_inputs(filename: str) -> list:
    full_file_path = os.path.join(os.path.dirname(sys.argv[0]), filename)
    with open(full_file_path, 'r', encoding='utf-8') as r:
        return r.read().splitlines()


def get_stacks(input_list: list[str]) -> list[str]:
    delimiter_index = input_list.index('')
    stacks = input_list[:delimiter_index - 1]
    return stacks


def get_stack_indexes(input_list: list[str]) -> list[int]:
    delimiter_index = input_list.index('')
    stacks_numbers_string = input_list[delimiter_index - 1]
    stacks_indexes = [x for x, v in enumerate(stacks_numbers_string) if v.isnumeric()]
    return stacks_indexes


def get_instruction(input_list: list[str]) -> list[Move]:
    delimiter_index = input_list.index('')
    instructions = input_list[delimiter_index + 1:]

    result = []
    for r in instructions:
        params = [int(s) for s in r.split() if s.isdigit()]
        move = Move(*params)
        result.append(move)
    return result


def parse_stacks(str_stacks: list[str], stacks_indexes: list[int]) -> list[list[str]]:
    stacks = [[] for x in stacks_indexes]

    for string in str_stacks:
        for stack_index in range(len(stacks_indexes)):
            current_value = string[stacks_indexes[stack_index]]
            if current_value.isalpha():
                stacks[stack_index].insert(0, current_value)

    return stacks


def make_move(move: Move, stacks: list[list[str]]) -> list[list[str]]:
    stack_to_pop = stacks[move.move_from]
    index_to_pop = move.number_of_crates_to_move
    crates_to_move = stack_to_pop[-index_to_pop:]

    stacks[move.move_from] = stacks[move.move_from][:-index_to_pop]
    stacks[move.move_to] += crates_to_move
    return stacks


def perform_instructions(stacks: list[list[str]], instructions_parsed: list[Move]):
    stacks_state = stacks
    for move in instructions_parsed:
        stacks_state = make_move(move, stacks_state)

    result = [x.pop() for x in stacks_state]
    return ''.join(result)


def main():
    inputs = get_inputs('example_part2.txt')

    stacks = get_stacks(input_list=inputs)
    intructions = get_instruction(input_list=inputs)
    stacks_indexes = get_stack_indexes(input_list=inputs)
    stacks = parse_stacks(stacks, stacks_indexes)

    result = perform_instructions(stacks, intructions)

    print(result)


if __name__ == '__main__':
    main()
