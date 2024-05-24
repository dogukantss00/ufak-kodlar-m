from scapy.all import*

eth= Ether()

arp = ARP()

eth.dst="ff:ff:ff:ff:ff:ff"

arp.pdst="10.0.2.1/24"

bcpckt=eth/arp



ans,unans=srp(bcpckt,timeout=5)


print("#"*30)

for snd,rcv in ans:
    print(rcv.psrc,":",rcv.src)