def get_inputs(filename: str) -> list:
    with open(filename, 'r', encoding='utf-8') as r:
        result = r.read().splitlines()

        step = 3
        split_list = []
        for i in range(0, len(result), step):
            x = i
            split_list.append(result[x:x + step])
        return split_list


def get_badges(lines):
    result = []
    for line in lines:
        badge = (set(line[0]) & set(line[1]) & set(line[2])).pop()
        result.append(badge)
    return result


def count_priority(char):
    offset = 96 if char.islower() else 38
    return ord(char) - offset


def main():
    lines = get_inputs('example_part2.txt')
    badges = get_badges(lines)
    total = 0
    for i in badges:
        total += count_priority(i)

    print(total)


if __name__ == '__main__':
    main()
