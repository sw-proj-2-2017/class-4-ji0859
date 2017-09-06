def fac(a):
    if a == 0:
        return 1
    return a * fac(a-1)

while True:
    n = int(input())
    if n == -1:
        break 
    else :
        print (fac(n)) 
