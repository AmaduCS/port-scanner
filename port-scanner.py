# A simple port scanning tool with my favorite language
import socket 

def scan_ports(target, start_port, end_port):
    print(f"Scanning {target} from port {start_port} to {end_port}...\n")
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5) # every half of second
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is OPEN")
    print("All Ports Scanned")


if __name__ == "__main__":
    target = input("Enter the target IP or Domain: ")
    start_port = int(input("Start Port: "))
    end_port = int(input("End Port: "))
    scan_ports(target, start_port, end_port)