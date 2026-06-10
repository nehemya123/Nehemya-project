# Packet Tracer Small Business Network Lab

This project simulates a small business network using Cisco Packet Tracer and includes a Python subnet calculator for network planning.

## Project Goals

- Design a small business network
- Configure routers, switches, PCs, and servers
- Practice IP addressing, DHCP, DNS, and troubleshooting
- Use Python to calculate subnet information

## Network Design

The network includes:

- 1 router
- 2 switches
- 6 PCs
- 1 server
- 3 departments:
  - Admin
  - Sales
  - IT

## IP Plan

| Department | Network | Gateway |
|---|---|---|
| Admin | 192.168.10.0/24 | 192.168.10.1 |
| Sales | 192.168.20.0/24 | 192.168.20.1 |
| IT | 192.168.30.0/24 | 192.168.30.1 |

## Python Tool

The `subnet_calculator.py` file calculates:

- Network address
- Broadcast address
- Subnet mask
- CIDR
- Usable host range
- Total usable hosts

## Skills Practiced

- Cisco Packet Tracer
- TCP/IP networking
- IP addressing
- Subnetting
- DHCP and DNS basics
- Python scripting
- Git and GitHub documentation
