#!/usr/bin/env python
# coding=utf-8
import random
import string
# 读入已有验证码 生成新增文件 和新的全部验证码文件
# 重试次数
temp_number = 10
# 获取个数
get_number = 1000
def rander(len=9, num_flag=True, low_flag=False, up_flag=True, special_flag=False):
    num = "0123456789"
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special = "~!@#$%^&*()[]{}_=+-"

    str = ''
    if num_flag:
        str += num
    if low_flag:
        str += lower
    if up_flag:
        str += upper
    if special_flag:
        str += special
    if str == '':
        str = num + lower
    return string.join(random.sample(str, len)).replace(" ", "")


# 获取验证码
def get_code(number=0, code_list=[], diff_list=[]):
	lose_number = 0
	for i in range(number):
		#footer_int = random.randint(1, 9)
		footer_int = rander()
		if footer_int in code_list:
			lose_number += 1
		else:
			code_list.append(footer_int)
			diff_list.append(footer_int)
			# print footer_int
	return lose_number

# 读原始文件
def read_file(code_file, code_list):
	for part in code_file:
		part = part.replace('\n','')
		code_list.append(part)

# 写全部文件
def write_file(write_code_file, code_list):
	for code in code_list:
		write_code_file.write(code+'\n')
	write_code_file.close()

# 写新增文件
def diff_file(diff_code_file, diff_list):
	for code in diff_list:
		diff_code_file.write(code+'\n')
	diff_code_file.close()
	
	
def main():
	
	global temp_number
	code_file = open('code_number.txt','r')
	write_code_file = open('code_number_all.txt','w+')
	diff_code_file = open('code_number_new.txt','w+')
	code_list = []
	diff_list = []
	read_file(code_file, code_list)

	lose_number = get_code(get_number, code_list=code_list, diff_list=diff_list)
	while(lose_number and temp_number):
		lose_number =  get_code(lose_number, code_list=code_list, diff_list=diff_list)
		temp_number -=1
	
	if temp_number == 0 :
		print "number is not enough"
	write_file(write_code_file, code_list)
	diff_file(diff_code_file, diff_list)


if  __name__ == '__main__':
	main()
