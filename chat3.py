
lines = []
with open('line2.txt','r') as f:
	for line in f:
		lines.append(line.strip().split(' '))
	print(lines)

for line in lines:
	time = line[0][:5]
	name = line[0][5:]	
	print(time,name)
#字串的某一段取出来，清单分割
#时间的部分 前五个字符 长度固定
#s[0][:5]