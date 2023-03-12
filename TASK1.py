import re



london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1"
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2"
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True
    }
}
#Ждем ввода устройства
equipment1=input('enter equipment: ')
print('\n' + '-' * 30)

#Делаем все строчными буквами
equipment=equipment1.lower()

print('Имя устройства: ' + equipment)


# Составляем список ключей
key1= str(london_co[equipment].keys())

# Ищем ключи устройства, которое ввели
newdict=london_co[equipment]

#Ждем параметр, который надо найти
parametr1=input('enter parametr' +key1 + ': ')

#Делаем все строчными буквами
parametr=parametr1.lower()

#Ищем значение параметра в словаре
realparametr=newdict.get(parametr, 'Такого параметра нет')

#печатаем ответ
print(parametr + ': ' + realparametr)
