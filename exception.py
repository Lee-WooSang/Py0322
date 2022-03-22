
def average(list,end):
    return sum(list[:end+1])/(end+1)
    



list = [1,2,3,4,2]
end = -1

try:
    print(average(list,end))
except:
    print(end+1)

sum_list = sum(list[:len(list)])
#print(sum_list)

print("-------------------")
print(list.count(2))
for i in range(list.count(2)):
    print(list.index(2))
    del list[list.index(2)]

print("-----------------------")
list[0]=10
print(list)


print("튜플")

t = (1, "korea", 3.5, 1)
print(t)

