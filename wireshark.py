
import pyshark

# Load the capture file
capture = pyshark.FileCapture('/Users/eden/Desktop/wireshark_packets/test_capture.pcapng')

print(("\033[1;4mWireshark File Capture\033[0m"))
print("\n1 = Latency Check")
print("2 = Unsecured Protocols")
print("3 = Large Packet Detector")
print("4 = Failed Handshake Analyzer")
print("5 = DNS Query Extractor")
print("6 = Top IP Talkers")

user_input = int(input("\nEnter a number: "))

if user_input == 1:
    # Ask the user for their latency threshold
    try:
        latency_threshold = float(input("\nEnter the latency threshold in seconds (e.g., 5 for 5 seconds, 0.4 for 400ms): "))
        print(f"\nAnalyzing packets with latency greater than {latency_threshold} seconds...\n")
        
        previous_time = None
        previous_packet_no = None
        
        for packet in capture:
            if hasattr(packet, 'sniff_timestamp'):  # Ensure the packet has a timestamp
                current_time = float(packet.sniff_timestamp)
                if previous_time is not None:
                    latency = current_time - previous_time
                    if latency > latency_threshold:
                        print(f"Packet #{previous_packet_no} -> Packet #{packet.number}: {latency:.2f} seconds")
                previous_time = current_time
                previous_packet_no = packet.number
    except ValueError:
        print("Invalid input! Please enter a valid numeric value for latency threshold.")
        

if user_input == 2:

    print("\nAnalyzing unsecured protocols...\n")
    unsecured_protocols = ['HTTP','TELNET','FTP','RSH','SNMP','POP3','IMAP']

    for packet in capture:
        # Checks if protocols are in packet
        if packet.highest_layer in unsecured_protocols:
            print("Packet Number:", packet.number)
            print("Source Port:", packet.tcp.srcport)
            print("Destination Port:", packet.tcp.dstport)
            print("Protocol:", packet.ip.proto)
            print("Source IP:", packet.ip.src)
            print("Destination Address:", packet.ip.dst + "\n")


# Close the capture file
capture.close()
