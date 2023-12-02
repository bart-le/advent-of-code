import math
import re
import sys


def get_set_power(sets):
    colours = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    for count, colour in re.findall(r"(\d+) (\w+)", sets):
        if int(count) > colours[colour]:
            colours[colour] = int(count)

    return math.prod(colours.values())


def main():
    path = sys.argv[1]

    file = open(path, "r")

    total = 0

    for line in file.readlines():
        _, sets = line.strip().split(": ")

        total += get_set_power(sets)

    file.close()

    print(total)


if __name__ == "__main__":
    main()
