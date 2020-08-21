def utopian(n):
    height = 1
    if n==0:
        return height
    else:    
        for i in range(1,n+1):
            if(i%2!=0):
                height *= 2
            else:
                height += 1
        return height

if __name__ == "__main__":
    n = int(input())
    print(utopian(n))