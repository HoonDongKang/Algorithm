import sys


def sys_input():
    return sys.stdin.readline().rstrip()


def solve(input: str):
    result = 0
    parts = input.split("-")

    result = sum(map(int, parts[0].split("+")))

    for part in parts[1:]:
        nums = part.split("+")
        sum_nums = sum(map(int, nums))
        result -= sum_nums

    return result


def main():
    input = sys_input()
    answer = solve(input)
    print(answer)

if __name__ == "__main__":
    main()
