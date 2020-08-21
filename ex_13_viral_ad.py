import math

def advertising(n):
    like = 0
    share = 0
    cummulative = 0

    for day in range(1, n+1):
        if day==1:
            share = 5
            like = math.floor(share/2)
            cummulative += like

        else:
            share = like*3
            like = math.floor(share/2)
            cummulative += like

    return cummulative

if __name__ == "__main__":
    n = int(input())
    print(advertising(n))