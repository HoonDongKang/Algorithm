import sys

def sys_input():
    return sys.stdin.readline().rstrip()

def solve(n:int, s:int, n_list:list[int]):
    left = 0 
    cur_sum = 0
    min_diff = float('inf')

    for right in range(n):
        cur_sum += n_list[right]
        while cur_sum >= s:
            min_diff = min(min_diff, right-left+1)
            cur_sum -= n_list[left]
            left += 1

    return 0 if min_diff == float('inf') else min_diff

def main():
    n,s = map(int, sys_input().split())
    n_list = list(map(int, sys_input().split()))

    answer = solve(n,s,n_list)
    print(answer)

if __name__ == "__main__":
    main()
