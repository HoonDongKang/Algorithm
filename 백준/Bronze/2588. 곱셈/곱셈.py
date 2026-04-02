import sys

def sys_input():
    return sys.stdin.readline().rstrip()

def solve(inputs:list[int]) -> list[int]:
    results = []
    numbers = []

    for input in str(inputs[1]):
        numbers.append(input)

    for number in numbers[::-1]:
        results.append(inputs[0] * int(number))

    results.append(inputs[0] *inputs[1])
    return results

def main():
    inputs = list(map(int, [sys_input() for _ in range(2)]))
    answers = solve(inputs)

    for answer in answers:
        print(answer)

if __name__ == "__main__":
    main()
