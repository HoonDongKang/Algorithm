import sys
sys.setrecursionlimit(10**6)

def sys_input() -> str:
    return sys.stdin.readline().rstrip()

def solve(lines: list[tuple[int,int]], computers: int):
    graph = [[] for _ in range(computers)]
        
    for i, j in lines:
        graph[i-1].append(j-1)
        graph[j-1].append(i-1)


    stack = [0]
    visited = [False] * computers
    visited[0] = True

    count = 0

    while stack:
        node = stack.pop()

        for next in graph[node]:
            if not visited[next]:
                visited[next] = True
                stack.append(next)
                count+= 1

    return count
        
def main():
    computers = int(sys_input())
    length = int(sys_input())
    lines = [tuple(map(int, sys_input().split())) for _ in range(length)]

    print(solve(lines, computers))

if __name__ == "__main__":
    main()
