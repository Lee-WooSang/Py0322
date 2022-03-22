# Function2.py

wordlist = ["J", "A", "M"]

def change(x):
    x[0] = "H"


change(wordlist)

print(wordlist)


print("---약간 수정----")

wordlist = ["J", "A", "M"]

def change(x):
    x1 = x[:]
    x1[0] = "H"
    print("함수 내부:",x1)

change(wordlist)

print(wordlist)

# 함수의 내부 이름 해석(LGB)
x = 1
def func1(a):
    return a+x

print(func1(1))

def func2(a):
    x = 2
    return a + x
    
print(func2(1))

# 전역변수
g = 1

def testScope(a):
    global g
    g += 1
    return a + g

print(testScope(1))
print(testScope(1))
print(testScope(1))
print("전역변수 g : ", g)

# 디버깅 연습2
def intersect(prelist, postlist):
    retList = []
    for x in prelist:
        if x in postlist and x not in retList:
            retList.append(x)
    return retList

print(intersect("HAM", "SPAM"))