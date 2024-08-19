import socket as sc

# Get the server's IP address
server_ip = "192.168.1.26"  # Change this to the server's IP address if different
server_port = 61127

# Create a UDP socket
client = sc.socket(sc.AF_INET, sc.SOCK_DGRAM)

try:
    # Send a message to the server
    msg = input("Enter a message: ")
    client.sendto(msg.encode("utf-8"), (server_ip, server_port))
    print("Message sent")

    # Optionally, receive a response from the server
    try:
        response, addr = client.recvfrom(1024)  # Buffer size of 1024 bytes
        print(f"Received response from server: {response.decode('utf-8')}")
    except Exception as e:
        print(f"Error receiving response: {e}")

except Exception as e:
    print(f"Houston we have a problem: {e}")

finally:
    # Close the socket
    client.close()
