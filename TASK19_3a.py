from itertools import repeat
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)
import yaml
from concurrent.futures import ThreadPoolExecutor
from Create_device_dict import Create_device_list

devices=[]
command=[]


commands = {
    "192.168.56.101": ["ls",'ip a'],
    "192.168.56.102": ["ping 192.168.56.1 -c 5",'ping 192.168.56.3 -c 5', "ip a"],
    "192.168.56.103": ["ping 192.168.56.101 -c 5"]
}
output='C:\\python\\show_result_new.txt'

def send_command_show(ip,commands):
    output = 'C:\\python\\show_result_new.txt'
    device = Create_device_list(ip)
    print(commands)
    try:
        ssh = ConnectHandler(**device)
        for command in commands:
            promt=ssh.find_prompt()
            result1 = ssh.send_command(command, strip_prompt=True, strip_command=False)
            with open(output, 'a') as f:
                f.write('\n')
                f.write(result1)
                f.write('\n' + '-' * 30)
    except NetmikoTimeoutException:
        a = device['host']
        print(f' device {a} is not reachable')
    except NetmikoAuthenticationException:
        a = device['host']
        print(f' device {a} authentication is wrong')
    result=promt+result1
    return result

def send_show_command_to_devices(devices,command,limit):
    with ThreadPoolExecutor(max_workers=limit) as executor:
        executor.map(send_command_show, devices, command)



if __name__=="__main__":
    for devices_list, command_list in commands.items():
        devices.append(devices_list)
        command.append(command_list)

    send_show_command_to_devices(devices, command, 3)