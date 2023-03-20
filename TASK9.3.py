config_filename1='C:\\python\\config_sw2.txt'
result_access={}
result_trunk={}
result_={}

def get_int_vlan_map(config_filename):
    file=open(config_filename, 'r')
    a=file.read()
    b=a.split('!')
    for item in b:
        if item.strip().startswith('interface'):
            intf_list=item.split() #Ищем строки с номерами интерфейсов, чтобы использовать в ключе
            list1=item.split('\n') # разбиваем конфиг построчно
            for strings in list1:
                if strings.strip() == 'switchport mode trunk':
                    for strings2 in list1:
                        result1 = []
                        if strings2.strip().startswith('switchport trunk allowed vlan'):
                            vlan=strings2.split() # Строку switchport trunk allowed vlan разбиваем в список по пробелу
                            num_str=vlan[4] # Ищем номера разрешенных вланов
                            list2=num_str.split(',') # 1,2,3 разбиваем на строки с числами
                            m=[]
                            for items in list2: # читаем список с номерами вланов
                                m.append(int(items))  # делаем их числами
                                result_trunk[intf_list[1]]=m

                if strings.strip() == 'switchport mode access':
                    flag=True
                    for strings2 in list1:
                        result1 = []
                        if strings2.strip().startswith('switchport access vlan'):
                            vlan=strings2.split() # Строку switchport access vlan разбиваем в список
                            result1.append(vlan[3]) # result1 - список из одной строки - номер влана
                            result_str=str(result1).strip('[]') # Номер влана переводим из списка в строку и удаляем []
                            e=result_str[1:-1] # т.к. result_str строка в формате '100', первый и последний символы отбрасываем
                            g=int(e)
                            if g:
                                result_access[intf_list[1]]=g
                                flag=False
                    if flag:
                        result_access[intf_list[1]] = 1 # Если в явном виде нет строки switchport access vlan и номер, то порт в первом влане





    result=(result_access, result_trunk) # делаем кортеж из словарей
    return result

print(get_int_vlan_map(config_filename1))