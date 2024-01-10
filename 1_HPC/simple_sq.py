import subprocess

batcmd="squeue"
result = subprocess.check_output(batcmd, shell=True, text=True)
# print ('hello sq')

#print (result)

with open('/tmp/sq.txt', 'w') as f:
    f.write(result)
