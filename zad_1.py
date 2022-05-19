# Задайте строку из набора чисел. 
# Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.
path = r'C:\_moi\GB\Знакомство с языком Python\Семинары\Семинар 4\test 2.txt'
with open(path, 'r') as data:
    list = data.read().split(' ') # можно не указывать разделителем пробел, в python он по умолчанию
print(list)   
for i in range(len(list)):
    list[i] = int(list[i])
print(list)
print(f'max {max(list)}; min {min(list)}')

