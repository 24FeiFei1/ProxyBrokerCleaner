with open("proxy.txt", "r") as file:
    proxy_list = file.readlines()

proxy_files = {}

for proxy in proxy_list:
    proxy_info = proxy.split()
    proxy_type = proxy_info[-2]
    ip_port = proxy_info[-1].rstrip('>')
    filename = f"{proxy_type}.txt"
    
    if filename not in proxy_files:
        proxy_files[filename] = []
    
    proxy_files[filename].append(ip_port)

for filename, proxies in proxy_files.items():
    with open(filename, "w") as file:
        for proxy in proxies:
            file.write(proxy + "\n")

print("Proxy bilgileri dosyalara çeşide göre ayrıldı.")
