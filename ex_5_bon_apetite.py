def average(bill, k, b):
    dish = len(bill)
    cost = 0
    for i in range(dish):
        if(i == k):
            continue
        else:
            cost += bill[i]
    ret = (cost/2)
    if b == int(ret):
        return 'Bon Appetit'
    else:    
        return b-int(ret)

if __name__ == "__main__":
    bill = [3, 10, 2, 9]
    k = 1
    b = 12
    ret = average(bill, k, b)
    print(ret)