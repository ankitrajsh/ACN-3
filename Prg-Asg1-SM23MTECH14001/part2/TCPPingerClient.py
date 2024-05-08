import socket
import time

server_address = ('192.168.254.1', 12000)  
try:
    N = int(input("Enter the number of pings to send: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit(1)

min_rtt = float('inf')
max_rtt = 0
total_rtt = 0
packet_loss_count = 0

for sequence_number in range(1, N + 1):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        start_time = time.time()
        client_socket.connect(server_address)
        ping_message = f"PING {sequence_number} {time.time()}"
        client_socket.send(ping_message.encode())
        response = client_socket.recv(1024).decode()
        end_time = time.time()
        rtt = end_time - start_time
        min_rtt = min(min_rtt, rtt)
        max_rtt = max(max_rtt, rtt)
        total_rtt += rtt

        if response != ping_message:
            print(f"Request timed out for sequence number  {sequence_number}")
            packet_loss_count += 1
        else:
            print(f"Received: {response}, RTT: {rtt:.6f} seconds")

    except ConnectionRefusedError:
    
        print(f"Request timed out for sequence number {sequence_number}")
        packet_loss_count += 1
    finally:
       
        client_socket.close()

average_rtt = total_rtt / (N - packet_loss_count) if (N - packet_loss_count) > 0 else 0

packet_loss_rate = (packet_loss_count / N) * 100

print("\nPing statistics:")
print(f"   Packets sent: {N}")
print(f"   Packets received: {N - packet_loss_count}")
print(f"   Packet loss rate: {packet_loss_rate:.2f}%")
print(f"   Minimum RTT: {min_rtt:.6f} seconds")
print(f"   Maximum RTT: {max_rtt:.6f} seconds")
print(f"   Average RTT: {average_rtt:.6f} seconds")

