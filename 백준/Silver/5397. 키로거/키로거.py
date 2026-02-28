import sys

def sys_input() -> int:
    return sys.stdin.readline().rstrip()

def solve(inputs: list[str]) -> None:
    for input in inputs:
        left = []
        right = []

        for char in input:
            if char == '<':
                if left:
                    right.append(left.pop())
            elif char == '>':
                if right:
                    left.append(right.pop())
            elif char == '-':
                if left:
                    left.pop()
            else:
                left.append(char)

        print("".join(left + right[::-1]))

def main() -> None:
    input_count = int(sys_input())
    inputs = [sys_input() for _ in range(input_count)]

    solve(inputs)


if __name__ == "__main__":
    main()
