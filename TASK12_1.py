import subprocess
reachable=[]
unreachable=[]
result=()


list_of_ip = ["192.168.0.2", '8.8.8.8', '192.168.0.1']

def check_reachability(ip_address):
    for ip in ip_address:
        reach=subprocess.run(['ping', ip], stdout=subprocess.DEVNULL) # проверяем доступность ip из списка, переданного функции
        if reach.returncode == 0: # если доступен, вернет returncode=0
            reachable.append(ip) # доступные ip добавляем в словарь
        else:
            unreachable.append(ip) # если не доступен, добавляем в другой словарь
    result=(reachable, unreachable) # делаем кортеж из словарей
    return result

if __name__=="__main__":
    print(check_reachability(list_of_ip))




