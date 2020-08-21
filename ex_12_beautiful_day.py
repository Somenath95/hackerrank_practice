def mirror_num(n):
    new_n = 0
    while n > 0:
        rem = n%10
        new_n = (new_n*10) + rem
        n = n//10
    return new_n

def beautifulDays(i, j, k):
    count = 0
    for day in range(i, j+1):
        if abs(day - mirror_num(day))%k == 0:
            count += 1
        else:
            continue
    return count        

if __name__ == "__main__":
    i = int(input())
    j = int(input())
    k = int(input())
    print(beautifulDays(i, j, k))