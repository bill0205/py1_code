#liaotian
#读取input档，产生output档
#提示 可能用到continue

#把最常用的做法给大家展示出来看，你以前没见过很难想到

def readfile(filename):
	lines = []
	with open(filename,'r') as f:
		for line in f:
			lines.append(line.strip('\n'))
		return lines

def convert(lines):
	new = []
	person = None
	for line in lines:
		if 'allen' in line: 
			#if line == allen
			person = 'allen'
			continue
		elif 'tom' in line:
			person = 'tom'
			continue
		if person: #如果person有值才做
			new.append(person+ ':'+ line)
		#如果第一行不是人名，会down掉
		#在for loop外面先宣告预设值 peeson =
	return new

def  write_file(filename,lines):
	with open(filename,'w') as f:
		for line in lines:
			f.write(line+ '\n')
	#return filename 不需要回传

def main():
	lines = readfile('input.txt')
	lines = convert(lines)
	write_file('output.txt',lines)

main()	


#with open('output.txt','w') as f:
#	f.write()