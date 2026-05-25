N = int(input())

command = []
num = []

for _ in range(N):
    line = input().split()
    cmd = line[0]
    
    if cmd == 'push_back':
        target = int(line[1])
        num.append(target)
        # print(target) 
        
    elif cmd == 'get':
        target = int(line[1])
        print(num[target - 1])
        
    elif cmd == 'size':
        print(len(num))
        
    elif cmd == 'pop_back':
        if num:
            num.pop()