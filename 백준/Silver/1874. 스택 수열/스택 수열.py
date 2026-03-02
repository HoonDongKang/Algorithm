import sys
def sys_input() -> map:
    return sys.stdin.readline().rstrip()

def solve(inputs: list[int]) -> int:
    result = []
    stack = []
    index = 1

    for input in inputs:
        while index <= input:
            stack.append(index)
            result.append('+')
            index += 1
        if stack and stack[-1] == input:
            stack.pop()
            result.append('-')
        else:
            return 'NO'

    return result


def main() -> None:
    length = int(sys_input())
    inputs = [int(sys_input()) for _ in range(length)]
    answer = solve(inputs)

    if answer == 'NO':
        print(answer)
    else:
        [print(symbol) for _, symbol in enumerate(answer)]


if __name__ == "__main__":
    main()
