def professor(k, a):
    student = 0
    n = len(a)
    for i in range(n):
        if a[i] <= 0:
            student += 1
        else:
            continue
    
    if student >= k:
        return 'NO'
    else:
        return 'YES'

if __name__ == "__main__":
    k = int(input())
    a = 0, -1, 2, 1
    print(professor(k, a))        