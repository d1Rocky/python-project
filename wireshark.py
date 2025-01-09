

import pyshark

capture = pyshark.FileCapture('your_capture_file.pcap')

# Iterate over packets
for packet in capture:
    print(packet)  # Print basic packet information

# Close the capture file
capture.close()