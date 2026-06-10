import ipaddress

def subnet_info(network_input):
    try:
        network = ipaddress.ip_network(network_input, strict=False)

        print("\nNetwork Information")
        print("-------------------")
        print(f"Network Address: {network.network_address}")
        print(f"Broadcast Address: {network.broadcast_address}")
        print(f"Subnet Mask: {network.netmask}")
        print(f"CIDR: /{network.prefixlen}")
        print(f"Total Addresses: {network.num_addresses}")

        usable_hosts = max(network.num_addresses - 2, 0)
        print(f"Usable Hosts: {usable_hosts}")

        hosts = list(network.hosts())
        if hosts:
            print(f"First Usable IP: {hosts[0]}")
            print(f"Last Usable IP: {hosts[-1]}")
        else:
            print("No usable host addresses.")

    except ValueError:
        print("Invalid network.")

def main():
    print("Small Business Network Subnet Calculator")
    print("Example: 192.168.10.0/24")

    while True:
        user_input = input("\nEnter a network or type 'q' to quit: ")

        if user_input.lower() == "q":
            print("Goodbye!")
            break

        subnet_info(user_input)

if __name__ == "__main__":
    main()
