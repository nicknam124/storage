def solution(x):
    num = sum(int(y) for y in str(x))
    if x % num == 0:
        answer = True
    else:
        answer = False
    return answer