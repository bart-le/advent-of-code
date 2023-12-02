import re
import sys


colours = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def game_possible(sets):
    for count, colour in re.findall(r"(\d+) (\w+)", sets):
        if int(count) > colours[colour]:
            return False

    return True


def main():
    path = sys.argv[1]

    file = open(path, "r")

    total = 0

    for index, line in enumerate(file.readlines(), 1):
        _, sets = line.strip().split(": ")

        if game_possible(sets):
            total += index

    file.close()

    print(total)


if __name__ == "__main__":
    main()
