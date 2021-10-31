# 產生一個隨機整數1~100(不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話印出 “終於答對了！”
# 猜錯的話 要告訴他 比答案大/小
# 給出一個範圍

import random
start = int(input('請輸入最小範圍:'))
end = int(input('請輸入最大範圍:'))
r = random.randint(start, end) 

count = 0
while True:
	count += 1 # count = count + 1
	answer =  int(input ('number:'))
	if r == answer:
		print ('答對了')
		print ('猜了', count, '次')
		break 
	elif r > answer:
		print('比答案小')
	elif r < answer:
		print('比答案大')
	print ('猜了', count, '次')


