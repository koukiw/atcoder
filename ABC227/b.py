N = int(input())
S = list(map(int, input().split()))
def calcu(a,b):
  answer = 4*a*b + 3*a + 3*b
  return answer
area = set() 
for i in range(1,142):
  for j in range(1,142):
    area.add(calcu(i,j))

n = 0
for s in S:
  if s in area:
    n+=1
print(N-n)
  