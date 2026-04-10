import sys
sys.setrecursionlimit(10**6)

def sys_input():
    return sys.stdin.readline().rstrip()

def solve(n:int, meetings:list[tuple[int,int]]):
    sorted_meetings = sorted(meetings, key=lambda x: (x[1], x[0]))
    cnt = 0
    end_time = 0

    for i, meeting in enumerate(sorted_meetings):
        start, end = meeting
        
        if end_time <= start:
            cnt += 1
            end_time = end
        

    return cnt
def main():
    n = int(sys_input())
    meetings = [tuple(map(int,sys_input().split())) for _ in range(n)]

    answer = solve(n, meetings)
    print(answer)
if __name__ == "__main__":
    main()
