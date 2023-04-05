import csv
import re
import glob

result={}
r={}

def find_hostname(sh_cdp):
    regexp=r'^(.+)[>#]'
    match=re.match(regexp,sh_cdp)
    if match:
        hostname=match.group(0).strip('>').strip('#')
    return hostname


def parse_sh_cdp_neighbors(sh_cdp):
    regex = (r'(?P<hostname>\S+) +'  # remote hostname
             r'(?P<int>\S+ +\S+) +'  # local intf
             r'\d+ +'  # hold timer
             r'\D? +\D? +\D? +'  # capability
             r'\S+ +'  # platform
             r'(?P<rint>\S+ +\S+)')  # remote intf
    list1=sh_cdp.split('\n')
    for lines in list1:
        a={}
        b={}
        match = re.search(regex, lines)
        if match:
            a[match.group('hostname')] = match.group('rint')
            b[match.group('int')] = a
            r.update(b)
            result[find_hostname(sh_cdp)]=r
    return result






if __name__=='__main__':
    with open('C:\\python\\sh_cdp_n_sw1.txt') as f:
        file=f.read()
    print(parse_sh_cdp_neighbors(file))
