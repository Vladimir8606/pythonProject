import yaml
from TASK12_2 import convert_ranges_to_ip_list

list1=['192.168.56.101-102']
output='C:\\python\\device_list.yaml'
device={}
username=input('Print username: ')
password=input('Print password: ')

def Create_device_list(ip):
    device={ 'device_type':'linux',
            'host':ip,
            'username':username,
            'password':password,
            'timeout':100

        }
    return device


if __name__=="__main__":
    list_of_ip_address=convert_ranges_to_ip_list(list1)
    Create_device_list(list_of_ip_address, output)

