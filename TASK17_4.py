import csv
import datetime
from TASK17_1 import print_headers

input='C:\\python\\mail_log.csv'
out='C:\\python\\result_mail_log.csv'
list1=[]
res=[]
result=[]

def convert_str_to_datetime(datetime_str):
    """
    Конвертирует строку с датой в формате 11/10/2019 14:05 в объект datetime.
    """
    return datetime.datetime.strptime(datetime_str, "%d/%m/%Y %H:%M")

def convert_datetime_to_str(datetime_obj):
    """
    Конвертирует строку с датой в формате 11/10/2019 14:05 в объект datetime.
    """
    return datetime.datetime.strftime(datetime_obj, "%d/%m/%Y %H:%M")

def write_last_log_to_csv(source_log,output):
    with open(source_log) as f:
        reader=csv.reader(f)
        headers=next(reader)
        a=list(reader)
        for items in a:
            item=convert_str_to_datetime(items[2]),items[1],items[0]
            list1.append(list(item))
        a=sorted(list1)
        a.reverse()
        for itemss in a:
            if str(itemss[1]) not in str(result):
                result.append(itemss)
        for lines in result:
            line=lines[2],lines[1],convert_datetime_to_str(lines[0])
            res.append(list(line))
    print_headers(headers,output)
    for r in res:
        with open(output, 'a', newline='') as dest:
            writer = csv.writer(dest, delimiter=',')
            writer.writerow(r)



if __name__=="__main__":
    write_last_log_to_csv(input, out)