import re

ip=input('введите ip/mask: ')

# Разделяем ip и prefix
string1=ip.split('/')

# Записываем в разные строки
string2=string1[0]
string3=string1[1]

#делаем строку
string4=str(string2)
string9=str(string3)

#Разделяем по точке
string5, str6, str7, str8=string4.split('.')

#Преобразовываем в строку
st5=str(string5)
st6=str(str6)
st7=str(str7)
st8=str(str8)

# Строки преобразовываем в числа
num1=int(st5)
num2=int(st6)
num3=int(st7)
num4=int(st8)






# делаем число из префикса
num5=int(string9)




# Считаем маску в двоичном формате, разбиваем на октеты
mask=('1'*num5 + (32-num5)*'0')

#Ищем первый 0 в маске
firstnull=mask.find('0')

#Делаем бинарый формат ip адреса по октетам
st5_bin=("{:08b}").format(num1)
st6_bin=("{:08b}").format(num2)
st7_bin=("{:08b}").format(num3)
st8_bin=("{:08b}").format(num4)

#Делаем бинарное число из адреса
ipb=st5_bin + st6_bin +st7_bin +st8_bin

#Ищем сетевую часть адреса
network=ipb[0:firstnull]
net=str(network)+(32-num5)*'0'

#разбираем на октеты
net_oct1=net[0:8]
net_oct2=net[8:16]
net_oct3=net[16:24]
net_oct4=net[24:32]

#Переводим октеты в десятичный формат
ten_net_oct1=int(net_oct1,2)
ten_net_oct2=int(net_oct2,2)
ten_net_oct3=int(net_oct3,2)
ten_net_oct4=int(net_oct4,2)

#Печатаем вывод сетевой части
print('Network:' + '\n')


#В десятичном формате
print("{:<8} {:<8} {:<8} {:<8}".format(ten_net_oct1, ten_net_oct2, ten_net_oct3, ten_net_oct4))

#в двоичном формате - столбцы по 8 символов, выравнивание слева
print("{:<8} {:<8} {:<8} {:<8}".format(net_oct1, net_oct2, net_oct3, net_oct4))


# Печатаем вывод маски сети
c
print('Mask:' + '\n')



#Разбиваем маску на октеты
oct1=mask[0:8]
oct2=mask[8:16]
oct3=mask[16:24]
oct4=mask[24:32]


# переводим октеты в двоичный формат
decoct1=int(oct1,2)
decoct2=int(oct2,2)
decoct3=int(oct3,2)
decoct4=int(oct4,2)

#Печатаем префикс
print(string3)

# Печатаем десятичные октеты
print("{:<8} {:<8} {:<8} {:<8}".format(decoct1, decoct2, decoct3, decoct4))

# печатаем двоичные октеты
print("{:<8} {:<8} {:<8} {:<8}".format(oct1, oct2, oct3, oct4))