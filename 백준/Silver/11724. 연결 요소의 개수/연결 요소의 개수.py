import sys

def sys_input() -> str:
    return sys.stdin.readline().rstrip()

def solve(lines: list[tuple[int,int]], length: int):
    graph = [[] for _ in range(length)]

    for i, j in lines:
        graph[i-1].append(j-1)
        graph[j-1].append(i-1)

    visited = [False] * length
    stack = []
    count = 0

    for i in range(length):
        if not visited[i]:
            stack.append(i)
            visited[i] = True

            while stack:
                node = stack.pop()

                for next in graph[node]:
                    if not visited[next]:
                        visited[next] = True
                        stack.append(next)

            count +=1

    return count

def main():
    n, m = map(int, sys_input().split())
    lines = [tuple(map(int, sys_input().split())) for _ in range(m)]

    print(solve(lines, n))

if __name__ == "__main__":
    main()
