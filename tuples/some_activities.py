
t = ()
print(type(t)) # tuple
t = (1,)    #Если хотите кортеж из одного числа
            #  ОБЯЗАТЕЛЬНО СТАВЬТЕ ЗАПЯТУЮ ПОСЛЕ ЧИСЛА
print(type(t)) # tuple
t = (1)
print(type(t)) # int
t = (28, 9, 1990)
print(type(t)) # tuple
colors = ['red', 'green', 'blue'] #Это список
print(colors) # ['red', 'green', 'blue']
t = tuple(colors) #Конвертация списка в кортеж
print(t) # ('red', 'green', 'blue')