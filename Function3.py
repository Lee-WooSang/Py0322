# Function3.py

# 기본값을 주는 경우

def times(a=5, b=20):
    return a*b
#호출
print(times())
print(times(2))
print(times(2,3))

# 키워드인자(파라메터명을 지정)

def connectURI(server, port):
    strUrl = "http://" + server + ":" + port
    return strUrl

# 호출
print(connectURI("multicampus.com","80"))
print(connectURI(port="80", server="multicampus.com"))

# 가변인자 처리
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

# 호출    
print(union("HAM", "EGG"))
print(union("HAM", "EGG", "SPAM"))

# 정의되지 않은 인자(**, 내부에서 딕셔너리)
def userURIBuilder(server, port, **user):
    strURL = 'http://' + server + ":" + "/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
    return strURL

# 호출
print(userURIBuilder("multicampus.com","80",id="kim",passwd="1234"))
print(userURIBuilder("multicampus.com","80",id="kim",passwd="1234",age="30"))

# 람다함수(이름이 없는 간단한 함수 정의)

g = lambda x,y:x*y
print(g(3,4))
print(g(5,6))

print( (lambda x:x*x)(3))

print(globals())
