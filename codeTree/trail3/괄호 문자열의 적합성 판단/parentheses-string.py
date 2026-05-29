str = input()

# Please write your code here.
stack = []

def main(str):
    for char in str:
        if char == '(':
            stack.append(char)
        else:
            if len(stack) == 0:
                return 'No'
            top = stack.pop()
            if top != '(':
                return 'No'

    if len(stack) > 0:
        return 'No'
        
    return 'Yes'

print(main(str))