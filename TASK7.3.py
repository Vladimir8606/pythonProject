import re



e=[]
flag=False
flag_vlan=False
file='C:\\python\\CAM_table.txt'
file_out1='C:\\python\\file_out1.txt'

# Проверяем что vlan введен корректно
while not flag_vlan:
    vlan = input('Введите номер vlan: ')
    if vlan.isdigit():
        flag_vlan=True
    else:
        print('Vlan может состоять только из цифр')
#Переводим lan в цифру
vlan_num=int(vlan)

#Читаем файл, ищем строки с mac и записываем в файл
with open(file) as src:
    for lines in src:
        list1=lines.split()
        try:
            string1=str(list1[1]).strip()
            if string1[4]=='.' and string1[9]=='.':
                with open(file_out1, 'a') as dest:
                    dest.writelines(lines.rstrip() + '\n')
        except:
            pass
    f=open(file_out1)
    a=f.readlines() #читаем файл построчно
    for num in a:
        split3=num.split() #Делаем список списков
        c=int(split3[0]) # Делаем первое значение числом
        d=split3[0] = c # Заменяем первое значение числом
        e.append(split3) # Делаем список, где вначале будут числа, а не строки
    sorted1=sorted(e) #сортируем список

    for test in sorted1:
        if test[0] == vlan_num:
            g=('{:<8}{:20}{:<15}'.format(test[0], test[1], test[3])) #печатаем результат
            print(g)
            flag=True
    if not flag:
        print('Такого vlan нет')

open(file_out1, 'w')

