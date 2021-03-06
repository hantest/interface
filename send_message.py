# coding=utf-8
import requests
import json

import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

#
# 发短信接口-0 发送登陆验证码
#

def test_send_message():
	# 接口测试地址url
	url = "https://passport.csdn.net/v1/api/app/sendAppVerifyCode"

	# headers头信息
	headers = {
		"content-Type":"application/json",
		"X-Device-ID":"20180408131945dbdaf50860b94aa0bd80ca3ad5ced7e501e6a8444fd06459",
		"X-App-ID":"CSDN-EDU",
		"X-OS":"Android",
		"X-Access-Token":"bf2addbdc16f7e7178d8bd972333763a"
	}

	# 接口传送的参数
	'''
	type:
	0 发送登录验证码
	1 发送绑定手机验证码
	2 绑定第三方账号验证码
	3 注册第三方账号验证码
	4 手机号+验证码关联第三方账号验证码
	5 绑定用户手机号验证码（第三方根据账号密码关联的时候发现账号没有绑定手机号的情况）
	'''
	data = {

		"mobile":"18811431657",
		"type":"0" #发送登陆验证码
	}

	#发送请求
	r = requests.post(url = url, json = data, headers = headers) 

	print(r.text)  #获取响应报文
	print(r.status_code)

if __name__ == "__main__":
	test_send_message()