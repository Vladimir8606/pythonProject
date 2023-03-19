import re

with open('C:\\python\\ospf.txt') as src:
    for lines in src:
        list1 = lines.split()
        prefix= list1[1]
        AD = list1[2]
        next_hop = list1[4]
        Last_update = list1[5]
        Outbound_Interface = list1[6]
        result=('Prefix: ' + str(prefix) + '\n'
                'AD\Metric: ' + str(AD) + '\n'
                'Next-Hop: ' + str(next_hop).rstrip(',') + '\n'
                'Last update: ' + str(Last_update) + '\n'
                'Outbound Interface: ' + str(Outbound_Interface) + '\n'
                )
        print(result)