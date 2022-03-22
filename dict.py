
a = {'alice': [1,2,3], 'bob': 20, 'tony': 15}

print(a)
print(type(a))

for key, val in a.items():
    print("key:{}, value={}".format(key,val))

