import sys

def sys_input():
    return sys.stdin.readline().rstrip()

def solve(n: int) -> list[str]:
    length = 2 * n - 1
    mid = length // 2
    result = []
    
    for i in range(mid):
        blank = mid - i
        star = length - blank * 2
        result.append(" " * blank + "*" * star)

    result.append('*' * length)
    result += list(reversed(result[:-1]))

    return result
    

def main():
    n = int(sys_input())
    answers = solve(n)

    print("\n".join(answers))


if __name__ == "__main__":
    main()
