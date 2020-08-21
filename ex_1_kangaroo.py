def kangaroo(x1, v1, x2, v2):
    k1_pos = x1
    k2_pos = x2

    count = 0

    while k1_pos != k2_pos:
        k1_pos += v1
        k2_pos += v2
        count += 1

        if k1_pos == k2_pos:
            return 'YES'
        elif count >= 10000 and k1_pos != k2_pos:
            return 'NO'


if __name__ == "__main__":
    x1 = int(input())
    v1 = int(input())
    x2 = int(input())
    v2 = int(input())

    print(kangaroo(x1,v1,x2,v2))

