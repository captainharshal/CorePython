def num(*num1):
    sum = 0
    for var in num1:
     if not isinstance(var, (int,float,complex)):
        raise TypeError ('ALL VALUES SHOULD BE NUMERIC')
     sum += var
    return sum


print(num(6,8))
print(num(6.8,5.4))
print(num(6,8,5.4,9j))
print(num(6,8,5.4,"Harry"))
