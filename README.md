# python-project

Network Analysis Tool

this project is a Python-based tool designed to analyze network packets capture in Wireshark using .pcap or .pcaphg file. Using the pyshark library, the script provides five main features to help understand and analyze network activity. The tool is menu-driven, so you can choose what you want to do by entering a number. Below is a quick overview of the features and how to use them.


1. Latency Check

- Analyzes packet timestamps to detect delays between consecutive packets.
- You can set a latency threshold, and the script will find packets with delays exceeding that value.

2. Unsecured Protocols

- Checks for packets that use unsecured protocols like HTTP, FTP, Telnet etc.
- Displays the source and destination information for packets using these protocols.

3. Large Packet Detector

- Identifies packets that are larger than a specified size.
- You set the size threshold (in bytes), and the script lists packets exceeding it.

4. DNS Query Extractor

- Extracts and displays domain names from DNS query packets.

5. Top IP Talkers

- Finds the most frequent communication pair (source and destination IPs) in the capture file.


P.S.

For large files, the script might take time to process all packets so be aware. 

Feel free to use my code whether it is for studying python or learn more about Wireshark and how it works. I worked really hard to make this project and I am really proud it!