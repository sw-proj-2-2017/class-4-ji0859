def fac(n):
    factorial = 1
    a = int(n)
    for i in range(a, 0, -1):
        factorial *= i
    return factorial
