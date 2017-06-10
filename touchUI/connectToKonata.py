import paramiko
import os


def ConnectToKonata(code):
    HOST=os.environ["KONATA_HOST"]
    USER=os.environ["KONATA_USER"]
    PRIVATE_KEY='/home/xztaityozx/.ssh/konata_rsa'
    
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.load_system_host_keys()
    ssh.connect(HOST,username=USER,key_filename=PRIVATE_KEY)
    
    command='echo -e "1\n'+code+'" > /home/ubuntu/zaisekiKun/zaishituKun/touchUI/dataBank.txt'
    
    ssh.exec_command(command)
    ssh.close()



