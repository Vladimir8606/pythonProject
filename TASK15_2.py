import re

filename='C:\\python\\sh_ip_int_br.txt'

def parse_sh_ip_int_br(file):
    regex=(r'(\S+) +(\S+) +\w+ +\w+ +(\S+ ?+\S+) +(\S+)')
    with open(file) as f:
        a=f.read()
        result=re.findall(regex, a)
    return result

print(parse_sh_ip_int_br(filename))