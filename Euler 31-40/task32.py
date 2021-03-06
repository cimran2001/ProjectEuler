from time import time

def calculate():
    result = 0
    L = []

    for i in range(1, 10000):
        for j in range(1, i):
            x = str(i) + str(j) + str(i*j)
            if len(x) == 9 and len(set(x)) == 9 and '0' not in x and i * j not in L:
                result += i * j
                L.append(i*j)
            if len(x) > 9:
                break
    return result


start = time()
print(calculate())
print("Time {} s.".format(time() - start))