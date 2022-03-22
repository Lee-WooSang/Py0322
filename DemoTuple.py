# DemoTuple

a = {1, 2, 3, 3}
b = {3, 4, 4, 5}

print(a)
print(b)

print(a.union(b))
print(a.difference(b))

tp = (1, 2, 3)
print(tp)
print(len(tp))

# 함수를 정의
def calc(a,b):
    return a+b, a*b

print(calc(3,4))

args=(3,4)

print(calc(*args))



# 딕셔너리
color = {"apple" : "red", "banana" : "yellow"}
print(len(color))
print(type(color))
print(color["apple"])

# 반복구문
for item in color.items():
    print(item)

print("------------------")    
for k, v in color.items():
    print(k, v)
