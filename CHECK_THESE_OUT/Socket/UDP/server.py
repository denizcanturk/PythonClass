import socket as sc

# Server IP and port
server_ip = "0.0.0.0"  # Listen on all interfaces
server_port = 61127

# Create a UDP socket
server = sc.socket(sc.AF_INET, sc.SOCK_DGRAM)
server.setsockopt(sc.SOL_SOCKET, sc.SO_REUSEADDR, 1)  # Optional: reuse address and port

# Bind the socket to the address and port
server.bind((server_ip, server_port))

print(f"Server is listening on {server_ip}:{server_port}")

try:
    while True:
        # Receive message from client
        msg, addr = server.recvfrom(1024)  # Buffer size of 1024 bytes
        print(f"Received message from {addr}: {msg.decode('utf-8')}")

        # Optionally, send a response back to the client
        response = "Message received"
        server.sendto(response.encode("utf-8"), addr)

except KeyboardInterrupt:
    print("Server is shutting down...")

finally:
    # Close the socket
    server.close()
