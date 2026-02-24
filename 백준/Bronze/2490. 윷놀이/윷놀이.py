import sys

def sys_input() -> list[int]:
    return list(map(int, sys.stdin.readline().split()))

def solve(inputs: list[int])-> str:
    game_info = { "front": 0, "back": 0 }
    for _, input in enumerate(inputs):
        if input == 0:
            game_info['front'] += 1
        else:
            game_info['back'] += 1

    if game_info['front'] == 1:
        return 'A'
    elif game_info['front'] == 2:
        return 'B'
    elif game_info['front'] == 3:
        return 'C'
    elif game_info['front'] == 4:
        return 'D'
    elif game_info['back'] == 4:
        return 'E'
    
    
def main() -> None:
    for _ in range(3):
        inputs = sys_input()
        if inputs:
            print(solve(inputs))

if __name__ == "__main__":
     main()
