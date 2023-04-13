import netmiko
import logging
from concurrent.futures import ThreadPoolExecutor

import subprocess
reachable=[]
unreachable=[]

list1=['1.1.1.1','10.0.0.1','8.8.8.8','10.0.0.2']
result=()

logging.getLogger('paramiko').setLevel(logging.WARNING)

logging.basicConfig(
    format = '%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO,
)

def check_ip(ip_address):
    reach=subprocess.run(['ping', ip_address], stdout=subprocess.DEVNULL) # проверяем доступность ip из списка, переданного функции
    return reach.returncode

def concurrent(list_of_address,limit):
    with ThreadPoolExecutor(max_workers=limit) as executor:
        result = executor.map(check_ip, list_of_address)
        for device, output in zip(list_of_address, result):
            if output == 0:  # если доступен, вернет returncode=0
                reachable.append(device)  # доступные ip добавляем в словарь
            else:
                unreachable.append(device)  # если не доступен, добавляем в другой словарь
        result = (reachable, unreachable)  # делаем кортеж из словарей
        return result


if __name__=="__main__":
    print(concurrent(list1,3))