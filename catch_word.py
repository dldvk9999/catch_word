# -*- coding: cp949 -*- 
from hanspell import spell_checker
from termcolor import *
import colorama
colorama.init()

# ��� ���Ͽ��� �˻�����.
f = open("little prince.txt", "r")
line_number = 0
# ������ �˻�����.
filtering = ["����", "�����彺����", "������ ����", "�߿��ϴٴ�", "��������"]

while True:
	line = f.readline()
	line_number += 1
	if not line: 
		break
	
	result = spell_checker.check(line)
	After_line = result.checked
	After_line_error = result.errors
	if After_line_error:
		print("����� ����")
		print(line_number, "��° Line :", line, end='')
		cprint("-> " + colored(After_line, "white", "on_blue") + "\n")
	
	for i in filtering:
		if i in line:
			index = line.find(i)
			print("������ �߰�")
			print(line_number, "��° Line : ", line[0:index], end='')
			cprint(colored(i, "white", "on_red") + line[index+len(i):] + "\n")

f.close()