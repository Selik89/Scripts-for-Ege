import ipaddress

network = ipaddress.ip_network(f'63.178.184.0/255.255.255.192', 0)
cnt = 0
for ip in network:
    b = '0' * (32 - len(bin(int(ip))[2:])) + bin(int(ip))[2:]
    if b[:16].count('1') >= b[16:].count('1'):
        cnt += 1
print(cnt)