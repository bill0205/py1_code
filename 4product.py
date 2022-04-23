#使用者输入商品名称
#用清单储存使用者输入的东西
#清单怎么变成二维的，又装商品名又装价格


import os #operating system
#读取档案，检查档案是否存在
def read_file(filename):
	products = []
	if os.path.isfile(filename):
		#只要查得到的都不用背
		print('yeah!找到档案了')
		with open(filename,'r',encoding= 'utf-8') as f:
			for line in f:
				if '商品' in line:
					# '商品，价格' in line 不ok
					continue #跳到下一回
					#使用continue常常和for loop
					#什么情况我跳过这个回合
				name,price = line.strip().split(',')
				#print(name)
				products.append([name,price])
		print(products)
			#split切割标准
			#strip()去换行+空格 记得每一行有换行的符号
	else:
		print('找不到档案...')
	return products


#让使用者输入
def user_input(products):
	while True:
		name = input('请输入商品名称:')
		if name == 'q':
			break
		price = input('请输入产品的价格:')
		price = int(price)
		#p = []
		#p.append(name)
		#p.append(price)
		#products.append(p)
		products.append([name,price])
		#把products变成参数传递进来，不然要伸手去外面拿
	print(products)
	return products
	#print(products[0][1])



#把商品价格印出 ｜购买记录
def print_products(products):
	#加入参数products，这个函数才知道products是什么
	for p in products:
		#print(p)
		print(p[0],'价格是',p[1])
		#只是一个打印，印出东西，所以不需要回传


#写入档案
#w 写入模式 有没有档案不重要 有的话会覆盖掉 没的话会搞出来，写入
#不同的属性的数据常常存取csv，excel数据
#csv档案用','做分隔
def write_file(filename,products):
	with open(filename, 'w', encoding= 'utf-8') as f:
		f.write('商品'+','+'价格'+'\n')
		#写入读取档案设计文档编码utf-8
		for p in products:
		#因为函数里面没有说products是什么，所以我们要把他变成一个参数，投币孔，投进来
			f.write(p[0]+ ','+ str(p[1])+'\n')  #真正写入f.write
		#加法只能字串跟字串，整数跟整数
		#当p[1]是整数时，需要转换格式
# python 一离开with会自动closed文档


products = read_file('product.csv')
#档名变成参数product.csv
#回传products
products = user_input(products)
#products更新
#一定要return products，不然product是空的
print_products(products)
write_file('products.csv',products)


#func的中心思想只做一件事，单纯