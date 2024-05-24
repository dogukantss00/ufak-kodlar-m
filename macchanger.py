import random
import subprocess
charlist=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

a=random.choice(charlist)
newMAc=""

for i in range(12):
    newMAc=newMAc+random.choice(charlist)

print(newMAc)

ifconfigresult=subprocess.check_output("ifconfig eth0",shell=True).decode()
print(ifconfigresult)