import re
import sys


def find_symbols(line, start, end):
    return re.search(r"[^\w\.]", line[start:end]) if line else None


def find_part_numbers(above, current, below):
    matched = []

    for match in re.finditer(r"\d+", current):
        start = 0 if match.start() == 0 else match.start() - 1
        end = len(current) if match.end() == len(current) else match.end() + 1

        adjacent = find_symbols(current, start, end)
        diagonal = find_symbols(above, start, end) or find_symbols(below, start, end)

        if adjacent or diagonal:
            matched.append(int(match.group()))

    return matched


def main():
    path = sys.argv[1]

    file = open(path, "r")

    part_numbers = []

    lines = file.readlines()

    for index, line in enumerate(lines):
        above = lines[index - 1] if index > 0 else None
        below = lines[index + 1] if index < len(lines) - 1 else None

        part_numbers.extend(find_part_numbers(above, line.strip(), below))

    file.close()

    print(sum(part_numbers))


if __name__ == "__main__":
    main()
