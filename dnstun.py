import socket
import sys
#import os
import struct

def dnsserver():
	sock_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock_s.bind(("",53))
	sock_s.listen(5)
	conn,addr = sock_s.accept()
	print "[*]form :",addr
	data = conn.recv(1024)

	print data
	que_header=b"\x01\x01\x84\x80\x01\x01\x00\x00\x00\x01\x00\x00"
	que_que = b"\x05\x6C\x69\x78\x69\x6E\x02\x6D\x65\x00\x00\x01\x00\x01"
	que_res = b"\x01\x01\x01\x00\x00\x00\x00\x00\x01\x02"
	reply = que_header+que_que+que_res
	re_len = len(reply)
	l = struct.pack(">H", re_len) 
	conn.send(l+que_res+"i love you")
	conn.close()
	sock_s.close()



def dnsclient():
	sock_c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock_c.connect(("127.0.0.1",53))
	que_header=b"\x01\x01\x00\x80\x00\x01\x00\x00\x00\x01\x00\x00"
	que_que = b"\x05\x6C\x69\x78\x69\x6E\x02\x6D\x65\x00\x00\x01\x00\x01"
	q = que_header+que_que
	re_len = len(q)
	l = struct.pack(">H", re_len) 
	sock_c.send(l+q)
	print sock_c.recv(1024)
	sock_c.close()

	
def main():
	if len(sys.argv)<2:
		print "[*]args must be specif..."
		sys.exit(1)
	elif sys.argv[1] =="-s":
		dnsserver()
	elif sys.argv[1] =="-c":
		dnsclient()

if __name__ == '__main__':
	main()
