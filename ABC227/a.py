N, K, A = map(int, input().split())
#Nは人数、Kはカード総数、A人目から配り始める
s = K % N
n = A+s-1
if n == 0:
  n = 1
  print("{}".format(n))
elif n <= N:
  print("{}".format(n))
else:
  n = n % N
  print("{}".format(n))