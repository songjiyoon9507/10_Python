'''
웹 사이트 게시판 폼을 작성 중인 A 게시물
총 건수와 한 페이지 당 탑재 가능한 게시물 수를
입력했을 때 총 페이지 수를 출력하라

페이징 (Paging)
- 게시판에 게시물이 n개 있을 때, 총 몇 페이지로
구성되는지를 계산 하는 것

페이징 예시
- 페이지당 최대 게시물 수 : 10개
- 게시물 수 : 15개
- 필요한 페이지 수는 ? 2페이지
'''

# 게시물 페이징
def getTotalPage(m, n) :
    # 몫 연산자
    if m % n != 0 :
        page = m // n + 1
    else :
        page = m // n
    return page

page = getTotalPage(5, 10)
print(page)