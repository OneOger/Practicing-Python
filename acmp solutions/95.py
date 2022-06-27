# acmp.ru
# 95


def rec(s, count=0):
    if len(s) == 1:
        return s, count
    else:
        sum = 0
        for i in s:
            sum += int(i)
        return rec(str(sum), count + 1)


s = input()
print(*rec(s))
