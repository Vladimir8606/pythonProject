import re

result={}
filename='C:\\python\sh_cdp_n_sw1.txt'
def generate_description_from_cdp(file):
    regex=(r'(?P<hostname>\S+) +' # remote hostname
           r'(?P<int>\S+ +\S+) +' # local intf
           r'\d+ +' # hold timer
           r'\D? +\D? +\D? +' # capability
           r'\S+ +'  # platform
           r'(?P<rint>\S+ +\S+)') # remote intf
    with open(file) as f:
        a=f.read()
        lines=a.split('\n')
        for line in lines:
            match=re.match(regex,line)
            if match:
                #print(match.groups())
                rem_hostname = match.group('hostname')
                rem_int=match.group('rint')
                description=f'description Connected to {rem_hostname} port {rem_int}'
                result[match.group('int')]=description
    print(result)






generate_description_from_cdp(filename)