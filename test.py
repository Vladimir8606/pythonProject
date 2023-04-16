from itertools import repeat
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)
from TASK12_2 import convert_ranges_to_ip_list
from Create_device_dict import Create_device_list
from concurrent.futures import ThreadPoolExecutor

list1=['192.168.56.101-102']
output='C:\\python\\show_result.txt'
ip_addr=[]

def send_command_show(ip,command):
    device=Create_device_list(ip)
    try:
        ssh = ConnectHandler(**device)
        promt=ssh.find_prompt()
        result1 = ssh.send_command(command, strip_prompt=True, strip_command=False)
    except NetmikoTimeoutException:
        a = device['host']
        print(f' device {a} is not reachable')
    except NetmikoAuthenticationException:
        a = device['host']
        print(f' device {a} authentication is wrong')
    result=promt+result1
    return result

def send_show_command_to_devices(ip,command,filename,limit):
    with ThreadPoolExecutor(max_workers=limit) as executor:
        result = executor.map(send_command_show, ip,repeat(command))
        for out in result:
            with open(filename, 'a') as f:
                f.write('\n')
                f.write(out)
                f.write('\n' + '-' * 30)


if __name__=="__main__":
    command = "ping 192.168.56.1 -c 5"
    list_of_ip_address=convert_ranges_to_ip_list(list1)
    for ip in list_of_ip_address:
        ip_addr.append(ip)
    send_show_command_to_devices(ip_addr, command, output, 3)