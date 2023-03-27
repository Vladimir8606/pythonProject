import re


filename='C:\\python\\cisco_nat_config.txt'
def convert_ios_nat_to_asa(input):
    regex=(r'ip nat inside source (\S+) +'
           r'(\S+) +'
           r'(\S+) +'
           r'(\d+) +'
           r'interface '
           r'(\S+) +'
           r'(\d+)') # static or dynamic
    with open(input) as f:
        lines=f.read()
        line=lines.split('\n')
        for each in line:
            print(each)
            match=re.match(regex,each)
            if match:
                print(match.groups())


convert_ios_nat_to_asa(filename)