#Словари
dictionary = {}
dictionary = \
 {
 'up': '↑',
 'left': '←',
 'down': '↓',
 'right': '→'
 }
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←
# типы ключей могут отличаться

for k in dictionary.keys():
    print(k)

for val in dictionary.values():
    print(val)