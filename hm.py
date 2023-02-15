import mmap
scanner = mmap.PortScanner()
ip=input("ip ")
print("Resultado")
scanner.scan(ip)
print(scanner.all_hosts())