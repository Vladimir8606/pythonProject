from itertools import repeat
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)
import yaml
from concurrent.futures import ThreadPoolExecutor, as_completed


output='C:\\python\\show_result2.txt'

def send_command_show(device,command):
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

def send_commands_to_devices(devices,command,limit):
    for device in devices:
        future_list = []
        with ThreadPoolExecutor(max_workers=limit) as executor:
            future = executor.submit(send_command_show, device,command)
            future_list.append(future)
        for a in as_completed(future_list):
            res=a.result()
            with open(output, 'a') as f:
                f.write('\n')
                f.write(res)
                f.write('\n' + '-' * 30)


if __name__=="__main__":
    command = "ip a"
    with open("C:\\python\\device.yaml") as f:
        devices = yaml.safe_load(f)
    send_commands_to_devices(devices, command, 3)