# lst = (2,3,5,4,6)
# runner_up = []

# for num in lst:
#     if (num == max(lst)):
#         continue
#     else: 
#         runner_up.append(num)

# print(max(runner_up))        
raw_input()
i = int(input())
lis = list(map(int,raw_input().strip().split()))[:i]
z = max(lis)
while max(lis) == z:
    lis.remove(max(lis))

print (max(lis))