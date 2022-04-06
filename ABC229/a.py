#a = [input() for i in range(2)]
a = input()+input()

t1 = ".##."
t2 = "#..#"

if a == t1 or a == t2:
  print("No")
else:
  print("Yes")