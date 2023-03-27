

headers = ["hostname", "ios", "platform"]

data = [
    ("R1", "12.4(24)T1", "Cisco 3825"),
    ("R2", "15.2(2)T1", "Cisco 2911"),
    ("SW1", "12.2(55)SE9", "Cisco WS-C2960-8TC-L"),
]
result=[]

def convert_to_dict(list_of_keys, list_of_tuples):
    for dataline in list_of_tuples:
        result1=dict(zip(list_of_keys,dataline))
        result.append(result1)
    return result



print(convert_to_dict(headers, data))