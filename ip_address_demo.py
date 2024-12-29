import ipaddress

net = list(ipaddress.ip_network('10.10.2.0/25'))

for i in list(net):
    print(i)

print(f'the ip range is {net[0]} - {net[-1]}')
