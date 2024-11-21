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
a, b = input("곱셈할 두 수를 입력 하시오. 예) 5 4\n").split()
# split() 스페이스바 기준으로 두 개를 분리 시켜줌
print(int(a) * int(b))

print(f"{a} + {b} = {int(a)+int(b)}")
print(f"{a} - {b} = {int(a)-int(b)}")
print(f"{a} / {b} = {int(a)/int(b)}")
print(f"{a} * {b} = {int(a)*int(b)}")