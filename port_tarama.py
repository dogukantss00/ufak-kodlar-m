import socket

ip="10.0.2.4"

for port in range(1,100):
    try:
        #port tanımlar
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip,port))
        print(str(port),"open")
    except Exception as e:
        print(str(port),"closed")
        pass
    finally:
        s.close