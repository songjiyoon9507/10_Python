import random

print(2+8)
print("안녕하세요", "Python")
# , 을 넣어서 출력하면 띄어쓰기로 출력됨
print("3*5=", 3*5)
print("안녕"), print("True"), print(True)
# print 사이를 ,로 나누면 줄바꿈 출력
print("""
이렇게 출력하면
줄바꿈도
알아서
됨
""")

# input 과 f-string 사용하기
# name = input("당신의 이름은 무엇인가요?")
# print("당신의 이름은 " + name + "입니다.")
# print(name + "님 반갑습니다.")
# input은 모두 문자열로 들어옴

# + 와 , 의 차이
# print(input("당신의 이름은 무엇인가요?") + "님 안녕하세요.")
# print(input("당신의 이름은 무엇인가요?"), "님 안녕하세요.")
# print("감사합니다")
# 아래에 작성하면 줄바꿈 출력

# int 이용하기
# print("농구공 1개 5000원")
# count = int(input("농구공이 몇 개 필요한가요?"))
# print("총 금액은", 5000*count, "원 입니다.")

# f-string
# print(f"총 금액은 {5000*count}원 입니다.")

# split() 과 이스케이프 시퀀스 - 사칙연산
# 이스케이프 시퀀스
# \n : 엔터키
# \t : tab키
# \\ : \
# a, b = input("두 수를 입력 하시오. 예) 5 4\n").split()
# split() 스페이스바 기준으로 두 개를 분리 시켜줌
# print(int(a) * int(b))

# print(f"{a} + {b} = {int(a)+int(b)}")
# print(f"{a} - {b} = {int(a)-int(b)}")
# print(f"{a} * {b} = {int(a)*int(b)}")
# print(f"{a} / {b} = {int(a)/int(b)}")
# print(f"{a} // {b} = {int(a)//int(b)}")
# print(f"{a} % {b} = {int(a)%int(b)}")
# print(f"{a} ** {b} = {int(a)**int(b)}")

# print("당신의 파이썬 공부 시간을 알려주세요")
# time = int(input("오늘의 파이썬 공부 시간은 몇 분 인가요?\n"))
# # a = 시간
# a = time // 60
# # b = 분
# b = time % 60
# print(f"당신의 총 공부 시간은 {a}시간 {b}분 입니다.")

# float 함수 사용 (원의 반지름이 정수일 수 있지만 실수일 수 있음)
# r = float(input("원의 반지름을 입력해주세요 : \n"))
# print(f"원의 넓이는 {r * r * 3.14}")
# print(f"원의 넓이(거듭제곱) {r**2 * 3.14}")
# 2의 7 제곱은 2**7

# round(a/b , 1) a 나누기 b 했을 때 결과값 소수 자리수 1자리까지 출력
# r = float(input("원의 반지름을 입력해주세요 : \n"))
# print(f"원의 넓이는 {r * r * 3.14}")
# print(f"원의 넓이(거듭제곱) {round(r**2 * 3.14, 2)}")

# su = int(input("숫자를 입력해주세요.\n"))
# if su % 2 == 0 :
#     print(su, "(은)는 짝수이다.")
# else :
#     print(su, "(은)는 홀수입니다.")

# 합격/불합격 코드
# pa = 80
# score = int(input("당신의 점수를 입력하세요\n"))
#
# if score >= pa :
#     print("합격입니다.")
# else :
#     print("불합격입니다.")

# random() : 0부터 1사이의 부동소수점(float)숫자를 리턴
print(random.random())

# randint(최소, 최대) : 최소부터 최대까지의 중 임의의 정수를 리턴
print(f"선택한 수는 : {random.randint(0, 5)} 입니다.")

# uniform(최소, 최대) : 최소에서 최대까지 중 임의의 부동소수점(float)숫자를 리턴
a = random.uniform(1.14, 36.5)
print(f"1.14와 36.5 사이의 선택한 수 : {a} 입니다.")

# randrange(시작, 끝, 간격) : 시작부터 끝까지 숫자 중에 지정된 간격의 숫자 중 리턴하고 간격 값은 선택 사항
b = random.randrange(5, 20)
print(f"5와 20 사이의 선택한 수 : {b} 입니다.")

# shuffle(컬렉션) : 컬렉션의 값을 뒤섞어서 리턴
c = ['apple', 'orange', 'book', 'cat', 'dog']
random.shuffle(c)
print(f"{c}")

# choice(컬렉션) : 컬렉션의 값 중 임의의 값을 리턴
print(f"{random.choice(c)}")

# choices(컬렉션, 가중치, 샘플 수) : 컬렉션 값에 가중치를 지정하고 임의의 값을 추출
d = random.choices([1, 2, 3, 4, 5], [10, 10, 20, 20, 15])
print(f"{d}")

# sample(컬렉션, 샘플 수) : 컬렉션 타입의 값 중에 지정한 샘플 수 만큼 랜덤으로 추출
e = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
f = random.sample(e, 3)
print(f"{f}")

lottoNum = random.sample(range(1, 45), 6)
print(lottoNum)

print("컴퓨터가 선택한 숫자를 맞춰보세요")
value = int(input("1부터 10까지 숫자 중 한개를 입력해주세요\n"))
computer = random.randint(1, 10)
if computer == value :
    print("맞았습니다.")
else :
    print(f"틀렸습니다. 컴퓨터가 선택한 숫자는 {computer} 입니다.")