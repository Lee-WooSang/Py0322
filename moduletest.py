def grade(point):
    if point <= 50:
        level = 'C'
    elif point <= 75:
        level = 'B'
    elif point <= 100:
        level = 'A'
    else:
        level = 'None'
        
    return level

print("40 : " + grade(40))
print("70 : " + grade(70))
print("90 : " + grade(90))
