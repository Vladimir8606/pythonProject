access_mode_template = [
        "switchport mode access", "switchport access vlan",
        "switchport nonegotiate", "spanning-tree portfast",
        "spanning-tree bpduguard enable"
    ]

access_config = {
    "FastEthernet0/12": 10,
    "FastEthernet0/14": 11,
    "FastEthernet0/16": 17
}

access_config_2 = {
    "FastEthernet0/03": 100,
    "FastEthernet0/07": 101,
    "FastEthernet0/09": 107,
}
port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security"
]
result=[]
psecurity=None

def generate_access_config(intf_vlan_mapping, access_template, psecurity):

    """
    intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
        {"FastEthernet0/12": 10,
         "FastEthernet0/14": 11,
         "FastEthernet0/16": 17}
    access_template - список команд для порта в режиме access

    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    """
    for intf, vlan in intf_vlan_mapping.items():
        result.append("interface " + intf)
        for command in access_template:
            if command.endswith('access vlan'):
                result.append(command + ' ' + str(vlan))
            else:
                result.append(command)
        result.extend(psecurity)
    return result

print(generate_access_config(access_config_2, access_mode_template,port_security_template))

