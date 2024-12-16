# for문
for i in range(5):
    print(i)
print("=======================")

for i in range(5):
    print(i, end=' ')
print("\n=======================")

# for문 사용해서 구구단 출력하기
a = 2

for i in range(1,10) :
    print(f"{a}*{i}={a*i}")

# while 문으로 구구단 2단부터 9단까지 출력하기
a = 2
while a < 10 :
    for i in range(1, 10) :
        print(f"{a}*{i}={a*i}")
    a += 1

# 단 입력 받아서 출력
# su = int(input("몇 단을 출력할까요?"))
# i = 1
# while i < 10 :
#     print(f"{su}*{i}={su*i}")
#     i += 1

# 리스트 사용 예
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for item in a :
    if item % 2 == 0 :
        print("짝수 출력 :", item)

for i in range(100) :
    print(i)
    if i == 10 :
        print("정지")
        break