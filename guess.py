
#载入import 引入别人写好的功能 ｜模组module
#对比 x=5 一个箱子
#这个箱子已经内置的工具箱，常用工具箱
#standard library标准函数库
#最常用的给你 input print直接给你
#不常用但要用引用
#package套件里面很多个module 
#module就是python档一个又一个



#产生一个1-100的整数
#让使用者重复输入数字去猜 ｜while
#猜对的话 印出 终于猜对了
#猜错了告诉他比答案大或者小 ｜if

import random

r = random.randint(1,50)
#random工具箱里randint随机整数，从1-100中随机产生
#input应该放在哪里
while True:
	num = input('请输入你猜的数字（1-50内）：')
	num = int(num)
	if num == r:
		print('终于猜对答案了')
		break
	elif num > r:
		print('猜错了，比答案大')
	elif num < r:
		print('猜错了，比答案小')
	

