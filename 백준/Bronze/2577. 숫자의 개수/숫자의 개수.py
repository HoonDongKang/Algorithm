import sys

def sys_input() -> int:
    return int(sys.stdin.readline().rstrip())

def solve(numbers: list[int]) -> list[int]:
    number_counts = [0] * 10
    result =1
    for num in numbers:
        result *= num
    
    for str_num in str(result):
        number_counts[int(str_num)] +=1

    return number_counts

def main() -> None:
    numbers = [sys_input() for _ in range(3)]
    number_counts = solve(numbers)

    for num in number_counts:
        print(num)

if __name__ == "__main__":
    main()
