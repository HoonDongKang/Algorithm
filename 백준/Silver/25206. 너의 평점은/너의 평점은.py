import sys

def sys_input():
    return sys.stdin.readline().rstrip()

def solve(scores: list[list[str]]) -> int:
    score_table = {
        "A+": 4.5, "A0": 4.0,
        "B+": 3.5, "B0": 3.0,
        "C+": 2.5, "C0": 2.0,
        "D+": 1.5, "D0": 1.0,
        "F": 0.0
    }
    totalN = 0
    sumN = 0

    for score in scores:
        subject, n, grade = score
        
        if grade =='P':
            continue
        
        totalN += float(n) * score_table[grade]
        sumN += float(n)

    return totalN / sumN


def main():
    scores = [sys_input().split() for _ in range(20)]
    answer = solve(scores)

    print(answer)


if __name__ == "__main__":
    main()
