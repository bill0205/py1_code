#读取档案
#data = []
#with open('food.txt','r') as f:
	#with 自动close，走到第十一行，自动close
	#只有在with里面框框的部分，档案是打开
	#读取'r' 写入'w' as当作 f档案file
	#把档案food.txt当作f   
#	for line in f:
	#每一行叫line 一行一行读
#		data.append(line.strip())
#print(data)
# 如果这里print(line)是什么结果
#打印出来为什么中间会有空行？
#按enter换行，记事本存\n，读取档案有读到换行符
#怎么去掉换行符？
#.append只能对list做
#.strip()只能对str做，去掉空格 ｜档案读取常用

data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f: 
		#每次读取一行，装进清单
		data.append(line)
		count +=1
		if count % 1000 == 0:
			print(len(data))
			# % 求余数，每1000次计数
		#print命令很花时间
print('档案读取完了，总共有', len(data), '笔资料')
#print(data[0])
#print('---------———----')
#print(data[1])
#print(len(data[0]))

#怎么写程序算这一百万笔留言的平均长度
#提示 用for loop做
#data里面存了一百万笔留言，每笔留言我可以看他的len(data[i])
#所有的len(data[i])加在一起，除以总长度


#错误写法
#num = 0
#for i in len(data):  #一百万笔字串
#	num += len(data[i])
#num = num / len(data)
#int 不能做for loop
#for loop是针对于list做的
sum_len = 0
for d in data: 
	sum_len += len(d)
print('留言的平均长度为', sum_len/len(data))


#对清单做筛选 len(data[i])
#
new = []

for d in data: #d是字串，data是清单
	#for loop 一笔笔读取原始资料
	if len(d) < 100:
		new.append(d)
		#不需要 new = new.append(d)
print('一共有', len(new), '笔留言长度小于100')
print(new[0])