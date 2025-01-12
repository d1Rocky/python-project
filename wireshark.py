
import pyshark

# Load the capture file
capture = pyshark.FileCapture('/Users/eden/Desktop/wireshark_packets/test_capture.pcapng')

print(("\033[1;4mWireshark File Capture\033[0m"))
print("\n1 = Latency Check")
print("2 = Unsecured Protocols")
print("3 = Large Packet Detector")
print("4 = DNS Query Extractor")
print("5 = Failed Handshake Analyzer")
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
            # Check if the packet has a 'sniff_timestamp' attribut
            if hasattr(packet, 'sniff_timestamp'):
                current_time = float(packet.sniff_timestamp)
                if previous_time is not None:
                    latency = current_time - previous_time
                    if latency > latency_threshold:
                        print(f"Packet #{previous_packet_no} -> Packet #{packet.number}: {latency:.2f} seconds")
                # Update the previous packet's details with the current packet's details
                previous_time = current_time
                previous_packet_no = packet.number
    except ValueError:
        print("Invalid input! Please enter a valid numeric value for latency threshold.")
        

if user_input == 2:

    print("\nAnalyzing unsecured protocols...\n")
    # Define a list of unsecured protocols
    unsecured_protocols = ['HTTP','TELNET','FTP','RSH','SNMP','POP3','IMAP']

    for packet in capture:
        # Check if the highest layer of the packet matches any unsecured protocol
        if packet.highest_layer in unsecured_protocols:
            print("Packet Number:", packet.number)
            print("Source Port:", packet.tcp.srcport)
            print("Destination Port:", packet.tcp.dstport)
            print("Protocol:", packet.ip.proto)
            print("Source IP:", packet.ip.src)
            print("Destination Address:", packet.ip.dst + "\n")
    # Checks if packet highest layer is not finding matches to unsecured protocols within packet file
    if packet.highest_layer is not unsecured_protocols:
        print("\033[1mUnsecured protocol was not found!\033[0m")


if user_input == 3:

    while True:
        try:
            # Prompt the user to enter a size threshold
            large_packet = int(input("\nEnter the packet size threshold in bytes(e.g., 1500 will be 1500 bytes): "))
            print(f"\nAnalyzing large packets that are bigger or equal to {large_packet} bytes...\n")
        
            for packet in capture:
                # Check if the packet object has the 'length' attribute
                if hasattr(packet, 'length'):
                    # Convert the packet length to an integer
                    current_size = int(packet.length)
                    # Compare the packet size with the user-defined threshold
                    if current_size >= large_packet:
                        print("\nPacket #" + packet.number)
                        print("Packet size: " + str(current_size))
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




# Close the capture file
capture.close()
