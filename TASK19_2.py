from itertools import repeat
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)
import yaml
from concurrent.futures import ThreadPoolExecutor


output='C:\\python\\show_result.txt'

def send_command_show(device,command):
    print(device)
    #result = ''
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

def send_show_command_to_devices(devices,command,filename,limit):
    with ThreadPoolExecutor(max_workers=limit) as executor:
        result = executor.map(send_command_show, devices,repeat(command))
        for out in result:
            with open(filename, 'a') as f:
                f.write('\n')
                f.write(out)
                f.write('\n' + '-' * 30)


if __name__=="__main__":
    command = "ping 192.168.56.1 -c 5"
    with open("C:\\python\\device.yaml") as f:
        devices = yaml.safe_load(f)
    send_show_command_to_devices(devices, command, output, 3)