# 1. 전에 내가 쓴 코드는 간결하지 않고 또한 여러함수를 지정하였으며
# 2. n, r의 크기를 예외처리하여 다시입력하도록 만들지 않음
#factorial 이용
def fact(n) :
      if n == 0 :
            return 1
      else :
            return n * fact(n - 1)

def combi(n, r) :
      return fact(n) / (fact(r) * fact(n-r))

n =int(input("input first number:"))
r = int(input("input second number:"))
while n <r:
    print("다시입력해주세요")
    n =int(input("input first number:"))
    r = int(input("input second number:"))
print (combi(n, r))
