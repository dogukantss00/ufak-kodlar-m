from scapy.all import*

ip=IP()

icmp=ICMP()

pingpacket=ip/icmp

addr="10.10.10."

for i in range(125,130):
    pingpacket[IP].dst=addr+str(i)
    print(pingpacket[IP].dst)

#buraya kadar olan kısım tüm ıp adreslerini tek tek yazar

    response=sr1(pingpacket,timeout=0.5)
    print(response)
#karşı tarafın acık olup olmadıgını gösterir