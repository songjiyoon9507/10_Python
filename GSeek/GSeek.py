import random
# import webbrowser

# random 모듈 import

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
# num = int(input())
#
# def gugudan(num) :
#     for i in range(1, 10) :
#         print(str(num) + " * " + str(i) + " = " + str(num*i))
#
# gugudan(num)

# 1부터 10까지 출력
num = 1
# while num <= 10 :
#     print(num)
#     num += 1

# 1부터 100까지 홀수만 출력
# while num <= 100 :
#     if num % 2 == 1 :
#         print(num)
#     num += 1

# while num <= 100 :
#     print(num)
#     num += 2

# 숫자를 입력 받아, 제곱을 출력
# 숫자가 0이 들어오면 종료
# x = 1
#
# while x != 0 :
#     x = int(input())
#     print(x*x)

# 컴퓨터 숫자 게임 만들기 (Up, Down)
# 내장 함수 (built in 함수)
# random 은 외장 함수 (모듈) -> import 해줘야함
ranNum = random.randrange(1, 11)
# (random range 준말) (1 ~ 100 사이 숫자 나옴 100은 포함 안됨 99까지 나옴)
print(ranNum)

# url = "www.gseek.kr"
# webbrowser.open(url)

# 유저에게 입력 받기

play = True

# while True :
#     inputNum = int(input())
#     if inputNum > ranNum :
#         print("Down")
#     elif inputNum < ranNum :
#         print("Up")
#     else :
#         print("정답입니다.")
#         break

# while play :
#     inputNum = int(input())
#     if inputNum > ranNum :
#         print("Down")
#     elif inputNum < ranNum :
#         print("Up")
#     else :
#         print("정답입니다.")
#         play = False

def say_hello() :
    print("헬로 파이썬")

say_hello()

# 함수는 재사용하기 위해서 만듦
# def sum(a, b) :
#     # print(a + b)
#     return a + b
inputA = int(input())
# inputB = int(input())

# print(sum(inputA, inputB))

# 두 개의 값을 받아서, 두 개의 값의 합과 곱을 출력하는 함수
# def mul(c, d) :
#     return c * d

# print(mul(inputA, inputB))

# 입력 값이 짝수인지 홀수인지 출력하는 함수
def is_odd(x) :
    if x % 2 == 0 :
        print("짝수입니다.")
    else :
        print("홀수입니다.")

is_odd(inputA)