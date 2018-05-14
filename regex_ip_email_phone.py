#匹配 手机号码 邮箱 IP

import re

class Match:

	def __init__(self):
		self.phone = re.compile("1[^1269]\d{9}")
		self.email = re.compile("[^\._][\w\._-]+@(?:[A-Za-z0-9]+\.)+[A-Za-z]+$")
		self.ip = re.compile("((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)")

	def is_email(self,email):
		result = self.email.match(email)
		if result:
			return result
		else:
			return False
	def is_phone(self,phone):
		result = self.phone.match(phone)
		if result:
			return result
		else:
			return False
	def is_ip(self,ip):
		result = self.ip.match(ip)
		if result:
			return result
		else:
			return False

match = Match()

# a = input("输入你要匹配的电话：")
# result = match.is_phone(a)
# if result:
# 	print("你输入的电话匹配成功：%s" % result.group())
# else:
# 	print("请输入的电话号码格式不正确")

# e = input("输入你要匹配的邮箱：")
# result = match.is_email(e)
# if result:
# 	print("你输入的邮箱匹配成功：%s" % result.group())
# else:
# 	 print("请输入的邮箱格式不正确")


i = input("输入你要匹配的IP地址：")
result = match.is_ip(i)
if result:
	print("你输入的IP地址匹配成功：%s" % result.group()) 
else:
	 print("请输入的IP格式不正确")