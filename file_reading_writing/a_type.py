colors = ['red', 'black', 'green']
data = open('file.txt', 'a')
data.writelines(colors)
data.close()