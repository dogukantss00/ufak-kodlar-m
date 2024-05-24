import paramiko

def SendCommand(command):

    #kod çalıştırmak için kullanılır
    stdin,stdout,stderr=ssh.exec_command(command)

    #çıktı almak için
    cmd_output=stdout.read()
    print("<<":cmd_output.decode())


#ssh client olarak bağlantı yapmak için bir ssh nesnesi oluşturur
ssh=paramiko.SSHClient()

#ssh baglantısı bulamazsa yeni ip adresini bilinen bağlantıların arasına ekler
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ip="ip gir"
username=""
password=""

ssh.connect(ip,port=port,username=username,password=password)

command="whoami"
#gelen komut quit olmadıgı sürece komut istemeye devam edicek
while command.lower().strip()!="quit":
    
    if(command!=""):
        SendCommand(command)
    command=input(">>")

