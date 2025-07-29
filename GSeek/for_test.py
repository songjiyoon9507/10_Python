for i in range(1, 11) :
    print(i, end=' ')
print('')
moneys = {'이순신' : 100, '세종대왕' : 10000,'신사임당' : 50000}
for k, v in moneys.items() :
    print(k, v)

for k in moneys.keys() :
    print(k, moneys[k])

s = {1,1,1,2,2,2,3,3,3,4,4,4,5,5,5}
for i in s :
    print(i, end=' ')
print('')
t = (1,1,1,2,2,2,3,3,3,4,4,4,5,5,5)
for i in t :
    print(i, end=' ')
print('')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [n for n in numbers if n % 2 == 0]
print(result, '는 짝수입니다.')

num2 = [1, 2, 3, 4, 5]
result = [n * 10 for n in num2]
print(result)

for n in num2 :
    print(n * 10, end=' ')
print('')
fruits = ['apple', 'orange', 'mango']
upper_fruit = [f.upper() for f in fruits]
print(upper_fruit)

upper_fruit = []
for f in fruits :
    tmp = f.upper()
    upper_fruit.append(tmp)
print(upper_fruit)