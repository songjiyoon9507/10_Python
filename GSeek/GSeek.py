# print("너 이름이 뭐니?")
# name = input()
# print("너의 이름은 " + name + "이구나")

# 숫자 2개를 입력 받아서 출력하는 프로그램
# a = input()
# b = input()
# print(a + b)

# input()으로 받는 값은 문자열임 더하면 둘이 붙어 나옴
# 문자열을 숫자로 바꾸는 방법
# a = int(input())
# b = int(input())
# print(a + b)

# 숫자 3개를 입력 받아 그 곱을 출력하는 프로그램
# a = int(input())
# b = int(input())
# c = int(input())
# print(a * b * c)

# 만약에 내가 돈이 10000원 이상 있으면 택시, 아니면 버스
money = 15000
if money >= 10000 :
    print("택시")
else :
    print("버스")

# a와 b 중에 둘 중 큰 것 출력
a = 20
b = 20

if a > b :
    print(a)
else :
    print(b)

# a와 b 가 같을 때는 같다고 출력
# if a > b:
#     print(a)
# else:
#     if a == b :
#         print("두 수는 같습니다")
#     else :
#         print(b)

if a > b :
    print(a)
elif a < b :
    print(b)
else :
    print("두 개의 숫자는 같습니다.")

# 1부터 10까지 모두 출력
for i in range(1, 11) :
    print(i)

# 구구단 출력하기
for i in range(2, 10) :
    for j in range (1, 10) :
        print(str(i) + " * " + str(j) + " = " + str(i*j))

# 입력 받아서 그 단에 해당하는 구구단을 출력하는 함수를 작성하여라
num = int(input())

def gugudan(num) :
    for i in range(1, 10) :
        print(str(num) + " * " + str(i) + " = " + str(num*i))

gugudan(num)