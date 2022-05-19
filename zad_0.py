# Запись в файл словаря
# file_name = 'test.txt'
# my_dict = {
# 1: 'One',
# 2: 'Two'
# }
my_dict = {
1: 'One',
2: 'Two'
}

data = open('test.txt', 'w')
for i in my_dict:
    data.write(my_dict[i])
    data.write(' ') 
data.close()
# path = 'test.txt'               # указание полного пути файла с экранированием
path = r'C:\_moi\GB\Знакомство с языком Python\Семинары\Семинар 4\test.txt'  
with open(path, 'r') as data: # Когда используем with файл закрывать не нужно
    for line in data:
        print(line)

file = open('test.txt', 'r')    # считывание файла через метод .read ---> аналог строк 19-21
all_info = file.read()          # можно в скобках указать обьём считываемой информации 
print(all_info)
file.close()

file = open('test.txt', 'a')    # режим дозаписи в конце файла
file.write('NEW\n')           
file.close()

import pickle
path2 = 'test.txt'
with open('my_dict.pickle', 'wb') as f:
    pickle.dump(my_dict, f)
with open('my_dict.pickle', 'rb') as f:
    path = pickle.load(f)
print(path)