import heapq, sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# Please write your code here.
def main(arr, n):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(n)]

print(*(main(arr, n)))