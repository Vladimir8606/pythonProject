trunk_mode_template = [
    "switchport mode trunk", "switchport trunk native vlan 999",
    "switchport trunk allowed vlan"
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17]
}

result={}


def generate_access_config(trunk_config_var, trunk_mode_template_var):

    """
    intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
        {"FastEthernet0/12": 10,
         "FastEthernet0/14": 11,
         "FastEthernet0/16": 17}
    access_template - список команд для порта в режиме access

    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    """
    for intf, vlan in trunk_config_var.items():
        result1 = []
        for command in trunk_mode_template_var:
            if command.endswith('allowed vlan'):
                vlan_str=''.join(str(vlan).strip('[]'))
                result1.append(command + ' ' + vlan_str)
            else:
                result1.append(command)
        result[intf]=str(result1).strip('[]')
    return result

print(generate_access_config(trunk_config, trunk_mode_template))

