S = int(input())
 
if S < 42:
  if S < 10:
    S = "0"+str(S)
  else:
  	S = str(S)
else:
  S = S+1
  S = str(S)
  
print("AGC0{}".format(S))


#zfill(3)で文字列を右よせで3桁の余白にはゼロを埋めることができる