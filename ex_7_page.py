def pageCount(n, p):
    min_1 = p - 1
    min_2 = n - p
    if min_1 >= min_2:
        return min_2
    else:
        return min_1

if __name__ == "__main__":
    n = int(input())
    p = int(input())
    result = (pageCount(n, p))
    print(result)