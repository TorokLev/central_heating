import paramiko

hostname = '192.168.1.101'
password = '*****'
username = "pi"
port = 22

mypath='/sys/bus/w1/devices/28-02146384abff/w1_slave'
remotepath='/home/pi/28-02146384abff.txt'


t = paramiko.Transport((hostname, 22))
t.connect(username=username, password=password)
sftp = paramiko.SFTPClient.from_transport(t)
sftp.put(mypath, remotepath)
