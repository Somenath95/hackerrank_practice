a = [1,2,3,4,5]
length = len(a)
lst = []

for i in range(length):
    sum = 0
    for j in range(length):
        if(i != j):
            sum = sum + a[j]
    lst.append(sum)
print(max(lst), min(lst))    
