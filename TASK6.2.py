import re

ip_flag=False
while not ip_flag:
    ip = input('Введите ip address: ')
    flag = True
    try:
        ip_list1 = ip.split('.')
        ip_oct1 = int(ip_list1[0])
        ip_oct2 = int(ip_list1[1])
        ip_oct3 = int(ip_list1[2])
        ip_oct4 = int(ip_list1[3])
        if len(ip_list1) == 4:
            for num in ip_list1:
                test_num = int(num)
                if test_num >= 1 and test_num <= 255:
                    pass
                else:
                    flag = False
                    print('Вне диапазона')
                    break


            if flag:
                if ip_oct1 >= 1 and ip_oct1 <= 223:
                    print('unicast')
                elif ip_oct1 >= 224 and ip_oct1 <= 239:
                    print('multicast')
                elif ip == '255.255.255.255':
                    print('local broadcast')
                elif ip == '0.0.0.0':
                    print('unassigned')
                else:
                    print('unused')
                ip_flag = True
        else:
            print('Incorrect  lenght IP')
    except:
        print('Incorrect IP')


