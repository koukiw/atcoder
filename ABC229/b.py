#A,B = map(int,input().split())
A, B = input().split()
a = list(A[::-1])
b = list(B[::-1])
#X, Y = A.zfill(20), B.zfill(20)
def judge():
  for x, y in zip(a, b):
    if int(x) + int(y) >= 10:
      return print("Hard")
  return print("Easy")

judge()