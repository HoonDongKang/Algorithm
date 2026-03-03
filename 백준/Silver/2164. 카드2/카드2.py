import sys
from collections import deque

def sys_input() -> str:
    return sys.stdin.readline().rstrip()

def solve(cards: int) -> int:
    cards_queue = deque()
    index = 0 

    for i in range(cards):
        cards_queue.append(i+1)

    while len(cards_queue) != 1:
        if index % 2 == 0:
            cards_queue.popleft()
        else:
            cards_queue.append(cards_queue.popleft())
        index += 1
    
    return cards_queue[0]


def main() -> None:
    cards = int(sys_input())
    card = solve(cards)
    print(card)

if __name__ == "__main__":
    main()
