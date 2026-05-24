a, o, c = input().split()
a = int(a)
c = int(c)

def plus(a, b):
    return a + b

def sub(a, b):
    return a - b

def div(a, b):
    return a // b

def pro(a, b):
    return a * b

def result(a, o, b):
    if o == "+":
        return plus(a, b)
    if o == "-":
        return sub(a, b)
    if o == "/":
        return div(a, b)
    if o == "*":
        return pro(a, b)

if o not in ['+', '-', '*', '/']:
    print(False)
else:
    print(f"{a} {o} {c} = {result(a, o, c)}")