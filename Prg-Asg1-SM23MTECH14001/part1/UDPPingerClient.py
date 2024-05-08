# Create a UDP socket
client_socket = socket(AF_INET, SOCK_DGRAM)

client_socket.settimeout(1.0)

try:
    N = int(input("Enter the number of pings to send: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit(1)

rtt_times = []
lost_packets = 0

for sequence_number in range(1, N + 1):

    timestamp = time.time()

    message = f"Ping {sequence_number} {timestamp}".encode()

    start_time = time.time()

    client_socket.sendto(message, server_address)

    try:
        response, server_addr = client_socket.recvfrom(1024)

        # Calculate the round-trip time (RTT) using the timestamp
        end_time = time.time()
        rtt = end_time - timestamp
        rtt_times.append(rtt)

        # Print the response message and RTT
        print(f"Received: {response.decode()}, RTT: {rtt:.6f} seconds")
    except timeout:
        # Handle timeout (packet loss)
        print(f"Request timed out")
        lost_packets += 1

# Calculate and report statistics
if rtt_times:
    min_rtt = min(rtt_times)
    max_rtt = max(rtt_times)
    avg_rtt = sum(rtt_times) / len(rtt_times)
    packet_loss_rate = (lost_packets / N) * 100
    print(f"\nPing statistics:")
    print(f"Minimum RTT: {min_rtt:.6f} seconds")
    print(f"Maximum RTT: {max_rtt:.6f} seconds")
    print(f"Average RTT: {avg_rtt:.6f} seconds")
    print(f"Packet Loss Rate: {packet_loss_rate:.2f}%")

client_socket.close()
