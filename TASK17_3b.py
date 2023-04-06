import yaml
import glob
from TASK17_3a import generate_topology_from_cdp
from TASK11_2 import unique_network_map
from TASK11_2 import draw_topology

output="C:\\python\\topology.yaml"
resul={}
out1="C:\\python\\new_topology.sgv"

def transform_topology(topology):
    with open(topology) as f:
        template=yaml.safe_load(f)
    for key,value in template.items():
        for key1, value1 in value.items():
            for key2, value2 in value1.items():
                resul[key,key1]=(key2, value2)
    return(resul)



if __name__=="__main__":
    sh_cdp_n = glob.glob("C:\\python\\sh_cdp_n*")
    for items in sh_cdp_n:
        with open(items) as f:
            file = f.read()
            res = (generate_topology_from_cdp(file, output))
    transform_topology(output)
    draw_topology(unique_network_map(transform_topology(output)), out1)