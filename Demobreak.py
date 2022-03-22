# Demobreak

lst = [1,2,3,4,5,6,7,8,9,10]

# for item in lst:
#     if item > 5:
#         break
#     print("item:{0}".format(item))


result = [item**2 for item in lst if item > 5]
print(result)

lst2=[]
for item in lst:
    if item > 5:
        lst2.append(item**2)
print(lst2)

colors = {100:"apple", 200:"banana", 300:"kiwi"}

print([v.upper() for v in colors.values()])