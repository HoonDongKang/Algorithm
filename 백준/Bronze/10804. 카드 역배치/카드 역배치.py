import sys

def sys_input() -> str:
    return map(int,sys.stdin.readline().split())

def solve(ranges: list[tuple[int, int]]) -> list[int]:
    cards = list(range(1, 21))
    for start, end in ranges:
        cards[start-1: end] = reversed(cards[start-1:end])
    return cards

def main() -> None:
    ranges = [(start, end) for start, end in (sys_input() for _ in range(10))]
    answer = solve(ranges)
    print(*answer)

if __name__ == "__main__":
    main()
