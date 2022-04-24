#做统计计数,两个人说话的字数

def readfile(filename):
	lines = []
	with open(filename,'r') as f:
		for line in f:
			lines.append(line.strip('\n'))
		return lines

def convert(lines):
	zx_word_count = 0
	xcy_word_count = 0
	zx_siticker_count = 0
	xcy_siticker_count = 0
	zx_image_count = 0
	xcy_image_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'zx':
			if '贴图' in line:
				zx_siticker_count += 1
			elif '图片' in line:
				#张心有一行有三个图片怎么识别
				zx_image_count +=1
			else:				
				for n in s[2:]:
					zx_word_count += len(n)
		elif name == 'xcy':
			if '贴图' in line:
				xcy_siticker_count += 1
			else:				
				for n in s[2:]:
					xcy_word_count += len(n)
	print('zx说了',zx_word_count,'传了', zx_siticker_count,'贴图',zx_image_count,'image')
	print('xcy说了',xcy_word_count,'传了', xcy_siticker_count,'贴图')
		#print(s)
#问题：如果一行有几个图片 怎么统计起来
		
def  write_file(filename,lines):
	with open(filename,'w') as f:
		for line in lines:
			f.write(line+ '\n')
	#return filename 不需要回传

def main():
	lines = readfile('line.txt')
	lines = convert(lines)
#	write_file('output.txt',lines)

main()	 #程序的进入点