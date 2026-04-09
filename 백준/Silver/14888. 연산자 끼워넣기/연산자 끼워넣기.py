import sys


def sys_input():
    return sys.stdin.readline().rstrip()


def solve(n:int, nums:list[int], operations: list[int]):
    max_val = -1_000_000_000
    min_val = 1_000_000_000

    def dfs(idx, cur):
        nonlocal max_val, min_val
        if idx == n:
            max_val = max(max_val, cur)
            min_val = min(min_val, cur)
            return 
        
        for i in range(4):
            if operations[i] <= 0:
                continue

            operations[i] -= 1
            
            if i == 0:
                dfs(idx + 1, cur + nums[idx])
            
            if i == 1:
                dfs(idx+1, cur - nums[idx])
        
            if i == 2:
                dfs(idx+1, cur * nums[idx])

            if i == 3:
                if cur < 0:
                    dfs(idx+1, -(abs(cur) // nums[idx]))
                else:
                    dfs(idx+1, cur // nums[idx])

            operations[i] += 1 

    dfs(1, nums[0])
    return max_val, min_val

def main():
    n =  int(sys_input())
    nums = list(map(int, sys_input().split()))
    operations = list(map(int, sys_input().split()))

    max_val, min_val = solve(n,nums, operations)
    print(max_val)
    print(min_val)

if __name__ == "__main__":
    main()
