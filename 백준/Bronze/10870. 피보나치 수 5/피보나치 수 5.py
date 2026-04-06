import sys

def sys_input():
    return sys.stdin.readline().rstrip()

def solve(n: int):
    if n <= 1:
        return n
    return solve(n-1) + solve(n-2)        
    
def main():
    n = int(sys_input())

    answer = solve(n)
    print(answer)

if __name__ == "__main__":
    main()
