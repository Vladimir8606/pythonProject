from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)
import yaml


def send_show_command(device,command):
    result=''
    print(device)
    try:
        ssh=ConnectHandler(**device)
        result=ssh.send_command(command)
    except NetmikoTimeoutException:
        a=device['host']
        print(f' device {a} is not reachable')
    except NetmikoAuthenticationException:
        a = device['host']
        print(f' device {a} authentication is wrong')
    return result






if __name__ == "__main__":
    command = "sh bgp summary"
    with open("C:\\python\\device.yaml") as f:
        devices = yaml.safe_load(f)

    for dev in devices:
        print(send_show_command(dev, command))









