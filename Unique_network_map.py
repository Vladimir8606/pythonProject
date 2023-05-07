
topology_example = {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                    ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                    ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                    ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                    ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
                    ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
                    ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
                    ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
                    ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')}


def unique_network_map (topology_dict):
    #Ищем повторяющиеся соединения и удаляем их
    result1 = {} #
    for k in topology_dict.keys(): # перебираем ключи словаля
        result1.update(k)
        print(result1)
        string1 = result1.values() #собираем значения словаря
        keys=(str(k).strip('()')) # удаляем спец символы
        #print(keys)
        for val in string1: # Перебираем значения словаря
            val1=str(val).strip('[]') # убираем спец символы
            if keys not in val1: # Если ключ находится в значениях
                result1.update(k)

    return result1


if __name__=="__main__":
    print(unique_network_map(topology_example))