import socket, struct

def get_mac(addr):
    return ':'.join(f'{b:02X}' for b in addr)

def ethernet_frame(data):
    dest, src, proto = struct.unpack('!6s6s2s', data[:14])
    proto = ''.join(f'{b:02X}' for b in proto)
    return get_mac(dest), get_mac(src), proto, data[14:]

def main():
    host = socket.gethostbyname(socket.gethostname())
    print(f"IP: {host}")

    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    s.bind((host, 0))
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    while True:
        raw_data, _ = s.recvfrom(65536)
        dest, src, proto, _ = ethernet_frame(raw_data)
        print(f"\nEthernet Frame:\nDestination MAC: {dest}\nSource MAC: {src}\nProtocol: {proto}")

main()