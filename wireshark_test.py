import pyshark

# Load the capture file
capture = pyshark.FileCapture('/Users/eden/Desktop/wireshark_packets/test_capture.pcapng')

print("5 = Top IP Talkers")
user_input = int(input("\nEnter a number: "))

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
