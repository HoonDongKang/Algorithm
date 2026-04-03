import sys
from collections import deque

def sys_input():
    return sys.stdin.readline().rstrip()

def findPrime(n: int):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if prime[i]:
            for j in range(i*i, n+1, i):
                prime[j] = False

    return prime


def solve(words:list[str]):
    word_count={}

    for word in words:
        if not word in word_count:
            word_count[word] = 0
        word_count[word] += 1

    return sorted(word_count, key=lambda x: (-word_count[x], -len(x), x))



def main():
    n, length = map(int, sys_input().split())
    words = [sys_input() for _ in range(n)]
    filter_words = [x for x in words if len(x) >= length]

    answers = solve(filter_words)
    for answer in answers:
        print(answer)


if __name__ == "__main__":
    main()
