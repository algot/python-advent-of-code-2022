import sys
import os


def get_inputs(filename: str) -> list:
    full_file_path = os.path.join(os.path.dirname(sys.argv[0]), filename)
    with open(full_file_path, 'r', encoding='utf-8') as r:
        return r.read().splitlines()


def main():
    inputs = get_inputs('example_part2.txt')[0]
    shift = 14

    for i in range(len(inputs)):
        if len(set(inputs[i:i + shift])) == shift:
            return (i + shift)


if __name__ == '__main__':
    print(main())
