import sys
from collections import deque

def sys_input() -> map:
    return map(int, sys.stdin.readline().rstrip().split())

def solve(length: int, target: int) -> None:
    answer = []
    people = deque(range(1, length + 1))

    while people:
        people.rotate(-target + 1)
        answer.append(str(people.popleft()))

    return "<" + ", ".join(answer) + ">"


def main() -> None:
    length, target= sys_input()
    answer = solve(length, target)

    print(answer)


if __name__ == "__main__":
    main()
