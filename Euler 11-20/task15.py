def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print(int(fact(40) / (fact(20) * fact(20))))