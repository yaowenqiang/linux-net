
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
