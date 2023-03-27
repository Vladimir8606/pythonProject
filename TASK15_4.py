import re


filename = 'C:\\python\\config_r1.txt'

def get_ints_without_description(file):
    '''Функция изет интерфейсы на которых нет description и выводит их на stdout'''
    regex1=(r'interface (\S+)')
    regex2=(r'description (\S+)')
    with open(file) as f:
        a=f.read()
        list1=a.split('!')
        for items in list1:
            b=items.split('\n')
            for item in b:
                match=re.match(regex1,item)
                if match:
                    description=re.findall(regex2, items)
                    if not description:
                        print(match.group(1))


get_ints_without_description(filename)


