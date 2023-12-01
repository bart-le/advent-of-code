import re
import sys


spelled_digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_calibration_value(line):
    regex = "|".join([*spelled_digits.keys(), *spelled_digits.values()])

    digits = re.findall(rf"(?=({regex}))", line)

    mapped = [digit if digit.isdigit() else spelled_digits[digit] for digit in digits]

    return int(f"{mapped[0]}{mapped[-1]}")


def main():
    path = sys.argv[1]

    file = open(path, "r")

    calibration_values = [get_calibration_value(line) for line in file.readlines()]

    file.close()

    print(sum(calibration_values))


if __name__ == "__main__":
    main()
