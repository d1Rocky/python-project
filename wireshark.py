

import pyshark

capture = pyshark.FileCapture('/Users/eden/Desktop/wireshark_packets/test_capture.pcapng')

# Iterate over packets
for packet in capture:
    print(packet)  # Print basic packet information

# Close the capture file
capture.close()