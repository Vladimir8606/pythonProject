import re
filename=input("ведите имя файла для чтения: ")
output=input("ведите имя файла для записи: ")
file='C:\\python\\' + filename + '.txt'
file_out='C:\\python\\' + output + '.txt'

ignore = ["duplex", "alias", "configuration"]

with open(file) as src:
 for lines in src:
     if lines.startswith('!'):
         continue
     for k in ignore:
         if str(k) in lines:
             break
     else:
         with open(file_out, 'a') as dest:
             dest.writelines(lines.rstrip() + '\n')