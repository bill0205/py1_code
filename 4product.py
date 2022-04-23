#使用者输入商品名称
#用清单储存使用者输入的东西
#清单怎么变成二维的，又装商品名又装价格


import os #operating system

#读取文档
def read_file(filename):
	products = []
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

#写入文件
def write_file(filename,products):
	with open(filename, 'w', encoding= 'utf-8') as f:
		f.write('商品'+','+'价格'+'\n')
		#写入读取档案设计文档编码utf-8
		#csv档案用','做分隔
		for p in products:
		#因为函数里面没有说products是什么，所以我们要把他变成一个参数，投币孔，投进来
			f.write(p[0]+ ','+ str(p[1])+'\n')  #真正写入f.write
		#加法只能字串跟字串，整数跟整数
		#当p[1]是整数时，需要转换格式
# python 一离开with会自动closed文档



#主要执行的程序也写成程式码
def main():
	filename = 'products.csv'
	#把product.csv存成一个变数filename，所以提到都用filename
	#降低重复性
	if os.path.isfile(filename):	    
		#这个if语句检查档案在不在,不需要重复执行，不用写成函数
		print('yeah！找到档案了')
		products = read_file(filename)
	else:
		print('找不到档案')
	#档名变成参数product.csv
	#回传products
	products = user_input(products)
	#products更新
	#一定要return products，不然product是空的
	print_products(products)
	write_file('products.csv',products)

main() #程序的进入点
#product.csv已经有的不会覆盖，这个程序是往后添加

#func的中心思想只做一件事，单纯。
#怎么设计记账的程序写成func，每一个func只做一家事情
#refactor 重构