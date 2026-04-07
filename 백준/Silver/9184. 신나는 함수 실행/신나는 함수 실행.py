import sys

MEMO = {}

def sys_input():
    return sys.stdin.readline().rstrip()


def solve(a:int, b:int, c:int):
    if (a,b,c) in MEMO:
        return MEMO[(a,b,c)]
    
    if a<=0 or b<=0 or c<=0:
        MEMO[(a,b,c)] = 1
        return 1
    if a > 20 or b>20 or c>20:
        result = solve(20, 20, 20)
        MEMO[(a,b,c)] = result
        return result
    if a<b and b<c:
        MEMO[(a,b,c)]=solve(a,b,c-1) + solve(a,b-1,c-1) - solve(a,b-1,c)
    else:
        MEMO[(a,b,c)]=solve(a-1,b,c) + solve(a-1,b-1,c) + solve(a-1,b,c-1) - solve(a-1,b-1,c-1)

    return MEMO[(a,b,c)]
def main():
    while True:
        a,b,c = map(int, sys_input().split())
        if a == -1 and b == -1 and c == -1:
            break

        print(f"w({a}, {b}, {c}) = {solve(a, b, c)}")

if __name__ == "__main__":
    main()
