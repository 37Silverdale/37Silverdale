# -*- coding: utf-8 -*-
# 找你算账
# 中国娱乐圈驻伦敦办事处
# Version 3.2
# Copyright © 2018 蔡春瑜. All rights reserved.

import csv
import time

# Initialise global variables

options = '1.宁采臣 2.彭于晏 3.赵又廷 4.蔡因斯坦'
back = '0.返回'

header = ['ning', 'peng', 'zhao', 'cai']
names = ['宁洁','彭燕嘉','赵宏政','蔡春瑜']

ning_debt = {'ning':0., 'peng':0., 'zhao':0., 'cai':0.}

peng_debt = {'ning':0., 'peng':0., 'zhao':0., 'cai':0.}

zhao_debt = {'ning':0., 'peng':0., 'zhao':0., 'cai':0.}

cai_debt = {'ning':0., 'peng':0., 'zhao':0., 'cai':0.}

debts = [ning_debt, peng_debt, zhao_debt, cai_debt]

# Record the performance history

history = open("history.dat", "a", encoding='utf-8')

history.write(time.asctime(time.gmtime(time.time())))
history.write('\n')

# Function for adding record

def add(d = debts, h = history):
	while True:
		print('\n(▰╹◡╹▰)--- 这次是谁付的钱？\n', options, back)
		payer = input('\nᕙ(⇀‸↼‵‵)ᕗ---- ')
		try:
			name_index = int(payer)
		except ValueError:
			print('(눈_눈)---- 你不要乱输入，帅哥！\n')
			continue
		if name_index == 0:
			break
		if name_index < 0 or name_index > 4:
			print('Σ( ⚆൧⚆)---- 你不要乱输入，帅哥！\n')
			continue

		print('\n๐·°(৹˃̵﹏˂̵৹)°·๐-- 替谁付的钱？\n（若是多个人则用英文逗号分隔）\n\n', '0.所有人', options)
		payee = input('\nー( ´ ▽ ` )ﾉ---- ')
		if payee.find('，') != -1:
			print('( •o•) ---- 请用英文逗号，帅哥！\n')
			continue

		string_list = payee.split(',')
		try:
			int_set = {int(i) for i in string_list if int(i) >= 0 and int(i) <=4}
			if 0 in int_set:
				int_set = {1, 2, 3, 4}
		except ValueError:
			print('₍₍ ◟꒰ ‾᷅д̈ ‾᷄ ╬꒱-- 你不要乱输入，帅哥！\n')
			continue

		try:
			total_amount_str = input('\n( ´͈ ᵕ `͈ )◞♡--- 付了多少钱？\n现在已经支持加法输入。若想做减法，请输入“+-”也就是加负数\n━Σ(ﾟДﾟ|||)━---- ')
			amount_list_str = total_amount_str.split('+')
			amount_list = [float(i) for i in amount_list_str]
			amount = sum(amount_list)
		except ValueError:
			print('o(〃▽〃)o-- 你不要乱输入，帅哥！\n')
			continue

		average = amount/len(int_set)
		for n in int_set:
			d[name_index-1][header[n-1]] += average
			hist = '{}替{}付了{}镑\n'.format(names[name_index-1],names[n-1],average)
			h.write(hist)
			continue

# Function to check record

def calculate(d = debts, h = history):
	while True:
		print('ฅ(๑ ̀ㅅ ́๑)ฅ---- 你是谁？\n', options, back)
		try:
			richman = int(input('\nʕ•̀ω•́ʔ✧---- '))
		except ValueError:
			print('₍˄·͈༝·͈˄₎ฅ˒˒---- 你不要乱输入，帅哥！\n')
			continue
		if richman == 0:
			break

		cal = {'宁采臣':0.,'彭于晏':0.,'赵又廷':0.,'蔡康永':0.}
		print(' ˛˛ꉂ ೭(˵¯̴͒ꇴ¯̴͒˵)౨”-- 你分别欠')
		j = 0
		for c in cal.keys():
			cal[c] = debts[j][header[richman-1]] - debts[richman-1][header[j]]
			j += 1
		for name, money in cal.items():
			print('ฅ^•ﻌ•^ฅ----{} {}'.format(name, money))
		print('~(  ~³ω³ )~☍-------------- Pounds\n')

		spend = 0.
		for p in d:
			spend += p[header[richman-1]]
		print('从上次清帐到现在你的总开销是', spend, '镑。\n')

		h.write(names[richman-1])
		h.write('查帐\n')
		continue

# Function to reset record

def clear(d = debts, h = history):
	y = input('꒰●꒡ ̫ ꒡●꒱---- 你确定要清零吗？(y/n) ---- ')
	if y != 'y':
		print('꒰(@｀꒳´)꒱ ---- 那就不清零了～')
		h.write('取消清零\n')
		return

	for i in range(0,4):
		d[i] = d[i].fromkeys(d[i],0.)
	print('\n꒰●꒡ ̫ ꒡●꒱---- 清零成功！')
	h.write('成功清零\n')


# Read data file

readFile = open("data.csv", "r")

debt_reader = csv.DictReader(readFile)

count = 0
for row in debt_reader:
	for name in header:
		debts[count][name] = float(row[name])
	count += 1

readFile.close()

# Read history

def readHistory():
	historyFile = open("history.dat", "r", encoding='utf-8')
	historyReader = historyFile.read()
	print(historyReader)
	historyFile.close()

# Run the system 

while True:
	print('\n(๑¯◡¯๑)-------✧୧(๑=̴̀⌄=̴́๑)૭✧\n')
	print('ε-(=｀ω´=)-- 欢迎来到“找你算账”系统(v3.2)\n')
	print('( ꒪⌓꒪)---- 你想干什么？\n')
	print('ᕦ(･ㅂ･)ᕤ---- 1.记账\nᕦ(･ㅂ･)ᕤ---- 2.查账\nᕦ(･ㅂ･)ᕤ---- 3.查看历史记录\nᕦ(･ㅂ･)ᕤ---- 70.清零\nᕦ(･ㅂ･)ᕤ---- 0.保存并退出')
	print('\n✧(∗≧ꇴ≦)人(≧ꈊ≦∗)✧\n')
	try:
		alt = int(input('(ˊo̴̶̷̤⌄o̴̶̷̤ˋ)---- '))
	except ValueError:
		print('ヽ(ｏ`皿′ｏ)ﾉ你不要乱输入，帅哥！\n')
		continue
	if alt != 1 and alt != 2 and alt != 0 and alt != 70 and alt != 3:
		print('你不要乱输入，帅哥！ヽ(ｏ`皿′ｏ)ﾉ\n')
		continue

	if alt == 1:
		add()
	elif alt == 2:
		calculate()
	elif alt == 3:
		readHistory()
	elif alt == 70:
		clear()
	else:
		break

# Save data file

writeFile = open("data.csv", "w")

debt_writer = csv.DictWriter(writeFile, header)

debt_writer.writeheader()

for debt in debts:
	 debt_writer.writerow(debt)

writeFile.close()

history.close()