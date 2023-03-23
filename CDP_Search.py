def parse_cdp_neighbors(command_output):
    """
    Тут мы передаем вывод команды одной строкой потому что именно в таком виде
    будет получен вывод команды с оборудования. Принимая как аргумент вывод
    команды, вместо имени файла, мы делаем функцию более универсальной: она может
    работать и с файлами и с выводом с оборудования.
    Плюс учимся работать с таким выводом.
    """
    result={}
    number=0
    list1=command_output.split('\n') # Разделяем вывод построчно

    b=list1[0] # В переменную b записываем первую строку
    a=list1[0].find('>') # ищем hostname - все что будет перед ">"
    hostname=b[0:a]

    for item in list1: # читаем построчно
        if item.startswith('Device ID'): # Если строка начинается с Device ID, значит нам нужна следующая
            number=list1.index(item) # Ищем индекс этой строки
    list2=list1[number+1::] # Создаем новый список, в котором будут только строки нужные нам(указаны соседи)
    for items in list2: # читаем строки, нужные нам
        router, our_int, our_num_int, *others, rem_int, rem_int_num  =items.split() # записываем нужные нам данные, остальные войдут в переменную others
        intf=(our_int+our_num_int)
        remote_intf=(rem_int + rem_int_num)
        result[hostname, intf]=[router,remote_intf]
    return result

if __name__ == "__main__":
    with open("C:\\python\\sh_cdp_n_SW1.txt") as f:
        print(parse_cdp_neighbors(f.read()))
        print(type(parse_cdp_neighbors(f.read())))