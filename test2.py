import subprocess

result = subprocess.run(['ping', '8.8.8.8'], stdout=subprocess.PIPE)
output = result.stdout.decode('utf-8')
print(output)