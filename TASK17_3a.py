import yaml
import re
import glob

result={}
res={}
r={}
output="C:\\python\\topology.yaml"

def find_hostname(sh_cdp):
    regexp=r'^(.+)[>#]'
    match=re.match(regexp,sh_cdp)
    if match:
        hostname=match.group(0).strip('>').strip('#')
    return hostname


def parse_sh_cdp_neighbors(sh_cdp):
    regex = (r'(?P<hostname>\S+) +'  # remote hostname
             r'(?P<int>\S+ +\S+) +'  # local intf
             r'\d+ +'  # hold timer
             r'\D? +\D? +\D? +'  # capability
             r'\S+ +'  # platform
             r'(?P<rint>\S+ +\S+)')  # remote intf
    list1=sh_cdp.split('\n')
    r={}
    for lines in list1:
        a={}
        b={}
        match = re.search(regex, lines)
        if match:
            a[match.group('hostname')] = match.group('rint')
            b[match.group('int')] = a
            r.update(b)
            result[find_hostname(sh_cdp)]=r
    return result


def generate_topology_from_cdp(list_of_files, save_to_filename):
    result = parse_sh_cdp_neighbors(list_of_files)
    if 'C:\\python\\' in str(save_to_filename):
        with open(save_to_filename, 'a') as f:
            yaml.dump(result,f)
    else:
        result=None
    return result



if __name__=='__main__':
    sh_cdp_n = glob.glob("C:\\python\\sh_cdp_n*")
    for items in sh_cdp_n:
        with open(items) as f:
            file=f.read()
            res=(generate_topology_from_cdp(file,output))
    print(res)