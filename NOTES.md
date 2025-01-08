
Potential Virtualzation Systems

+ Hyper-V
+ VMware Workstation
+ Paralles
+ KVM
+ proxmox
+ ESXI


## KVM

Virtual Machine manager

NAT(network Address translation)


## ssh


sudo apt install openssh-server

tilix https://github.com/gnunn1/tilix/

gnome-terminal

## soho

+ Small Office/Home Office
+ Typically 20 hosts or less
+ Internet connectivity
+ Wireless

## SMB/SME

+ Small to medium-sized Business/enterprise
+ 1000 hosts or less
+ More networking devices

## Large enterprise

+ Anything goes
+ 1000 hosts or More
+ Global
+ ON-premises and clouse-based


Search for

+ SOHO LAN Diagram
+ Enterprise LAN Diagram

## TCP/IP


+ TCP/IP is a suite of protocols used by computers to communicate with each other
+ It includes TCP and IP, but also many others including HTTP, FTP, POP3, DNS, DHCP, and many more



ip -br -c a

CIDR Notation and networks

## DHCP

DHCP = Dynamic Host Configuration Protocol

It assigns TCP/IP information automatically to computers(IP address, netmask, GW, and DNS)

RFC2131

Use port 67 and 68 by default

Employs a four step process known as DORA

+ Discovery 
+ Offer
+ Request
+ Acknowledge


DNS

DNS is the Comain Name System

A wordwide sytem of domains, hosts and DNS servers which is defined in RFC 1591

The server use port 53 inbound by default

A fully qualified domain name (FQDN) is the combination of a host name and domain name, example ns1.example.com

The OSI model

+ Application
+ Presentation
+ Session
+ Transport
+ Network
+ Data Link
+ Physical



| Layer | name | PDU | Protocols |
| --------------- | --------------- | --------------- | ---------- |
| Layer7 | Application | Messages(Data) | FTP, HTTPS, POP3
| Layer6 | Presentation |  | ASCII, XML, JSON  | 
| Layer5 | Session |  | Duplexing, X.225 |
| Layer4 | Transport | Segments/Datagrams | TCP - UDP |
| Layer3 | Network | Packets | IPv4, ICMP, Routing |
| Layer2 | Data Link | Frames | 802.3, 802.11x |
| Layer1 | Phsical | bits | 1000BASE-T, Cat 6 |



TCP/IP model

+ Application
+ Transport
+ Internet
+ Link

Linux systems rely on one of serveral networking services, the three most common are networking, networkd and NetworkManager


apt  install network-manager

systemctl status NetworkManager


service networking status
/etc/init.d/networking status

location of configuration file:

/etc/network/interfaces

ip a
ip r ( short for ip route show)

ifquery

/etc/resolv.conf

systemctl status systemd-networkd

vim /etc/systemd/network/eth0.network


networkd (ubuntu)


nmcli

systemctl status systemd-networkd

Location of configuration file:
Ubuntu Server: /etc/netplan
Other distros: /etc/systemd/network

netplan try
netplan apply

networkctl
networkctl status

/etc/systemd/resolved.conf

resolvectl

## NetworkManager

systemctl status NetworkManager


Can be configured with a variety of tools

+ Settings, nm-connection-editor, nmtui, nmctl, cockpit,and configuration files (not recommended)

nmcli

nmcli edit

systemctl status cockpit.socket
systemctl enable --now cockpit.socket

NetworkManager configure files

/etc/NetworkManager/system-connections( key file, or ini file)
/etc/sysconfig/network-scripts

journalctl -u NetworkManager

### wicked

+ used by SUSE/openSUSE
+ To see if it is active, type systemctl status wicked
+ Can be configured with yaST2(uast command), netconfig command, or configuration file
+ Location of configuration file /etc/sysconfig/network

## Amazon Linux

+ Uses the systemd-networkd service
+ systemctl status systemd-networkd
+ /etc/sysconfig/network-scripts



## The ip Command


ip --help

main ip

ip link (Data Link layer)
ip link show
ip l


ip address (Network Layer)
ip address show
ip a

ip -br a


ip a s eth0 // just show specified network interface

ip -j a s eth0 // show json format
ip -j a s eth0 | jq '.' // show json format
ip -j -p a s eth0 // show json format, pretty

ip a | grep inet   | sort -n
ip -o -4 a | column -t
ip  -br  -4 a   | awk '{print $3}'
ip  -br  -4 a   | awk '{print $3}'  | cut -d/ -f1

/sys/class/net/

ip route show
ip route
ip r

ip -c r  | column -t

remote gateway

ip r delete default
ip r add default via 10.1.20.1
ip r add  172.21.0.0 dev eth0 
ip r delete  172.21.0.0/16

## Network Testing Commands

+ ping
+ traceroute
+ whois
+ dig(and nslookup)
+ ss
+ nmap


### ping

ping <hostname> 
ping <ip_address> 

ping -c
ping -s // specifies the packetsize 
ping -s 1400


### traceroute

apt install traceroute

traceroute example.com
traceroute -n example.com
traceroute -n example.com -q 5

### whois

whois example.com
whois prowse.tech
whois prowse.tech -H -I


### dig and nslookup

dig example.com
dig -x 93.184.215.14

nslookup example.com

nslookup 

### ss


ss -ant
ss -tulnw
ss -plunt
ss -tun

## nmap

nmap -V

nmap -sn 10.0.2.0/24

nmap  10.1.20.16

ip neighbor

ip nei
ip n


## Hostnames and DNS

hostnamectl set-hostname <hostame>

vim /etc/hostsname
hostnamectl set-location lab1



## DNS

/etc/resolv.conf
/etc/systemd/resolved.conf

nmcli connection modify eth0 ipv4.dns 8.8.8.8

### netplan

vim /etc/netplan/50-cloud-init.yaml 

vim /etc/systemd/resolved.conf


## Working with the hosts file








## Hostname and FQDN

hostname + domain name = FQDN






## nmcli

| nmcli command | Descrioption |
| -------------- | --------------- |
| nmcli | Displays the network configuration |
| nmcli con show | Displays the avaiable NetworkManager connections |
| nmcli con mod <network-interface> ... | Modifies the connection without the shell |
| nmcli con down <network-interface> | brings the network interface down |
| nmcli con up <network-interface> | brings the network interface up |
| nmcli con edit <network-interface> | Opens the nmcli shell |

nmcli c s ( for connection show)


