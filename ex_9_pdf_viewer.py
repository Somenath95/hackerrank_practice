def size(h, word):
    max_height = 0
    n = len(word)
    for i in range(n):
        v = ord(word[i]) - 97
        if (h[v] > max_height):
            max_height = h[v]
        else:
            max_height = max_height
    return max_height*n*1

if __name__ == "__main__":
    h = [1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]               
    word ='abc'
    print(size(h, word))