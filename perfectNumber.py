#変更の練習 v1.3

def perfectNumberList(n):
    res = ""
    for i in range(2,n+1):
        if validPerfectNumber(i):
            res += str(i) + "-"
    return res[:-1] if res != "" else "none"


def validPerfectNumber(n):
    sum = 1
    for i in range(2,n):
        if i*i > n:
            break
        if n % i == 0:
            sum += i
            sum += n/i
    return n == sum