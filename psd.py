#密码重试的程序
#使用者最多重试三次 while
#如果输入正确，印出 登陆成功 break跳出回圈
#如果输入不正确，印出 密码错误!还有_次机会

password = 'a123456'
i = 3 
#while 后面那个判断，true不true
#要提前把值设好
while i >= 1:
	psd = input('请输入密码：')
	if psd == password:  #字符串的相等
		print('登陆成功')
		break     #跳出回圈
	else:
		i = i - 1
		print('密码错误!还有', i, '次机会')
		if i == 1:
			break

#怎么设计三次机会 用while
#剩余0次怎么不打印 break

