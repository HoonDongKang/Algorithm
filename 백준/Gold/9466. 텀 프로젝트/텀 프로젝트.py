import sys
sys.setrecursionlimit(10**6)

def sys_input() -> str:
    return sys.stdin.readline().rstrip()

def solve(students: list[int], student_count: int):
    count = 0
    visited = [False] * student_count
    finished = [False] * student_count

    for i in range(student_count):
        if visited[i]:
            continue
        
        stack = []
        
        while True:
            if not visited[i]:
                visited[i] = True
                stack.append(i)
                i = students[i]-1
                continue

            if not finished[i]:
                count += 1
                next = students[i]-1
                while next != i:
                    count += 1
                    next = students[next]-1

            for node in stack:
                finished[node] = True

            break
    return student_count - count
        
def main():
    answers = []
    length = int(sys_input())
    for _ in range(length):
        student_count = int(sys_input())
        students = list(map(int, sys_input().split()))
        answers.append(solve(students, student_count))

    for answer in answers:
        print(answer)

if __name__ == "__main__":
    main()
