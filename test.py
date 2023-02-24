import re
line = 'Jun  3 14:39:05.941: %SW_MATM-4-MACFLAP_NOTIF: Host f03a.b216.7ad7 in vlan 10 is flapping between port Gi0/5 and port Gi0/15'
match = re.search(r'((?:\w{4}\.){2}\w{4}).+vlan (\d+).+port (\S+).+port (\S+)', line)
#print(match.groups())


bgp= ''' 
sh ip bgp | be Network
Network          Next Hop       Metric LocPrf Weight Path
192.168.66.0/24  192.168.79.7                       0 500 500 500 i
                 192.168.89.8                       0 800 700 i
192.168.67.0/24  192.168.79.7         0             0 700 700 700 i
                 192.168.89.8                       0 800 700 i
192.168.88.0/24  192.168.79.7                       0 700 700 700 i
                 192.168.89.8         0             0 800 800 i
'''
#print(bgp)

for line in bgp.split('\n'):
     match = re.search(r'(\d+) \1 \1', line)
     if match:
          print(line)

vlans = ['10', '20', '30']

a= ','.join(vlans)
print(a)

