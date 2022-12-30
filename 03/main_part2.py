def get_inputs(filename: str) -> list:
    with open(filename, 'r', encoding='utf-8') as r:
        result = r.read().splitlines()

        step = 3
        split_list = []
        for i in range(0, len(result), step):
            x = i
            split_list.append(result[x:x + step])
        return split_list


def get_interceptions(lines):
    result = ''
    for line in lines:
        line_length = len(line)
        separator_index = line_length // 2
        left_part, right_part = line[:separator_index], line[separator_index:]
        interception = ''.join(set(left_part).intersection(right_part))
        result += interception

    return result


def count_priority(char):
    offset = 96 if char.islower() else 38
    return ord(char) - offset


def main():
    lines = get_inputs('example_part2.txt')
    interceptions = get_interceptions(lines)
    total = 0
    for i in interceptions:
        total += count_priority(i)

    print(total)


if __name__ == '__main__':
    main()
