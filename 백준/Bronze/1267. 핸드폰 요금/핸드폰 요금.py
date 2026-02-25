import sys

def sys_input() -> str:
    return sys.stdin.readline()

def solve(times: list[int]) -> tuple[str, int]:
    y_fee = sum((t // 30 + 1) * 10 for t in times)
    m_fee = sum((t // 60 + 1) * 15 for t in times)

    if y_fee < m_fee:
        print("Y", y_fee)
    elif m_fee < y_fee:
        print("M", m_fee)
    else:
        print("Y M", y_fee)
    
def main() -> None:
    count = int(sys_input())
    times = list(map(int, sys_input().split()))
    solve(times)

if __name__ == "__main__":
    main()
