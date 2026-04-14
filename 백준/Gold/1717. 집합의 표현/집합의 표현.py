import sys

def sys_input():
    return sys.stdin.readline().rstrip()

def solve(n:int, m:int, answers:list[int]):
    result = []
    parent = [i for i in range(n+1)]

    
    for answer in answers:
        s, a, b = answer
        parent_a = find(a, parent)
        parent_b = find(b, parent)
        if s == 0:
            parent[parent_b] = parent_a
        else:
            if parent_a == parent_b:
                result.append('YES')
            else:
                result.append('NO')
    return result

def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]
def main():
    n,m = map(int, sys_input().split())
    nums = [list(map(int,sys_input().split())) for _ in range(m)]

    answers = solve(n,m,nums)
    print("\n".join(answers))

if __name__ == "__main__":
    main()
