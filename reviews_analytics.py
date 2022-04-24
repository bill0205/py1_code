

import time #引入内建模组
import progressbar
#下载安装第三方的模组,要写class，创造资料类别type


#不会把txt文件上传到git，360mb太大，git上限150
data = []
count = 0
bar = progressbar.ProgressBar(maxval=10000000000) 
bar.start()
with open('reviews.txt','r') as f:
	for line in f: 
		#每次读取一行，装进清单
		data.append(line)
		count += 1
		bar.update(count)
		#if count % 1000 == 0:
		#	print(len(data))
bar.finish()
print('档案读取结束，一共有',len(data),'笔资料')

#new = []
#for d in data:
#	if len(d) < 100:
#		new.append(d)
#print('一共有',len(new),'留言长度小于100')


#good = []
#for d in data:
#	if 'good' in d:
#		good.append(d)
#print('一共有',len(good),'提到good')

#查找一个词出现过多少次 字典 key字 value次数
#这部分很关键！！！ 如何做计数，字典的结构
start_time = time.time()
wc = {} #word_count
for d in data: #d字串 data列表
	words = d.split() #默认所有空格跳过
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增key进字典

for word in wc:
	if wc[word] > 1000000:
		print(word,wc[word])
end_time = time.time()
print('一共花了',end_time - start_time,'秒')
print(len(wc))
print(wc['bill']) 

while True:
	word = input('请问你想查什么名字')
	if word == 'q':
		break
	elif word in wc:
		print(word,'出现过的次数为',wc[word])
	else:
		print('这个字没有出现过')
print('感谢使用本查询功能')

#print(wc)
	#print(words)
	#break







