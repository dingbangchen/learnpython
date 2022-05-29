import subprocess
ipadd = input("Please input the ip address\n")
command1 = ['ping','-n','1',ipadd]
subprocess.call(command1)