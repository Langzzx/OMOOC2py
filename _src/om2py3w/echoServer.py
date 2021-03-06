# coding=utf-8
# OMOOC_3
# version 1.1
# ubuntu/lang

import socket
import sys
import os
import diary

#define keyword as CMD
KEYWORDS = ['a', 'l', 'e', 'i']
'''
	Below CMD from client/ and response
	a = show history info and sent back to client;
	l = show newest info sent back to clinet;
	i = show new input input and record to dairy.log
	e = empty the log file
'''

#Based on Client command input process response
def response(data):
	keyword = data[1]
	if keyword == 'a':
		diary.showHistory()
	elif keyword == 'l':
		diary.showLine()
	elif keyword == 'i':
		diary.inputDiary(data[-1])
	elif keyword == 'e':
		diary.emptyDiary()
	else: 
		print "CMD error"


def main():
	
	#initial the diary.log
	# if not exit diary.log, built
	diary.initDiary()
	print "Config done!, connect to Client, waiting CMD input..."
	print "..."
	print ''

	#create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	#Bind the socket to the port
	server_address = ('localhost', 10000)
	print >> sys.stderr, 'starting up on %s port %s' % server_address
	sock.bind(server_address)

	while True:
		print >>sys.stderr, '\nwaiting to receive message'
		data, address = sock.recvfrom(4960)

		if data[0] == "Hello":
			print "Connection! Begin data input\n"
			data = ['Begin']  ## init data to begin flag
			sentCMD = sock.sendto(data, address)	
			print "Waiting CMD input from client"

		data, address = sock.recvfrom(4960)
		#need make sure the input data, NOT affect the data input
		
		if data[1] not in KEYWORDS:
			print "Error input"
			data = "Error" + "无效命令，请输入正确指令：\n", + KEYWORDS
			sent = sendto(data, address)
		else:
			response(data)
			sent = sock.sendto(data, address)
			print >>sys.stderr, 'sent %s bytes back to %s' % (sent, address)

if __name__ == "__main__":
	main()
