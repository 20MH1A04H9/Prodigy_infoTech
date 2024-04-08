import pyshark

capture = pyshark.LiveCapture(display_filter='ip.addr == 192.168.1.6')

capture.set_debug()

capture.sniff(timeout=50)

for packet in capture:
    print(packet)

capture.close()