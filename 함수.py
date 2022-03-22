def add(a=1,b=2):
    result = a+b
    return result

#a = int(input("a:"))
#b = int(input("b:"))

#gab = add()
#print(gab)


def test(a,b,*args):
    result2 = 0
    i = 0

    print(type(args))
    for i in range(i,len(args)):
        result2 += int(args[i])
        print(args[i])
        
    return result2


print(test(1,2,5,6))



def spam(eggs):
    eggs.append(1)
    eggs=[2,3]
    print(type(eggs))
    return eggs
    
ham = [0]
spam(ham)
print(ham)
print(spam(ham))
