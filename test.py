import re


filename='C:\\python\sh_cdp_n_sw1_1.txt'
def generate_description_from_cdp(file):
    regex=(r'(?P<hostname>\S+) +' # remote hostname
           r'(?P<int>\S+) + (?P<port>\S+) +' # local intf
           r'\d+ +' # hold timer
           r'\S+ + ?\S+ + ?\S+ +' # capability
           r'\S +'  # platform
           r'(?P<rint>\S+) + (?P<rport>\S+)') # remote intf
    with open(file) as f:
        a=f.read()
        match=re.findall(regex,a)
        if match:
            print(match.groups())






generate_description_from_cdp(filename)