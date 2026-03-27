import sys

def sys_input():
    return sys.stdin.readline().rstrip()

def solve(cases: list[int]):
    answers = []
    max_number = max(cases)

    zero = [0] * (max_number + 1)
    one = [0] * (max_number + 1)

    zero[0] = 1
    one[0] = 0

    if max_number >= 1:
        zero[1] = 0
        one[1] = 1

    for i in range(2, max_number + 1):
        zero[i] = zero[i-1] + zero[i-2]
        one[i] = one[i-1] + one[i-2]

    for case in cases:
        answers.append((zero[case], one[case]))
        
    return answers

def main():
    length =int(sys_input())
    cases = [int(sys_input()) for _ in range(length)]

    answers = solve(cases)

    for answer in answers:
        print(answer[0], answer[1])


if __name__ == "__main__":
    main()
