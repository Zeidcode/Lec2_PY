def concatenatio (*param):
    res: str = ""
    for item in param:
        res += item
    return res

print(concatenatio('a','b','c')) #abc
print(concatenatio('a', '1')) #a1
# print(concatenatio(1,2,3,4)) #TypeError : .....