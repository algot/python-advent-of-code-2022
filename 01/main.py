def get_inputs(filename: str) -> list:
    with open(filename, 'r') as input_file:
        file_content = input_file.read().strip().split('\n')
        return file_content


def get_totals(inputs: list) -> list[int]:
    totals = []
    current_sum = 0
    for i in range(len(inputs)):
        if inputs[i] == '':
            totals.append(current_sum)
            current_sum = 0
        else:
            current_sum += int(inputs[i])
    return totals


def main():
    inputs = get_inputs('puzzle.txt')
    sums = get_totals(inputs)
    sorted_sums = sorted(sums)[-3:]

    print(max(sums))
    print(sorted_sums)
    print(sum(sorted_sums))


if __name__ == '__main__':
    main()
