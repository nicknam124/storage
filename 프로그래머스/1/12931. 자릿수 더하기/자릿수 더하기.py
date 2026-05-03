def solution(n):
    answer = 0
    str_n = str(n)
    int_n = [int(i) for i in str_n]
    answer = sum(int_n)

    return answer