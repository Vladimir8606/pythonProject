import csv
import re
from TASK17_1 import print_headers
import glob

headers=['hostname', 'ios', 'image', 'uptime']
output='C:\\python\\sh_ver_result.csv'

def parse_sh_version(sh_ver):
    regex = (r'Cisco IOS Software, \d+ Software \S+, Version (?P<ios>\S+).+router uptime is (?P<uptime>.+).+System returned.+System image file is (?P<image>\S+)')
    match=re.match(regex, sh_ver, re.DOTALL)
    if match:
        result=match.group('ios','image','uptime')
    return result


def get_filename(file):
    name = str(file).replace('C:\\python\\', '').replace('sh_version_', '').replace('.txt', '')
    return name

def write_inventory_to_csv(data_filenames, csv_filenames):
    print_headers(headers, csv_filenames)
    for files in data_filenames:
        with open(files) as file:
            lines=file.read()
            res = []
            res.append(get_filename(files))
            for items in parse_sh_version(lines):
                res.append(items)
            with open(csv_filenames, 'a', newline='') as dest:
                writer = csv.writer(dest, delimiter=',')
                writer.writerow(res)







if __name__=='__main__':
    sh_version_files = glob.glob("C:\\python\\sh_vers*")
    write_inventory_to_csv(sh_version_files, output)
