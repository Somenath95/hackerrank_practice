from collections import Counter

lst = [10,20,20,10,30,40,50,20,10,60,10,20]
ss , p = Counter(lst), 0
for s in ss: p += ss[s]//2
print(p) 