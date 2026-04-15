import sys
sys.setrecursionlimit(10**6)

def sys_input():
    return sys.stdin.readline().rstrip()

def solve(n:int, num_list:list[int]):
    stack = []
    result = [-1] * n

    for i in range(n):
        while stack and num_list[stack[-1]] < num_list[i]:
            idx = stack.pop()
            result[idx] = num_list[i]

        stack.append(i)
    return result

def main():
    n = int(sys_input())
    num_list = list(map(int, sys_input().split()))

    answer = solve(n, num_list)
    print(*answer)

if __name__ == "__main__":
    main()
