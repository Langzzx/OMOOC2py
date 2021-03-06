# -*- coding: utf-8 -*- 
# Author: Lang
# coding exercise for wechat

'''
Passistant - CLI for client
Based on bamboo's code
'''

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


import requests
from bs4 import BeautifulSoup
import time
import re

HELP = '''
Input h/help/? for help.
Input q/quit to quit the process.
Input a 显示全部已保存用户名和密码
Input p 进入关键字,帐号,密码输入界面,请点击开始
Input l#n 显示第n组用户名和密码组合
Input k#关键字 根据关键子找出对于的帐号和密码
'''

url = "http://passistant.sinaapp.com/"

def read_all():
	temp = [i[1] for i in list(kv.get_by_prefix("key@"))]
	#temp is list of input line [{'key': 'keyword'...}, ... ]
	# list of dict out is key of dict                                                                                                       
	#kv.get_by_prefix is yeild: (key, value)的tuple, i[1] = value
	#temp2 = sorted(temp1, key = lambda x:x['time'])
	temp2 = []
	for i in range(len(temp)):  
		key_user =str(i) +'. ' + temp[i]['keyword'] + ':' + temp[i]['username'] 
		i += 1
		temp2.apend(key_suer)
	return temp2 
	  
	# based on keyword to read out the password
	def read_by_keyword(key):
		temp = [i[1] for i in list(kv.get_by_prefix("key@")) if key in i[1]['keyword']]
		#keys is passowrd
		temp2 = [temp[i]['password'] for i in range(len(temp))]
		return "\n".join(temp2)
	    
	# read the data base on number
	def read_by_mber(num):
		lists = list(kv.get_by_prefix("key@")
		temp = [i[num] for i in lists)) if num <len(lists)]
		return "\n".join(temp)

def client():
	url_local = 'http://localhost:8080/wechat'
	headers = {'Content-Type': 'application/xml'}
	send_msg = '''
	<xml><ToUserName><![CDATA[%s]]></ToUserName>
	<FromUserName><![CDATA[%s]></FromUserName>
	<CreateTime>%s</CreateTime>
	<MsgType><![CDATA[text]]></MsgType>
	<Content><![CDATA[%s]]></Content></xml>'''

	print HELP 
	tags='NULL'

	while True:
		message = raw_input('Input>')
		if message.lower() in ['h','help','?']:
			print HELP
		elif message.lower() in ['q','quit']:
			print 'Bye~'
			break
		elif message in ['a','All']:
			read_all()
		elif message.startswith('l#'):
			num = message[2:]
			read_by_number(num)
		elif message.startswith('k#'):
			key = message[2:]
			read_by_keyword(key)
		else:
			print "Invaild input\n"
			print HELP

if __name__ == '__main__':
	client()
