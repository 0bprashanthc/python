import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
client.connect("127.0.0.1",username="pchintalapudi",password="")
client.exec_command("")
