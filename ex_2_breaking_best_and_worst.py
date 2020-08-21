def solution(scores):
    min_val = scores[0]
    max_val = scores[0]
    min_count = 0
    max_count = 0

    for i in range(len(scores)):
        if(scores[i] > max_val):
            max_val = scores[i]
            max_count += 1

        if(scores[i] < min_val):
            min_val = scores[i]
            min_count += 1

    return [max_count, min_count]

if __name__ == '__main__':
    scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
    x = solution(scores)
    print(x)