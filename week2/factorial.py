def fac(a):
    if a == 0:
        return 1
    return a * fac(a-1)

while True:
    n = str(input())
    if int(n) < 0:
        if n == -1 :
            break
        print ("양의 정수를 입력하시오")
    elif type(n) == float:
        print ("정수를 입력하시오")
    else :
        print (fac(int(n))) 
