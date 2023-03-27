import re

result={}
filename='C:\\python\\config_r2.txt'


def get_ip_from_cfg(file):
    regex=(r' ip address (\S+) (\S+)')
    with open(file) as f:
        a=f.read()
        list1=a.split('!')
        for items in list1:
            b=items.split('\n')
            for item in b:
                match=re.match(r'interface (\S+)', item)
                if match:
                    ip_mask=re.findall(regex, items)
                    if ip_mask:
                        result[match.groups()[0]]=ip_mask
    return result

print(get_ip_from_cfg(filename))