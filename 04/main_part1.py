import sys
import os


def get_inputs(filename: str) -> list:
    full_file_path = os.path.join(os.path.dirname(sys.argv[0]), filename)
    with open(full_file_path, 'r', encoding='utf-8') as r:
        return r.read().splitlines()


def get_range_from_assignment(elf_assignment):
    first_elf_left_limit, first_elf_right_limit = elf_assignment.split('-')
    return range(int(first_elf_left_limit), int(first_elf_right_limit) + 1)


def check_if_range_inside_another(range1, range2):
    is_first_inside_second = range1.start in range2 and range1[-1] in range2
    is_second_inside_first = range2.start in range1 and range2[-1] in range1
    return is_first_inside_second or is_second_inside_first


def main():
    inputs = get_inputs('example_part1.txt')
    counter = 0
    for i in inputs:
        first_elf_assignment, second_elf_assignment = i.split(',')
        first_elf_range = get_range_from_assignment(first_elf_assignment)
        second_elf_range = get_range_from_assignment(second_elf_assignment)

        if check_if_range_inside_another(first_elf_range, second_elf_range):
            counter += 1

    print(counter)


if __name__ == '__main__':
    main()
