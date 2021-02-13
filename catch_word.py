# -*- coding: cp949 -*- 
from hanspell import spell_checker
from termcolor import *
import colorama
colorama.init()

# 어느 파일에서 검색할지.
f = open("little prince.txt", "r")
line_number = 0
# 무엇을 검색할지.
filtering = ["도움", "거추장스럽고", "대항할 무기", "중요하다는", "수수께끼"]

while True:
	line = f.readline()
	line_number += 1
	if not line: 
		break
	
	result = spell_checker.check(line)
	After_line = result.checked
	After_line_error = result.errors
	if After_line_error:
		print("맞춤법 오류")
		print(line_number, "번째 Line :", line, end='')
		cprint("-> " + colored(After_line, "white", "on_blue") + "\n")
	
	for i in filtering:
		if i in line:
			index = line.find(i)
			print("금지어 발견")
			print(line_number, "번째 Line : ", line[0:index], end='')
			cprint(colored(i, "white", "on_red") + line[index+len(i):] + "\n")

f.close()