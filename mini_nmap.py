import nmap
#port taramaya yarar
ip=""
scanner=nmap.PortScanner()


# ne taraması yaptıgını,hangi method kullandıgını ve hangi servisleri taradıgını gösterir
scanner.scan(ip,"0-100","-sV")
print(scanner.scaninfo())
#ip ye yönelik tüm bilgileri basar
#state portun açık olmadıgını gösterir
print(scanner[ip].state())
#hangi protokollerin kullanıldıgını gösterir
print(scanner[ip].all_protocols)
#hangi portların acık oldugunu gösterir
print(scanner[ip]["tcp"].keys)
# belirtilen port hakkında bilgi verir
print(scanner[ip]["tcp",[21 ]])

for port in scanner[ip]["tcp"].keys():
    name=scanner[ip]["tcp"][port]["name"]
    product=scanner[ip]["tcp"][port]["product"]
    version=scanner[ip]["tcp"][port]["version"]
    print(port,name,product,version)