import netmiko
cisco_router = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.1',
    'username': 'user',
    'password': 'userpass',
    'secret': 'enablepass',
    'port': 20022,
}
ssh = ConnectHandler(**cisco_router)
ssh.enable()
result = ssh.send_command('show ip int br')
