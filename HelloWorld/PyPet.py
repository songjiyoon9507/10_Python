print("Hello World")
print("안녕 파이펫~")

# name = "플루토"
# age = 5
# weight = 5
# photo = "(=^o.o^=)"

# print("My Pet Name : " + name)
# print(photo)

# 변수 이름은 겹치면 안됨
# 딕셔너리 : 키 , 값 (object)
cat = {
    "name" : "플루토",
    "age" : 5,
    "hungry" : True,
    "weight" : 5,
    "photo" : "(=^o.o^=)"
}

mouse = {
    "name" : "찍찍이",
    "age" : 3,
    "hungry" : True,
    "weight" : 1.5,
    "photo" : "<:3 )~~~"
}

# 먹이 주는 함수
def feed(pet) :
    if pet["hungry"] == True :
        pet["hungry"] = False
        pet["weight"] += 1
    else :
        print(pet["name"] + "는 이미 배가 불러요")

pets = [cat, mouse]

for pet in pets :
    print(pet)
    feed(pet)
    print(pet)
    feed(pet)
    print(pet)

# print("내 애완동물 이름 : " + cat["name"])
# print(cat["photo"])
# print(cat)
#
# feed(cat)
# print(cat)
# feed(cat)
# print(cat)
#
# x = 3
# if x > 5 :
#     print("x는 5보다 큽니다.")
# else :
#     print("x는 5보다 작습니다.")