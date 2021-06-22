#연습 1번
"""
for i in range(1,10):
    print(i)
"""
#연습 2번
"""
n = int(input(""))
if(n>=80):
    print("A")
elif(n<=20):
    print("F")
"""
#연습 3번
"""
i, sum = 0, 0
for i in range(10, 31): 
  sum = sum + i  
print("%d" % sum)
"""

#실습 1번 -> 과제 4번
"""
i, sum = 0, 0
for i in range(1, 101): 
  sum = sum + i
  if (sum >= 230):
    break
print(i, "까지 더했을 때 합 :", sum)
"""
#실습 2번    
"""                 
money = 3500
a = 500
b = 700
c = 400
x = money // a
y = money // b
z = money // c
for x in range(1, x+1):
    for y in range(1, y+1):
        for z in range(1, z+1):
            if((a*x) + (b*y) + (c*z) == money):
                print("빵 %d개" %x)
                print("초코칩 %d개" %y)
                print("피크닉 %d개 \n" %z)
                """
                
#실습 3번 -> 과제 5번

n = int(input("주민번호 뒷 자리 입력(7자리 숫자) : "))
b = str(n)
if(int(b[0])== 1 or int(b[0])== 3):
  print("Male")
elif(int(b[0])== 2 or int(b[0])== 4):
  print("Female")


#과제 1번

s = []
for i in range(1, 11):
  s.append(i)
print(s)

for i in range(1,11):
  s.remove(i)
print(s)

"""
#과제 2번
for i in range(1,101): 
  j = str(i) 
  if '3' in j: 
    print('짝',end=' ') 
  elif '6' in j:
    print('짝',end=' ') 
  elif '9' in j: 
    print('짝',end=' ') 
  elif i % 40 == 0:
    print('짜악', end=' ')
  else: 
    print(j,end=' ')
"""

#과제 3번
"""
num = 0
r = 0
while(r != 63):
  num = num + 1
  r = 3 * num / 2
print(num)
"""