import sys
def sys_input() -> map:
    return sys.stdin.readline().rstrip()

def solve(inputs: list[int]) -> list[int]:
    stack = []
    result = []

    for i, input in enumerate(inputs):
        while stack and stack[-1][1] < input:
            stack.pop()

        if not stack:
            result.append(0)
        else:
            result.append(stack[-1][0] + 1)

        stack.append((i, input))

    return result
def main() -> None:
    length = int(sys_input())
    inputs = list(map(int, sys_input().split()))
    answer = solve(inputs)
    print(*answer)

if __name__ == "__main__":
    main()
