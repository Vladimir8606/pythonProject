import ipaddress

list1=['8.8.8.14-19', '3.3.3.3', '192.168.1.1-192.168.1.10', '1.1.1.1-4', '5.5.5.5', '2.2.2.222-2.2.2.227']
result=[]
it=[]

def convert_ranges_to_ip_list(ip_list):
    for ranges in list1:
        c = ranges.find('-')
        if c == -1:
            result.append(ranges)
        elif ranges.count('.') == 3:
            a = ranges.split('.')
            b = a[3].split('-')
            number1 = int((b[0]))
            number2 = int((b[1]))
            for ipv4 in range(number1, number2 + 1):
                d = a[0:3]
                d.append(str(ipv4))
                h = ','.join(d).replace(',', '.')
                result.append(h)

        elif ranges.count('.') == 6:
            a = ranges.split('-')
            it = []
            for items in a:
                b = items.split('.')
                it.append(b[3])
            num1 = int(it[0])
            num2 = int(it[1])
            for ip in range(num1, num2 + 1):
                d = b[0:3]
                d.append(str(ip))
                h = ','.join(d).replace(',', '.')
                result.append(h)
    return result

print(convert_ranges_to_ip_list(list1))
