import sys

def sys_input():
    return int(sys.stdin.readline().rstrip())

def solve(inputs: list[int])-> tuple[int, int]:
    min = 100
    sum = 0

    for i, input in enumerate(inputs):
        if input % 2 == 1 :
            if input < min:
                min = input
            sum += input

    if sum == 0:
        return (-1, -1)
    
    return ( min, sum )
    
def main() -> None:
     nums = [sys_input() for _ in range(7)]
     min, sum = solve(nums)
     print(sum)

     if sum != -1: 
        print(min)

if __name__ == "__main__":
     main()
