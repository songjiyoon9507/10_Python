# 천 미만의 자연수에서 2의 배수와 5의 배수의 총합을 구하라
total = 0

# for i in range(1, 1000) :
#     if i % 3 == 0 :
#         total += i
#     elif i % 5 == 0 :
#         total += i

for i in range(1, 1000) :
    if i % 3 == 0 or i % 5 == 0 :
        total += i

print(total)

# elif 사용하면 위에서 걸러지기 때문에 중복되는 숫자 자동으로 걸러짐

# 3의 배수이고, 5의 배수인 값의 합
andSum = 0

for i in range(1, 50) :
    if i % 3 == 0 and i % 5 == 0 :
        andSum += i

print(andSum)