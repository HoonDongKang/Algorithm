import sys

def sys_input() -> str:
    return sys.stdin.readline().rstrip()

def solve(braces: str) -> int:
    stack = []
    result = 0
    calculate_number = 1
    prev_brace = ''

    for brace in braces:

        if brace == '(':
            stack.append(brace)
            calculate_number *= 2

        elif brace == '[':
            stack.append(brace)
            calculate_number *= 3

        elif brace == ')':
            if not stack or stack[-1] != '(':
                return 0
            
            if prev_brace == '(':
                result += calculate_number
            
            stack.pop()
            calculate_number //= 2

        elif brace == ']':
            if not stack or stack[-1] != '[':
                return 0
            
            if prev_brace == '[':
                result += calculate_number
            
            stack.pop()
            calculate_number //= 3

        prev_brace = brace

    return result if not stack else 0

def main() -> None:
    braces = sys_input()
    answer = solve(braces)
    print(answer)

if __name__ == "__main__":
    main()
