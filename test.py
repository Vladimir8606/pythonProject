
topology_example = {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                    ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                    ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                    ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                    ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
                    ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
                    ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
                    ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
                    ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')}



class Topology:
    def unique_link(self,topology_dict):
        string1 = topology_dict.values()  # собираем значения словаря
        result1 = {}
        for k in topology_dict.keys():  # перебираем ключи словаля
            keys = (str(k).strip('()'))  # удаляем спец символы
            for val in string1:  # Перебираем значения словаря
                val1 = str(val).strip('[]')  # убираем спец символы
                if keys in val1:  # Если ключ находится в значениях
                    topology_dict[k] = None  # Делаем ключ равный None. Т.е. если ключ в строке 1 равен значения в строке n, значит это дублирующая связь
        for m, n in topology_dict.items():  # Все ключи, у которых значение не None, уникальные, записываем их в новый словарь
            if n != None:
                result1.update({m: n})
        self.topology=result1


top=Topology()
top.unique_link(topology_example)
print(top.topology)
