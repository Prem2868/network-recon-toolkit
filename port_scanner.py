#!/usr/bin/env python3
# ============================================================================
# PremLabs Security
# ============================================================================
# Author: Pramod Jogdand (@Prem2868)
# Description: Simple Python port scanner for network reconnaissance
# ============================================================================

import socket
import sys
from datetime import datetime


def scan_port(host, port, timeout=1):
    """
    Attempts to connect to a specific port on the target host.
    
    Args:
        host (str): Target hostname or IP address
        port (int): Port number to scan
        timeout (int): Connection timeout in seconds
    
    Returns:
        bool: True if port is open, False otherwise
    """
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        
        # Attempt connection
        result = sock.connect_ex((host, port))
        sock.close()
        
        # Return True if connection successful (port open)
        return result == 0
    except socket.gaierror:
        print(f"[-] Hostname {host} could not be resolved")
        return False
    except socket.error:
        print(f"[-] Could not connect to {host}")
        return False


def scan_common_ports(host):
    """
    Scans common ports on the target host.
    
    Args:
        host (str): Target hostname or IP address
    
    Returns:
        list: List of open ports found
    """
    # Common ports to scan
    common_ports = [21, 22, 23, 25, 53, 80, 443, 8080, 8443, 3306]
    
    open_ports = []
    
    print(f"\n[*] Starting port scan on {host}")
    print(f"[*] Scan started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    
    # Scan each port
    for port in common_ports:
        if scan_port(host, port):
            print(f"[+] Port {port} is OPEN")
            open_ports.append(port)
        else:
            print(f"[-] Port {port} is closed")
    
    return open_ports


def main():
    """
    Main function to run the port scanner.
    """
    # Check for command line arguments
    if len(sys.argv) < 2:
        print("Usage: python3 port_scanner.py <hostname/IP>")
        print("Example: python3 port_scanner.py 192.168.1.1")
        sys.exit(1)
    
    # Get target host from command line
    target_host = sys.argv[1]
    
    # Run the port scan
    open_ports = scan_common_ports(target_host)
    
    # Display results
    print("-" * 50)
    print(f"[*] Scan completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"[*] Total open ports found: {len(open_ports)}")
    
    if open_ports:
        print(f"[+] Open ports: {', '.join(map(str, open_ports))}")
    else:
        print("[-] No open ports found")
    
    print("\n[*] Port scan complete!")


if __name__ == "__main__":
    main()
