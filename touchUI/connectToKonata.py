import paramiko
import os
from datetime import datetime

def ConnectToKonata(code):
    HOST=os.environ["KONATA_HOST"]
    USER=os.environ["KONATA_USER"]
    PRIVATE_KEY=os.environ["KONATA_KEY"]
    
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.load_system_host_keys()
    ssh.connect(HOST,username=USER,key_filename=PRIVATE_KEY)
    
    command='echo -e "1\n'+code+'" > $HOME/zaisekiKun/zaishituKun/touchUI/dataBank.txt'
    
    ssh.exec_command(command)
    ssh.close()

    print("---accept touchUI---")
    print("datetime : "+datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    print("code : "+code)

