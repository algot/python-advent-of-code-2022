import sys
import os


def get_inputs(filename: str) -> list:
    full_file_path = os.path.join(os.path.dirname(sys.argv[0]), filename)
    with open(full_file_path, 'r', encoding='utf-8') as r:
        return r.read().splitlines()


def main():
    inputs = get_inputs('example_part1.txt')[0]

    result_str = ''
    for i in range(len(inputs)):
        current_char = inputs[i]
        result_str += current_char

        if len(result_str) > 3:
            last_four = result_str[-4:]
            last_four_set = set(last_four)
            if len(last_four_set) == 4:
                return i + 1


if __name__ == '__main__':
    print(main())
