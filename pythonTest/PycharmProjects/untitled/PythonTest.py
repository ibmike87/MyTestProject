import math

def printer (title,data):
    print("")
    print("입력 값 Type 형태 : ")
    print(type(title))
    print(type(data))
    if data == True :
        data = "True"
    else :
        data = "False"
    print(title + " : " + data)

#a = math.factorial(2)
b = math.cos(math.radians(180))
print(b)

c = 7 * -3
# print(c)

d = hex(255)
# print(d)
# print(type(d))


# 글자 찾기
str = "세종대왕의 한글창제"
result = "만" in str
title = "글자 찾기 결과"
printer(title,result)


# 문자열의 길이 구하기
title = "문자열 길이 구하기"
printer(title,len(str))



#리스트 초기화 함수
def initA():
    a = [1, 2, 3, 4, 5]
    return a

def initB():
    b = [3, 4, 5, 6, 7]
    return b



#리스트 연산 확인해보기
print("리스트 연산 확인해보기")
a = initA()
b = initB()
print(a+b)

#함수 메서드 동작 방식 확인해보기
print("extend 함수 동작 방식 확인해보기")
a = initA()
b = initB()
a.extend(b)
# ###a+b 와 a.extend(b)와 동일한 기능인듯 하다

print("insert 함수 동작 방식 확인해보기")
a = initA()
b = initB()
a.insert(2,9)
print(a)