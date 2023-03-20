config_filename1='C:\\python\\config_sw2.txt'
result_access={}

result={}


ignore = ["duplex", "alias", "Current configuration"]


def ignore_command(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    """
    ignore_status = False
    for word in ignore:
        if word in command:
            ignore_status = True
    return ignore_status



def get_int_vlan_map(config_filename):
    file=open(config_filename, 'r')
    a=file.read()
    b = a.split('!') #Разделяем куски конфига по !
    key = ()
    for line in b: #Читаем куски построчно
        list1=line.split('\n') #Разделяем их по строкам, добавляя в список
        value = []
        #print(list1)
        for string1 in list1: # перебираем объекты в списке ['', 'interface FastEthernet0/2', ' switchport mode access', ' switchport access vlan 20', ' duplex auto', '']

            if string1.strip():
                if not ignore_command(string1, ignore):
                    if not string1.startswith(' '):
                        key=string1
                    else:
                        if string1:
                        #print(string1)
                            value.append(string1.strip())
                    if key:
                        result[key]=value

    #print('key:' + '\n')
    #print(key)
    #print('-'*30)
    #print('values' + '\n')
    #print(value)
    return result

print(get_int_vlan_map(config_filename1))