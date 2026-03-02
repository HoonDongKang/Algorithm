import sys
def sys_input() -> map:
    return sys.stdin.readline().rstrip()

def solve(inputs: list[int]) -> int:
    stack = []

    for input in inputs:
        if input == 0:
            stack.pop()
        else:
            stack.append(input)

    return sum(stack)


def main() -> None:
    length = int(sys_input())
    inputs = [int(sys_input()) for _ in range(length)]
    answer = solve(inputs)

    print(answer)


if __name__ == "__main__":
    main()
