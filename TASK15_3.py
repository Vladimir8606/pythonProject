import re


filename_in='C:\\python\\cisco_nat_config.txt'
filename_out='C:\\python\\cisco_ASA_config.txt'

def convert_ios_nat_to_asa(input, output):
    '''Функция конвертирует NAT config IOS для ASA'''
    regex=(r'ip nat inside source (?P<nat_type>\S+) +' #static or dynamic
           r'(?P<proto>\S+) +' # protocol
           r'(?P<ip>\S+) +' # IP
           r'(?P<sport>\d+) +' # source port
           r'interface ' #
           r'(?P<intf>\S+) +' # interface
           r'(?P<dport>\d+)') # dest port
    with open(input) as f:
        lines=f.read()
        line=lines.split('\n')
        for each in line:
            #print(each)
            match=re.match(regex,each)
            if match:
                #print(match.groups())
                ip=match.group('ip')
                nat_type=match.group('nat_type')
                proto=match.group('proto')
                sport=match.group('sport')
                dport=match.group('dport')
                destination=(f'object network LOCAL_{ip}' +('\n') + f' host {ip}' +('\n') + f' nat (inside,outside) {nat_type} interface service {sport} {dport}' +('\n'))
                with open(output, 'a') as out:
                    out.writelines(destination)




convert_ios_nat_to_asa(filename_in, filename_out)