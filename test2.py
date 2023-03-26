import re
log = 'Jun  3 14:39:05.941: %SW_MATM-4-MACFLAP_NOTIF: Host f03a.b216.7ad7 in vlan 10 is flapping between port Gi0/5 and port Gi0/15'

match = re.search(r'Host (\S+) in vlan (\d+) .* port (\S+) and port (\S+)', log)

print(match)