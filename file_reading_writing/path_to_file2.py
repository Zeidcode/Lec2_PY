path = 'file2.txt'
data = open(path, 'r')
for color in data:
    print(color)
data.close()
exit()