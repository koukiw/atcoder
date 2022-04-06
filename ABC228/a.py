S = list(map(int,input().split()))
#S[2] = S[2]+0.5
if S[0] < S[1]:
  if S[0] <= S[2] < S[1]:
    print("Yes")
  else:
    print("No")
else:
  if S[0]<=S[2]<24 or 0<=S[2]<S[1]:
    print("Yes")
  else:
    print("No")
"""
S, T, X = map(int, input().split())

if S < T:  # 日付が変わらない場合
    print("Yes" if S <= X < T else "No")  # T時30分に電気は消えていますから、Tは含みません
else:  # 日付が変わる場合
    print("Yes" if X < T or S <= X else "No")
"""