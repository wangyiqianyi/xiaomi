# -*- coding:utf-8 -*-
#读取小米账号
import urllib2
import urllib
import cookielib
class Xiaomi:
	'''小米抢购'''
	def __init__(self,filename):
		#读取名为filename的文件
		self.file=open(filename)
		#print(self.file)
	def reader_user(self):
		xmfile=self.file
		print(xmfile)
		for line in xmfile.xreadlines():
			pass
			string=line.lstrip().split('----')
			#print(string)
			if(len(string) != 2):
				print("帐号格式错误，请使用4个-作为分隔符")
			userName=string[0]
			password=string[1]
			self.login(userName,password)
	def login(self,userName,password):
		    #登陆页面,通过抓包工具分析获得，如fiddler
        	login_url="https://account.xiaomi.com/pass/serviceLoginAuth2"
       		try:
        		#得到一个cookieJar实例
        		cj=cookielib.CookieJar()
        		#获得一个opener实例
        		opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        		#伪装成firefox浏览器，
        		opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0')]
        		#生成post数据，包含登录信息
        		data = urllib.urlencode({'passToken':'', 'user': userName, 'pwd': password, 'callback':'https://account.xiaomi.com', 'sid':'passport', 'qs':'%3Fsid%3Dpassport', 'hidden':'', '_sign':'KKkRvCpZoDC+gLdeyOsdMhwV0Xg='})
        		#设置urllib2的全局opener,建议使用open
        		urllib2.install_opener(opener)
        		#data参数传到Request对象
        		req = urllib2.Request(login_url, data)
        		#接受一个request对象，返回一个像文件对象一样的对象
        		op = urllib2.urlopen(req)
        		#读取页面源码
        		html=op.read()
        		#print(html)
        		self.buying()
    		except Exception,e:
        		print str(e)
	def buying(self):
		buy_url="http://www.mi.com/buyphone/mi3"
		try:
			req = urllib2.Request(buy_url)
			op=urllib2.urlopen(req)
			#读取页面代码
			html=op.read()
			print(html)
		except Exception,e:
			print str(e)
		print("成功")
xm=Xiaomi('xiaomi.txt')
xm.reader_user()
