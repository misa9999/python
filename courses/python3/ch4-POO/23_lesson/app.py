from calcipv4 import CalcIPv4


calc_ipv4 = CalcIPv4(ip="192.168.0.1", mask="255.255.255.0", prefix=24)


print(f"IP: {calc_ipv4.ip}")
print(f"Mask: {calc_ipv4.mask}")
print(f"Rede: {calc_ipv4.rede}")
print(f"Broadcast: {calc_ipv4.broadcast}")
print(f"Prefix: {calc_ipv4.prefix}")
print(f"Num ips: {calc_ipv4.ips}")
