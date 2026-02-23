import sys
    
def sys_input() -> int:
    return int(sys.stdin.readline().rstrip())

def solve() -> str:
    score = sys_input()
    grade = 'F'
    if 90 <= score and score <= 100:
        grade = 'A'
        
    if 80 <= score and score < 90:
        grade = 'B'

    if 70 <= score and score < 80:
        grade = 'C'
        
    if 60 <= score and score < 70:
        grade = 'D'
    return grade

def main() -> None:
    answer = solve()
    print(answer)
    
 
if __name__ == "__main__":
    main()