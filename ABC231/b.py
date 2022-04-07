import collections
a = int(input())
b = [input() for i in range(a)]
c = collections.Counter(b)
m = c.most_common()[0]
print(m[0])

"""
from collections import Counter

n = int(input())
s = [input() for _ in range(n)]

cnt = Counter(s).most_common()

print(cnt[0][0])

"""