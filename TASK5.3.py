import re

access_template = [
    "switchport mode access", "switchport access vlan {}",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

trunk_template = [
    "switchport trunk encapsulation dot1q", "switchport mode trunk",
    "switchport trunk allowed vlan {}"
]

type_int = input('access or trunk: ')
interface = input('Enter interface: ')
if type_int == 'access':
    vlans = input('Enter vlan: ')
    print('interface ' + interface)
    print(access_template[0])
    a = (access_template[1])
    b = (a.format(vlans))
    print(b)
    print(access_template[2])
    print(access_template[3])
    print(access_template[4])
else:
    vlans = input('Enter allowed vlans: ')
    print('interface ' + interface)
    print(trunk_template[0])
    print(trunk_template[1])
    a = (trunk_template[2])
    b = (a.format(vlans))
    print(b)
