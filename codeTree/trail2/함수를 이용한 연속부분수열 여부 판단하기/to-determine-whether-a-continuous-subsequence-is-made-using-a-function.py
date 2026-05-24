n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
def is_aa(a,b):
    for start in range(len(a) - len(b) + 1):
        same = True

        for b_idx in range(len(b)):
            if a[start+b_idx] != b[b_idx]:
                same = False
                break
            
        if same:
                return 'Yes'

    return 'No'

print(is_aa(a,b))