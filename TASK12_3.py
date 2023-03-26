from TASK12_1 import check_reachability
from TASK12_2 import convert_ranges_to_ip_list
from tabulate import tabulate


list2=['8.8.8.14-19', '3.3.3.3', '5.5.5.5', '192.168.0.1-192.168.0.9', '6.6.6.6']
reachable=[]
result=[]
result1=()
dict={}

columns=['Reachable', 'Unreachable']




def print_ip_table(reach):
    dict['reachable']=reach[0]
    dict['unreachable'] = reach[1]
    print(tabulate(dict, headers='keys'))

if __name__=="__main__":
    result1 = check_reachability(convert_ranges_to_ip_list(list2))
    reachability=[result1[0],result1[1]]

    print_ip_table(reachability)