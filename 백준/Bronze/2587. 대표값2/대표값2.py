import sys

def sys_input():
    return int(sys.stdin.readline().rstrip())

def solve(nums: list[int], length: int)-> tuple[int, int]:
    sorted_list = sorted(nums)
    total = sum(nums)
    avg = total // length  

    return ( avg, sorted_list[2] )
    
def main() -> None:
    length = 5
    nums = [sys_input() for _ in range(length)]
    avg, mid = solve(nums, length)
    print(avg)
    print(mid)

if __name__ == "__main__":
    main()
