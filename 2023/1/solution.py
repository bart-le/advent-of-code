import re
import sys


def get_calibration_value(line):
    digits = re.findall(r"\d", line)

    return int(f"{digits[0]}{digits[-1]}")


def main():
    path = sys.argv[1]

    file = open(path, "r")

    calibration_values = [get_calibration_value(line) for line in file.readlines()]

    file.close()

    print(sum(calibration_values))


if __name__ == "__main__":
    main()
