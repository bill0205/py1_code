#使用者输入商品名称
#用清单储存使用者输入的东西
#清单怎么变成二维的，又装商品名又装价格

products = []
while True:
	name = input('请输入商品名称:')
	if name == 'q':
		break
	price = input('请输入产品的价格:')
	#p = []
	#p.append(name)
	#p.append(price)
	#products.append(p)
	products.append([name,price])
print(products)
print(products[0][1])


for p in products:
	print(p)
	print(p[0],'价格是',p[1])
	
