
import pyshark

# Load the capture file
capture = pyshark.FileCapture('/Users/eden/Desktop/wireshark_packets/test_capture.pcapng')

print(("\033[1;4mWireshark File Capture\033[0m"))
print("\n1 = Latency Check")
print("2 = Unsecured Protocols")
print("3 = Large Packet Detector")
print("4 = DNS Query Extractor")
print("5 = Top IP Talkers")

user_input = int(input("\nEnter a number: "))

if user_input == 1:
    # Ask the user for their latency threshold
    while True:
        try:
            latency_threshold = float(input("\nEnter the latency threshold in seconds (e.g., 5 for 5 seconds, 0.4 for 400ms): "))
            print(f"\nAnalyzing packets with latency greater than {latency_threshold} seconds...\n")
        
            previous_time = None
            previous_packet_no = None
            latency_found = False
        
            for packet in capture:
                # Check if the packet has a 'sniff_timestamp' attribut
                if hasattr(packet, 'sniff_timestamp'):
                    current_time = float(packet.sniff_timestamp)
                    if previous_time is not None:
                        latency = current_time - previous_time
                        if latency > latency_threshold:
                            latency_found = True
                            print(f"Packet #{previous_packet_no} -> Packet #{packet.number}: {latency:.2f} seconds")
                    # Update the previous packet's details with the current packet's details
                    previous_time = current_time
                    previous_packet_no = packet.number

            if not latency_found:
                print(f"No packets found with latency greater than {latency_threshold} seconds.")
                print("Please enter a smaller threshold value.")
            else:
                break

        except ValueError:
            print("Invalid input! Please enter a valid numeric value for latency threshold.")
        

if user_input == 2:

    print("\nAnalyzing unsecured protocols...\n")
    # Define a list of unsecured protocols
    unsecured_protocols = ['HTTP','TELNET','FTP','RSH','SNMP','POP3','IMAP']

    unsecured_found = False

    for packet in capture:
        # Check if the highest layer of the packet matches any unsecured protocol
        if packet.highest_layer in unsecured_protocols:
            unsecured_found = True
            print("Packet Number:", packet.number)
            print("Source Port:", packet.tcp.srcport)
            print("Destination Port:", packet.tcp.dstport)
            print("Protocol:", packet.ip.proto)
            print("Source IP:", packet.ip.src)
            print("Destination Address:", packet.ip.dst + "\n")
    # Checks if packet highest layer is not finding matches to unsecured protocols within packet file
    if not unsecured_found:
        print("\033[1mUnsecured protocol was not found!\033[0m")


if user_input == 3:

    while True:
        try:
            # Prompt the user to enter a size threshold
            large_packet = int(input("\nEnter the packet size threshold in bytes(e.g., 1500 will be 1500 bytes): "))
            print(f"\nAnalyzing large packets that are bigger or equal to {large_packet} bytes...\n")
            packet_found = False

            for packet in capture:
                # Check if the packet object has the 'length' attribute
                if hasattr(packet, 'length'):
                    # Convert the packet length to an integer
                    current_size = int(packet.length)
                    # Compare the packet size with the user-defined threshold
                    if current_size >= large_packet:
                        packet_found = True
                        print("\nPacket #" + packet.number)
                        print("Packet size: " + str(current_size))

            if not packet_found:
                print(f"No packets found with size >= {large_packet} bytes. Please try a smaller number.")
            else:
                break
            
        except ValueError:
            print("\n\033[1mError! Please provide a whole number.\033[0m")


if user_input == 4:
    print("\nAnalyzing packets with Domain Name Server...\n")
    
    def extract_domain_name(packet):
        try:
            # Check if the packet has a DNS layer and the 'qry_name' attribute
            if hasattr(packet.dns, 'qry_name'):
                # Extract and return the DNS query name
                return packet.dns.qry_name
        except AttributeError:
            # Ignore packets without a DNS query name
            pass

    # Loop through packets to extract DNS query names
    for packet in capture:
        # Attempt to extract the domain name from the current packet
        domain_name = extract_domain_name(packet)
        # If a domain name was found, print it
        if domain_name:
            print(f"Domain Name: {domain_name} | Packet #{packet.number}")


if user_input == 5:

    print("\nAnalyzing for top IP talkers...\n")

    pairs = {}  # Dictionary to count communication pairs

    for packet in capture:
        if hasattr(packet, 'ip'):
            src = packet.ip.src
            dst = packet.ip.dst
            pair = (src, dst)

            # Checks for count if both src and dst show in the same packet
            if pair in pairs:
                pairs[pair] += 1
            else:
                pairs[pair] = 1

    # Find the pair with the maximum count
    max_pair = max(pairs, key=pairs.get)
    max_count = pairs[max_pair]

    print(f"Source IP: {max_pair[0]} Destination IP: {max_pair[1]} - {max_count} times")

# Close the capture file
capture.close()
