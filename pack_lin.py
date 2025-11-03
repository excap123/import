import socket, struct

def get_mac(addr):
    return ':'.join(f'{b:02X}' for b in addr)

def ethernet_frame(data):
    dest, src, proto = struct.unpack('!6s6sH', data[:14])
    return get_mac(dest), get_mac(src), socket.htons(proto), data[14:]

def main():
    print("Packet Sniffer started... Press Ctrl+C to stop.\n")

    # Create raw socket to capture all Ethernet frames
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    while True:
        raw_data, _ = s.recvfrom(65536)
        dest, src, proto, _ = ethernet_frame(raw_data)
        print(f"\nEthernet Frame:\nDestination MAC: {dest}\nSource MAC: {src}\nProtocol: {proto}")

main()