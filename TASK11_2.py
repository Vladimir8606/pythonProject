import sys

from CDP_Search import parse_cdp_neighbors
import graphviz as gv

import os
os.environ["PATH"] += os.pathsep + 'C:\\Program Files\\Graphviz2.38\\bin\\'
styles = {
    'graph': {
        # 'label': 'Network Map',
        # 'fontsize': '16',
        'fontcolor': 'white',
        'bgcolor': '#333333',
        'rankdir': 'BT',
    },
    'nodes': {
        'fontname': 'Helvetica',
        'shape': 'ellipse',
        'fontcolor': 'white',
        'color': '#006699',
        'style': 'filled',
        'fillcolor': '#006699',
        'margin': '0.2',
    },
    'edges': {
        'style': 'bold',
        'color': 'red',
        'arrowhead': 'open',
        'fontname': 'Helvetica',
        'fontsize': '14',
        'fontcolor': 'white',
    }
}
result={}




infiles = [
    "C:\\python\\sh_cdp_n_sw1.txt",
    "C:\\python\\sh_cdp_n_r1.txt",
    "C:\\python\\sh_cdp_n_r2.txt",
    "C:\\python\\sh_cdp_n_r3.txt"
]

def apply_styles(graph, styles):
    graph.graph_attr.update(('graph' in styles and styles['graph']) or {})
    graph.node_attr.update(('nodes' in styles and styles['nodes']) or {})
    graph.edge_attr.update(('edges' in styles and styles['edges']) or {})
    return graph

def draw_topology(topology_dict, output_filename):
    nodes = set([
        item[0]
        for item in list(topology_dict.keys()) + list(topology_dict.values())
    ])
    g1 = gv.Graph(format='svg')
    #print(nodes)
    for node in nodes:
        g1.node(node)

    for key, value in topology_dict.items():
        head, t_label = key
        tail, h_label = value
        g1.edge(
            head, tail, headlabel=h_label, taillabel=t_label, label=" " * 12)

    g1 = apply_styles(g1, styles)
    g1.render(filename=output_filename)
    #print("Graph saved in", filename)

def unique_network_map (topology_dict):
    #Ищем повторяющиеся соединения и удаляем их
    string1=topology_dict.values() # собираем значения словаря
    result1={}
    for k in topology_dict.keys(): # перебираем ключи словаля
        keys=(str(k).strip('()')) # удаляем спец символы
        for val in string1: # Перебираем значения словаря
            val1=str(val).strip('[]') # убираем спец символы
            if keys  in val1: # Если ключ находится в значениях
                topology_dict[k]=None # Делаем ключ равный None. Т.е. если ключ в строке 1 равен значения в строке n, значит это дублирующая связь
    for m,n in topology_dict.items(): # Все ключи, у которых значение не None, уникальные, записываем их в новый словарь
        if n != None:
            result1.update({m:n})

    return result1





def create_network_map (filenames):
    for k in filenames:
        with open(k) as f:
            result.update(parse_cdp_neighbors(f.read()))
    return result


output="C:\\python\\topology.sgv"
if __name__ == "__main__":
    unique_network_map(create_network_map((infiles)))
    draw_topology(unique_network_map(create_network_map((infiles))),output)