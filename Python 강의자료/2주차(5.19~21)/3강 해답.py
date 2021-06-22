#연습 1번
"""
def info():
    print("학번 : 201511839")
    print("학년 : 3학년")
    print("이름 : 이선우")
info()
"""

#연습 2번
"""
def odd_even():
    num = int(input(''))
    if(num % 2 ==0):
        print("짝수입니다")
    else:
        print("홀수입니다")
odd_even()
"""

#연습 3번 
"""
n = int(input(''))
m = str(n)
print(sorted(list(m)))
"""

#과제 1번 
"""
n = int(input(''))
m = str(n)
a = sorted(list(m))
a.reverse()
print(a)
"""

#과제 2번
#
"""
def maxnum():
    n = map(int, input('').split())
    m = list(n)
    print(max(m))
maxnum()
"""
"""
##
def maxnum():
    k = [] 
    for i in range(3): 
        n = int(input("정수 입력 : ")) 
        k.append(n) 
    print("최대값 =",max(k)) 
maxnum()
"""
###
def max():
    a = 5
    b = 8
    c = 7
    if a>b and b>c:
        print(a)
    elif b>c and c>a:
        print(b)
    elif c>b and b>a:
        print(c)
max()

"""
#과제 3번
import random
print(random.sample(range(1,1001), 5))

#과제 4번
import math
print(math.gcd(128,90)).
"""
