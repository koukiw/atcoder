N, X = map(int,input().split())
A = list(map(int,input().split()))

flag = [False]*N

flag[X-1]=True
while not flag[A[X-1]-1]:
  flag[A[X-1]-1] = True
  X = A[X-1]
  
print(flag.count(True))