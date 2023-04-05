import csv
import re

header=['switch','mac','ip','vlan','interface']
files=['C:\\python\\sw1_dhcp_snooping.txt',
       'C:\\python\\sw2_dhcp_snooping.txt',
       'C:\\python\\sw3_dhcp_snooping.txt']


file='C:\\python\\sw1_dhcp_snooping.txt'
out1='C:\\python\\result.csv'


def print_headers(headers, output):
    with open(output, 'a', newline='') as dst:
        writer = csv.writer(dst, delimiter=',')
        writer.writerow(headers)



def write_dhcp_snooping_to_csv(filename, output):
    regex=(r'(\w+:\w+:\w+:\w+:\w+:\w+) +'
           r'(\S+) +'
           r'\d+ +'
           r'\S+ +'
           r'(\d+) +'
           r'(\S+)')


    with open(filename) as f:
        name=str(filename).replace('C:\\python\\', '').replace('_dhcp_snooping.txt', '')
        a=f.read()
        list1=a.split('\n')
        for lines in list1:
            match=re.match(regex, lines)
            if match:
                res = []
                res.append(name)
                for items in match.groups():
                    res.append(items)
                with open(output, 'a', newline='') as dest:
                    writer = csv.writer(dest, delimiter=',')
                    writer.writerow(res)



if __name__=='__main__':
    print_headers(header, out1)
    for file in files:
        write_dhcp_snooping_to_csv(file, out1)