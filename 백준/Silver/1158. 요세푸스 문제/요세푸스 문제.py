import sys
def sys_input() -> map:
    return map(int, sys.stdin.readline().rstrip().split())

def solve(length: int, target: int) -> None:
    answer = []
    people = list(range(1, length + 1))
    idx = 0

    while people:
        idx = (idx + target - 1) % len(people)
        answer.append(str(people.pop(idx)))

    return "<" + ", ".join(answer) + ">"


def main() -> None:
    length, target= sys_input()
    answer = solve(length, target)

    print(answer)


if __name__ == "__main__":
    main()
