import sys
import os


def get_inputs(filename: str) -> list:
    full_file_path = os.path.join(os.path.dirname(sys.argv[0]), filename)
    with open(full_file_path, 'r', encoding='utf-8') as r:
        return r.read().splitlines()


def main():
    commands: list[str] = get_inputs('example_part1.txt')

    path = '/home'
    dirs = {'/home': 0}

    for command in commands:
        if command[0] == '$':
            if command[2:4] == 'ls':
                pass
            elif command[2:4] == 'cd':
                if command[5] == '/':
                    path = '/home'
                elif command[5:7] == '..':
                    path = path[:path.rfind('/')]

                else:
                    dir_name = command[5:]
                    path = path + '/' + dir_name
                    dirs.update({path: 0})
        elif command[:3] == 'dir':
            pass
        else:
            size = int(command[:command.find(' ')])
            dir = path
            for i in range(path.count('/')):
                dirs[dir] += size
                dir = dir[:dir.rfind('/')]

    total = 0

    for dir in dirs:
        if dirs[dir] <= 100000:
            total += dirs[dir]

    print(total)


if __name__ == '__main__':
    main()
