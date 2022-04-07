from bisect import bisect_left

N, Q = map(int,input().split())
A = list(map(int,input().split()))
A_sort = sorted(A)

x = [int(input()) for i in range(Q)]
for i in range(Q):
  count = bisect_left(A_sort,x[i])
  print(N-count)


"""
from bisect import bisect_left

n, q = map(int, input().split())
a = sorted(list(map(int, input().split())))

for _ in range(q):
    t = bisect_left(a, int(input()))
    print(n - t)
"""