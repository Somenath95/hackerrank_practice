def race(k, height):
    max_height = height[0]
    n = len(height)
    for i in range(n):
        if(height[i] > max_height):
            max_height = height[i]
        else:
            continue
    if max_height - k <= 0:
        return 0
    else:
        return max_height-k    
if __name__ == "__main__":
    height=[1,6,3,15,2,10]
    k = 17
    print(race(k, height))