import random


def makeset():
    sweet = list(range(101))
    ran = random.randint(1, 50)
    ransweet = random.randint(0, 100)
    ranli = random.sample(sweet, ran)
    ranli = sorted(ranli)
    f_line = [len(ranli), ransweet]
    return [f_line, ranli]


# 문제 시작
# makeset의 리턴값 [개수, 최소 달콤함 수치]
proset = makeset()
a = proset[0]
# [각 쿠키의 달콤함 수치]
b = proset[1]


# # 예시 (답은 2)
# a = [6, 7]
# b = [1, 2, 3, 9, 10, 12]

# # 다해도 못넘는 경우 (-1 이 출력되야하는 경우)
# a = [7,100]
# b = [1,2,3,4,5,6,7]
print(a, b)

# 달콤함 수치 = (1 * 가장 안 단 쿠키 + 2 * 두번째로 안 단 쿠키).

count = 0
solve = False
while solve == False:
    cookie = b.pop(0)
    if cookie < a[1]:
        if b == []:
            count = -1
            solve = True
        else:
            cookie = cookie + b.pop(0) * 2
            b.append(cookie)
            b.sort()
            count += 1
            print(a, b)
    else:
        solve = True


# 정답 적기
answer = count

print("정답은:", answer)
