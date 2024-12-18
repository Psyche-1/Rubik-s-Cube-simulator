"""
Записать краткий конспект основных
свойств и функций, чтобы выбрать 
как проще обрабатывать
"""

"""	ЧТО ДОБАВИТЬ:

"""

#! python3

import re, os, shelve
#import graphics as gr #??



"""
#	РАБОТА СО СТРОКАМИ И СПИСКАМИ
#"""

wherefrom_string = 'Из файла: '


def check_string(main_string):
	'''
	Проверка подходит ли строка для вращения кубика
	потом какая строка: из калькулятора или из блокнота.
	Вывод её в удобном виде и для подачи на вращения кубика
	'''
	''' #?
	Возможно добавить после проверки через regex
	if содержит, что-то чего нет в словаре:
		print('Строка не подходит для вращения кубика')
		input('Попробуйте другую строку:\n')
		
	else:
		print()#то это нужная строка#Launch(запуск)
	'''
	global wherefrom_string
	
	string_regex = re.compile(r"[^a-i k-u w A-I K-U W()\^' 2]")
	mo = string_regex.search(main_string)
	if mo != None:
		print('Строка не подходит для вращения кубика')
		input('Попробуйте другую строку:\n')
	else:
		print('')

	main_string = main_string.strip('()')
	main_string = main_string.rstrip(' ')
	if 'I' in main_string:
		wherefrom_string = 'Из калькулятора: '
		print(wherefrom_string, end = '\n\n')
		
		main_string = return_rubiks_cube(main_string, 1)
		main_string = main_string.strip()
	else:
		wherefrom_string = 'Из блокнота: '
		print(wherefrom_string, end = '\n\n')
	print(main_string, end = '\n\n')
	turn_list = main_string.split(' ')
	print(str(turn_list))
	return turn_list

def reverse_and_apostrophe(main_string):
	main_string.reverse()
	for i in range(len(main_string) - 1):
		if "'" in main_string[i]:
			#убрать апостроф 
			main_string[i] = main_string[i].replace("'", '')
		elif '2' not in main_string[i]:
			#добавить апостоф
			main_string[i] = main_string[i] + "'"
	return(main_string)

def return_rubiks_cube(main_string, step):
	'''
	Получает строчку из графического калькулятора
	и возвращает строку которая будет обратной,
	то есть справа на лево и штрих убирает,
	если есть или добавляет если нет и нет 2, ещё убирает скобки
	'''
	main_string = main_string.strip('()')
	main_string = main_string.split('I')
	for i in range(len(main_string) - 1):
		main_string[i] = main_string[i].replace('^', '')
		#main_string[i] = main_string[i].upper()
	if step == 2:
		main_string = reverse_and_apostrophe(main_string)
	main_string = ' '.join(main_string)
	return(main_string)



'''	ПЕРЕПИСАТЬ string to list НОРМАЛЬНО!!!''' #???
def string_to_list(super_cube):
	'''
	из строки super_cube
	делает cube_list 
	'''
	super_cube = super_cube.replace('_', '')
	super_cube = super_cube.replace('\n', '')
	super_cube = super_cube.replace(' ', '')
	cube_list2 = super_cube.split('·')
	
	# Убирает пустые, ПРИДУМАТЬ КАК ЛУЧШЕ #???
	for i in range(len(cube_list2) - 23):
		if cube_list2[i] == '':
			del cube_list2[i]
	
	for i in range(len(cube_list2) - 10):
		if cube_list2[i] == '':
			del cube_list2[i]
	
	for i in range(len(cube_list2) - 3):
		if cube_list2[i] == '':
			del cube_list2[i]

	# [0,1,2,3,4,5,6,7,8]
	cube_list3 = [[9,9,9,9,9,9,9,9,9],[9,9,9,9,9,9,9,9,9],[9,9,9,9,9,9,9,9,9],[9,9,9,9,9,9,9,9,9],[9,9,9,9,9,9,9,9,9],[9,9,9,9,9,9,9,9,9]]
	
	for side in range(len(cube_list3)):
		if str(side) in '045':
			side_cube_list2 = cube_list2[3*side] + cube_list2[3*side + 1] + cube_list2[3*side + 2]
			for square in range(9):
				cube_list3[side][square] = side_cube_list2[square]
				
		if str(side) in '123':
			for square in range(9):
				i = square
				if str(i) in '012':
					cube_list3[side][square] = cube_list2[side + 2][i]
				if str(i) in '345':
					cube_list3[side][square] = cube_list2[side + 5][i - 3]
				if str(i) in '678':
					cube_list3[side][square] = cube_list2[side + 8][i - 6]

	#print(str(cube_list3) + '  cube_list3')
	return cube_list3


'''	ПЕРЕПИСАТЬ list to string НОРМАЛЬНО!!!''' #???
def list_to_string(cube_list):
	'''
	из списка cube_list
	делает super_cube 
	'''
	super_cube = ('\n' +
	'    ·___·' +  cube_list[0][0] + cube_list[0][1] + cube_list[0][2] + '·___·' + '\n' +
	'    ·___·' +  cube_list[0][3] + cube_list[0][4] + cube_list[0][5] + '·___·' + '\n' + 
	'    ·___·' +  cube_list[0][6] + cube_list[0][7] + cube_list[0][8] + '·___·' + '\n' +
	'    ·___     ___·' + '\n' +
	'    ·' + cube_list[1][0] + cube_list[1][1] + cube_list[1][2] + '·' +
	cube_list[2][0] + cube_list[2][1] + cube_list[2][2] + '·' +
	cube_list[3][0] + cube_list[3][1] + cube_list[3][2] + '·' +
	'\n' +
	'    ·' + cube_list[1][3] + cube_list[1][4] + cube_list[1][5] + '·' +
	cube_list[2][3] + cube_list[2][4] + cube_list[2][5] + '·' +
	cube_list[3][3] + cube_list[3][4] + cube_list[3][5] + '·' +
	'\n' +
	'    ·' + cube_list[1][6] + cube_list[1][7] + cube_list[1][8] + '·' +
	cube_list[2][6] + cube_list[2][7] + cube_list[2][8] + '·' +
	cube_list[3][6] + cube_list[3][7] + cube_list[3][8] + '·' +
	'\n' + '    ·___     ___·' + '\n' +
	'    ·___·' +  cube_list[4][0] + cube_list[4][1] + cube_list[4][2] + '·___·' + '\n' +
	'    ·___·' +  cube_list[4][3] + cube_list[4][4] + cube_list[4][5] + '·___·' + '\n' + 
	'    ·___·' +  cube_list[4][6] + cube_list[4][7] + cube_list[4][8] + '·___·' + '\n' +
	'    ·___     ___·' + '\n' +
	'    ·___·' +  cube_list[5][0] + cube_list[5][1] + cube_list[5][2] + '·___·' + '\n' +
	'    ·___·' +  cube_list[5][3] + cube_list[5][4] + cube_list[5][5] + '·___·' + '\n' + 
	'    ·___·' +  cube_list[5][6] + cube_list[5][7] + cube_list[5][8] + '·___·' + '\n'
	)
	return super_cube

def coloring(cube_list):
	'''
	Меняет короткие названия цветов на полные
	'''
	colors = {'y': 'yellow', 'o': 'orange', 'b': 'blue', 'r': 'red', 'w': 'white','g': 'green'}

	for side in range(len(cube_list)):
		for square in range(len(cube_list[side])):
			color = cube_list[side][square]
			if color in colors:
				cube_list[side][square] = colors.get(color, ' ')

	#print(cube_list)
	return cube_list


def find_different(cube_1, cube_2):
	'''
	находит и выводит разницу между 
	двумя кубиками до и после вращения
	'''
	if str(type(cube_1)) == "<class 'list'>" and str(type(cube_2)) == "<class 'list'>":
		if string_to_list(list_to_string(cube_1)) == string_to_list(list_to_string(cube_2)):
			print('Cube 1 = Cube 2')
		else:
			print('				Cube 1 no = Cube 2\n')
			print('Cube 1: ' + '\n\n' +  str(cube_1) + '\n\n\n' +  'Cube 2: ' + '\n\n' +  str(cube_2))
	elif str(type(cube_1)) == "<class 'list'>" and str(type(cube_2)) == "<class 'str'>":
		if string_to_list(list_to_string(cube_1)) == string_to_list(cube_2):
			print('Cube 1 = Cube 2')
		else:
			print('				Cube 1 no = Cube 2\n')
			print('Cube 1: ' + '\n\n' +  str(cube_1) + '\n\n\n' +  'Cube 2: ' + '\n\n' +  str(cube_2))
	elif str(type(cube_1)) == "<class 'str'>" and str(type(cube_2)) == "<class 'list'>":
		if string_to_list(cube_1) == string_to_list(list_to_string(cube_2)):
			print('Cube 1 = Cube 2')
		else:
			print('				Cube 1 no = Cube 2\n')
			print('Cube 1: ' + '\n\n' +  str(cube_1) + '\n\n\n' +  'Cube 2: ' + '\n\n' +  str(cube_2))
	elif str(type(cube_1)) == "<class 'str'>" and str(type(cube_2)) == "<class 'str'>":
		if string_to_list(cube_1) == string_to_list(cube_2):
			print('Cube 1 = Cube 2')
		else:
			print('				Cube 1 no = Cube 2\n')
			print('Cube 1: ' + '\n\n' +  str(cube_1) + '\n\n\n' +  'Cube 2: ' + '\n\n' +  str(cube_2))
	else:
		print('Cube 1 or Cube 2 is not string or list')
		print('Cube 1: ' + '\n\n' +  str(cube_1) + '\n\n\n' +  'Cube 2: ' + '\n\n' +  str(cube_2))
#"""


"""
#	ВРАЩЕНИЕ КУБИКА
#"""

def UP(cube, sign):
	def up1(cube):
		#print('up1')
		t1, t2, t3						   = cube[1][2], cube[1][5], cube[1][8]		#бока up1
		cube[1][2], cube[1][5], cube[1][8] = cube[2][0], cube[2][1], cube[2][2]
		cube[2][0], cube[2][1], cube[2][2] = cube[3][0], cube[3][3], cube[3][6]
		cube[3][0], cube[3][3], cube[3][6] = cube[5][0], cube[5][1], cube[5][2]
		cube[5][0], cube[5][1], cube[5][2] = t1, t2, t3
		
		t1, t2, t3						   = cube[0][0], cube[0][1], cube[0][2]		#сама сторона up1
		cube[0][0], cube[0][1], cube[0][2] = cube[0][6], cube[0][3], cube[0][0]
		cube[0][6], cube[0][3], cube[0][0] = cube[0][8], cube[0][7], cube[0][6]
		cube[0][8], cube[0][7], cube[0][6] = cube[0][2], cube[0][5], cube[0][8]
		cube[0][2], cube[0][5], cube[0][8] = t1, t2, t3
		
	def up2(cube):
		#print('up2')
		up1(cube)
		up1(cube)

	def up·1(cube):
		#print('up-1')
		t1, t2, t3						   = cube[5][0], cube[5][1], cube[5][2]		#бока up-1
		cube[5][0], cube[5][1], cube[5][2] = cube[3][0], cube[3][3], cube[3][6]
		cube[3][0], cube[3][3], cube[3][6] = cube[2][0], cube[2][1], cube[2][2]
		cube[2][0], cube[2][1], cube[2][2] = cube[1][2], cube[1][5], cube[1][8]
		cube[1][2], cube[1][5], cube[1][8] = t1, t2, t3
		
		t1, t2, t3						   = cube[0][2], cube[0][5], cube[0][8]		#сама сторона up-1
		cube[0][2], cube[0][5], cube[0][8] = cube[0][8], cube[0][7], cube[0][6]
		cube[0][8], cube[0][7], cube[0][6] = cube[0][6], cube[0][3], cube[0][0]
		cube[0][6], cube[0][3], cube[0][0] = cube[0][0], cube[0][1], cube[0][2]
		cube[0][0], cube[0][1], cube[0][2] = t1, t2, t3

	if sign == "'":
		up·1(cube)
	elif sign == '2':
		up2(cube)
	elif sign == '':
		up1(cube)
	else:
		print('sign error')


def FRONT(cube, sign):
	def front1(cube):
		#print('front1')
		t1, t2, t3						   = cube[0][6], cube[0][7], cube[0][8]		#бока front1
		cube[0][6], cube[0][7], cube[0][8] = cube[1][6], cube[1][7], cube[1][8]
		cube[1][6], cube[1][7], cube[1][8] = cube[4][0], cube[4][1], cube[4][2]
		cube[4][0], cube[4][1], cube[4][2] = cube[3][6], cube[3][7], cube[3][8]
		cube[3][6], cube[3][7], cube[3][8] = t1, t2, t3

		t1, t2, t3						   = cube[2][0], cube[2][1], cube[2][2]		#сама сторона front1
		cube[2][0], cube[2][1], cube[2][2] = cube[2][6], cube[2][3], cube[2][0]
		cube[2][6], cube[2][3], cube[2][0] = cube[2][8], cube[2][7], cube[2][6]
		cube[2][8], cube[2][7], cube[2][6] = cube[2][2], cube[2][5], cube[2][8]
		cube[2][2], cube[2][5], cube[2][8] = t1, t2, t3

	def front2(cube):
		#print('front2')
		front1(cube)
		front1(cube)

	def front·1(cube):
		#print('front-1')
		t1, t2, t3						   = cube[3][6], cube[3][7], cube[3][8]		#бока front-1
		cube[3][6], cube[3][7], cube[3][8] = cube[4][0], cube[4][1], cube[4][2]
		cube[4][0], cube[4][1], cube[4][2] = cube[1][6], cube[1][7], cube[1][8]
		cube[1][6], cube[1][7], cube[1][8] = cube[0][6], cube[0][7], cube[0][8]
		cube[0][6], cube[0][7], cube[0][8] = t1, t2, t3

		t1, t2, t3						   = cube[2][2], cube[2][5], cube[2][8]		#сама сторона front-1
		cube[2][2], cube[2][5], cube[2][8] = cube[2][8], cube[2][7], cube[2][6]
		cube[2][8], cube[2][7], cube[2][6] = cube[2][6], cube[2][3], cube[2][0]
		cube[2][6], cube[2][3], cube[2][0] = cube[2][2], cube[2][1], cube[2][2]
		cube[2][0], cube[2][1], cube[2][2] = t1, t2, t3

	if sign == "'":
		front·1(cube)
	elif sign == '2':
		front2(cube)
	elif sign == '':
		front1(cube)
	else:
		print('sign error')


def RIGHT(cube, sign):
	def right1(cube):
		#print('right1')
		t1, t2, t3						   = cube[0][2], cube[0][5], cube[0][8]		#бока right1
		cube[0][2], cube[0][5], cube[0][8] = cube[2][2], cube[2][5], cube[2][8]
		cube[2][2], cube[2][5], cube[2][8] = cube[4][2], cube[4][5], cube[4][8]
		cube[4][2], cube[4][5], cube[4][8] = cube[5][2], cube[5][5], cube[5][8]
		cube[5][2], cube[5][5], cube[5][8] = t1, t2, t3
		
		t1, t2, t3						   = cube[3][0], cube[3][1], cube[3][2]		#сама сторона right1
		cube[3][0], cube[3][1], cube[3][3] = cube[3][6], cube[3][3], cube[3][0]
		cube[3][6], cube[3][3], cube[3][0] = cube[3][8], cube[3][7], cube[3][6]
		cube[3][8], cube[3][7], cube[3][6] = cube[3][2], cube[3][5], cube[3][8]
		cube[3][2], cube[3][5], cube[3][8] = t1, t2, t3

	def right2(cube):
		#print('right2')
		right1(cube)
		right1(cube)

	def right·1(cube):
		#print('right-1')
		t1, t2, t3						   = cube[5][2], cube[5][5], cube[5][8]		#бока right-1
		cube[5][2], cube[5][5], cube[5][8] = cube[4][2], cube[4][5], cube[4][8]
		cube[4][2], cube[4][5], cube[4][8] = cube[2][2], cube[2][5], cube[2][8]
		cube[2][2], cube[2][5], cube[2][8] = cube[0][2], cube[0][5], cube[0][8]
		cube[0][2], cube[0][5], cube[0][8] = t1, t2, t3
		
		t1, t2, t3						   = cube[3][2], cube[3][5], cube[3][8]		#сама сторона right-1
		cube[3][2], cube[3][5], cube[3][8] = cube[3][8], cube[3][7], cube[3][6]
		cube[3][8], cube[3][7], cube[3][6] = cube[3][6], cube[3][3], cube[3][0]
		cube[3][6], cube[3][3], cube[3][0] = cube[3][2], cube[3][1], cube[3][2]
		cube[3][0], cube[3][1], cube[3][2] = t1, t2, t3

	if sign == "'":
		right·1(cube)
	elif sign == '2':
		right2(cube)
	elif sign == '':
		right1(cube)
	else:
		print('sign error')


def DOWN(cube, sign):
	def down1(cube):
		#print('down1')
		t1, t2, t3						   = cube[1][0], cube[1][3], cube[1][6]		#бока down1
		cube[1][0], cube[1][3], cube[1][6] = cube[2][6], cube[2][7], cube[2][8]
		cube[2][6], cube[2][7], cube[2][8] = cube[3][2], cube[3][5], cube[3][8]
		cube[3][2], cube[3][5], cube[3][8] = cube[5][6], cube[5][7], cube[5][8]
		cube[5][6], cube[5][7], cube[5][8] = t1, t2, t3
		
		t1, t2, t3						   = cube[4][2], cube[4][5], cube[4][8]		#сама сторона down1
		cube[4][2], cube[4][5], cube[4][8] = cube[4][8], cube[4][7], cube[4][6]
		cube[4][8], cube[4][7], cube[4][6] = cube[4][6], cube[4][3], cube[4][0]
		cube[4][6], cube[4][3], cube[4][0] = cube[4][0], cube[4][1], cube[4][2]
		cube[4][0], cube[4][1], cube[4][2] = t1, t2, t3

	def down2(cube):
		#print('down2')
		down1(cube)
		down1(cube)

	def down·1(cube):
		#print('down-1')
		t1, t2, t3						   = cube[5][6], cube[5][7], cube[5][8]		#бока down-1
		cube[5][6], cube[5][7], cube[5][8] = cube[3][2], cube[3][5], cube[3][8]
		cube[3][2], cube[3][5], cube[3][8] = cube[2][6], cube[2][7], cube[2][8]
		cube[2][6], cube[2][7], cube[2][8] = cube[1][0], cube[1][3], cube[1][6]
		cube[1][0], cube[1][3], cube[1][6] = t1, t2, t3
		
		t1, t2, t3						   = cube[4][0], cube[4][1], cube[4][2]		#сама сторона down-1
		cube[4][0], cube[4][1], cube[4][2] = cube[4][6], cube[4][3], cube[4][0]
		cube[4][6], cube[4][3], cube[4][0] = cube[4][8], cube[4][7], cube[4][6]
		cube[4][8], cube[4][7], cube[4][6] = cube[4][2], cube[4][5], cube[4][8]
		cube[4][2], cube[4][5], cube[4][8] = t1, t2, t3

	if sign == "'":
		down·1(cube)
	elif sign == '2':
		down2(cube)
	elif sign == '':
		down1(cube)
	else:
		print('sign error')


def BACK(cube, sign):
	def back1(cube):
		#print('back1')
		t1, t2, t3						   = cube[0][0], cube[0][1], cube[0][2]		#бока back1
		cube[0][0], cube[0][1], cube[0][2] = cube[1][0], cube[1][1], cube[1][2]
		cube[1][0], cube[1][1], cube[1][2] = cube[4][6], cube[4][7], cube[4][8]
		cube[4][6], cube[4][7], cube[4][8] = cube[3][0], cube[3][1], cube[3][2]
		cube[3][0], cube[3][1], cube[3][2] = t1, t2, t3
		
		t1, t2, t3						   = cube[5][2], cube[5][5], cube[5][8]		#сама сторона back1
		cube[5][2], cube[5][5], cube[5][8] = cube[5][8], cube[5][7], cube[5][6]
		cube[5][8], cube[5][7], cube[5][6] = cube[5][6], cube[5][3], cube[5][0]
		cube[5][6], cube[5][3], cube[5][0] = cube[5][2], cube[5][1], cube[5][2]
		cube[5][0], cube[5][1], cube[5][2] = t1, t2, t3
		
	def back2(cube):
		#print('back2')
		back1(cube)
		back1(cube)

	def back·1(cube):
		#print('back-1')
		t1, t2, t3						   = cube[3][0], cube[3][1], cube[3][2]		#бока back-1
		cube[3][0], cube[3][1], cube[3][2] = cube[4][6], cube[4][7], cube[4][8]
		cube[4][6], cube[4][7], cube[4][8] = cube[1][0], cube[1][1], cube[1][2]
		cube[1][0], cube[1][1], cube[1][2] = cube[0][0], cube[0][1], cube[0][2]
		cube[0][0], cube[0][1], cube[0][2] = t1, t2, t3
		
		t1, t2, t3						   = cube[5][0], cube[5][1], cube[5][2]		#сама сторона back-1
		cube[5][0], cube[5][1], cube[5][2] = cube[5][6], cube[5][3], cube[5][0]
		cube[5][6], cube[5][3], cube[5][0] = cube[5][8], cube[5][7], cube[5][6]
		cube[5][8], cube[5][7], cube[5][6] = cube[5][2], cube[5][5], cube[5][8]
		cube[5][2], cube[5][5], cube[5][8] = t1, t2, t3

	if sign == "'":
		back·1(cube)
	elif sign == '2':
		back2(cube)
	elif sign == '':
		back1(cube)
	else:
		print('sign error')


def LEFT(cube, sign):
	def left1(cube):
		#print('left1')
		t1, t2, t3						   = cube[0][0], cube[0][3], cube[0][6]		#бока left1
		cube[0][0], cube[0][3], cube[0][6] = cube[2][0], cube[2][3], cube[2][6]
		cube[2][0], cube[2][3], cube[2][6] = cube[4][0], cube[4][3], cube[4][6]
		cube[4][0], cube[4][3], cube[4][6] = cube[5][0], cube[5][3], cube[5][6]
		cube[5][0], cube[5][3], cube[5][6] = t1, t2, t3

		t1, t2, t3						   = cube[1][2], cube[1][5], cube[1][8]		#сама сторона left1
		cube[1][2], cube[1][5], cube[1][8] = cube[1][8], cube[1][7], cube[1][6]
		cube[1][8], cube[1][7], cube[1][6] = cube[1][6], cube[1][3], cube[1][0]
		cube[1][6], cube[1][3], cube[1][0] = cube[1][2], cube[1][1], cube[1][2]
		cube[1][0], cube[1][1], cube[1][2] = t1, t2, t3

	def left2(cube):
		#print('left2')
		left1(cube)
		left1(cube)

	def left·1(cube):
		#print('left-1')
		t1, t2, t3						   = cube[5][0], cube[5][3], cube[5][6]		#бока left-1
		cube[5][0], cube[5][3], cube[5][6] = cube[4][0], cube[4][3], cube[4][6]
		cube[4][0], cube[4][3], cube[4][6] = cube[2][0], cube[2][3], cube[2][6]
		cube[2][0], cube[2][3], cube[2][6] = cube[0][0], cube[0][3], cube[0][6]
		cube[0][0], cube[0][3], cube[0][6] = t1, t2, t3
		
		t1, t2, t3						   = cube[1][0], cube[1][1], cube[1][2]		#сама сторона left-1
		cube[1][0], cube[1][1], cube[1][3] = cube[1][6], cube[1][3], cube[1][0]
		cube[1][6], cube[1][3], cube[1][0] = cube[1][8], cube[1][7], cube[1][6]
		cube[1][8], cube[1][7], cube[1][6] = cube[1][2], cube[1][5], cube[1][8]
		cube[1][2], cube[1][5], cube[1][8] = t1, t2, t3

	if sign == "'":
		left·1(cube)
	elif sign == '2':
		left2(cube)
	elif sign == '':
		left1(cube)
	else:
		print('sign error')


# Между Up и Down
def EQUATORIAL(cube, sign):
	def equatorial1(cube):
		#print('equatorial1')
		t1, t2, t3						   = cube[1][1], cube[1][4], cube[1][7]
		cube[1][1], cube[1][4], cube[1][7] = cube[2][3], cube[2][4], cube[2][5]
		cube[2][3], cube[2][4], cube[2][5] = cube[3][7], cube[3][4], cube[3][1]
		cube[3][7], cube[3][4], cube[3][1] = cube[5][3], cube[5][4], cube[5][5]
		cube[5][3], cube[5][4], cube[5][5] = t1, t2, t3

	def equatorial2(cube):
		#print('equatorial2')
		equatorial1(cube)
		equatorial1(cube)

	def equatorial·1(cube):
		#print('equatorial-1')
		t1, t2, t3						   = cube[5][3], cube[5][4], cube[5][5]
		cube[5][3], cube[5][4], cube[5][5] = cube[3][7], cube[3][4], cube[3][1]
		cube[3][7], cube[3][4], cube[3][1] = cube[2][3], cube[2][4], cube[2][5]
		cube[2][3], cube[2][4], cube[2][5] = cube[1][1], cube[1][4], cube[1][7]
		cube[1][1], cube[1][4], cube[1][7] = t1, t2, t3

	if sign == "'":
		equatorial·1(cube)
	elif sign == '2':
		equatorial2(cube)
	elif sign == '':
		equatorial1(cube)
	else:
		print('sign error')


# Между Front и Back
def STANDING(cube, sign):
	def standing1(cube):
		#print('standing1')
		t1, t2, t3						   = cube[0][3], cube[0][4], cube[0][5]
		cube[0][3], cube[0][4], cube[0][5] = cube[1][3], cube[1][4], cube[1][5]
		cube[1][3], cube[1][4], cube[1][5] = cube[4][3], cube[4][4], cube[4][5]
		cube[4][3], cube[4][4], cube[4][5] = cube[3][3], cube[3][4], cube[3][5]
		cube[3][3], cube[3][4], cube[3][5] = t1, t2, t3

	def standing2(cube):
		#print('standing2')
		standing1(cube)
		standing1(cube)

	def standing·1(cube):
		#print('standing-1')
		t1, t2, t3						   = cube[3][3], cube[3][4], cube[3][5]
		cube[3][3], cube[3][4], cube[3][5] = cube[4][3], cube[4][4], cube[4][5]
		cube[4][3], cube[4][4], cube[4][5] = cube[1][3], cube[1][4], cube[1][5]
		cube[1][3], cube[1][4], cube[1][5] = cube[0][3], cube[0][4], cube[0][5]
		cube[0][3], cube[0][4], cube[0][5] = t1, t2, t3

	if sign == "'":
		standing·1(cube)
	elif sign == '2':
		standing2(cube)
	elif sign == '':
		standing1(cube)
	else:
		print('sign error')

# Между Left и Right
def MIDDLE(cube, sign):
	def middle1(cube):
		#print('middle1')
		t1, t2, t3						   = cube[0][1], cube[0][4], cube[0][7]
		cube[0][1], cube[0][4], cube[0][7] = cube[2][1], cube[2][4], cube[2][7]
		cube[2][1], cube[2][4], cube[2][7] = cube[4][1], cube[4][4], cube[4][7]
		cube[4][1], cube[4][4], cube[4][7] = cube[5][1], cube[5][4], cube[5][7]
		cube[5][1], cube[5][4], cube[5][7] = t1, t2, t3

	def middle2(cube):
		#print('middle2')
		middle1(cube)
		middle1(cube)

	def middle·1(cube):
		#print('middle-1')
		t1, t2, t3						   = cube[5][1], cube[5][4], cube[5][7]
		cube[5][1], cube[5][4], cube[5][7] = cube[4][1], cube[4][4], cube[4][7]
		cube[4][1], cube[4][4], cube[4][7] = cube[2][1], cube[2][4], cube[2][7]
		cube[2][1], cube[2][4], cube[2][7] = cube[0][1], cube[0][4], cube[0][7]
		cube[0][1], cube[0][4], cube[0][7] = t1, t2, t3

	if sign == "'":
		middle·1(cube)
	elif sign == '2':
		middle2(cube)
	elif sign == '':
		middle1(cube)
	else:
		print('sign error')



def rotate_cube(turn_list, cube_list):
	'''
	собирает все вращения вместе 
	и переводит из одного вида в 
	другой (написанного в калькуляторе 
	или скопированного из блокнота 
	и передает их другим функциям 
	для вращения кубика и печати его)
	
	МОЖЕТ ПЕРЕПИСАТЬ ЧЕРЕЗ РЕГУЛЯРНЫЕ ВЫРАЖЕНИЯ ИЛИ СЛОВАРЬ
	'''
	cube = cube_list
	for turn in turn_list:
		if '2' in turn:
			sign = '2'
		elif "'" in turn:
			sign = "'"
		else:
			sign = ''
		
		if 'U' in turn:
			UP(cube, sign)
		elif 'F' in turn:
			FRONT(cube, sign)
		elif 'R' in turn:
			RIGHT(cube, sign)
		elif 'D' in turn:
			DOWN(cube, sign)
		elif 'B' in turn:
			BACK(cube, sign)
		elif 'L' in turn:
			LEFT(cube, sign)
		elif 'E' in turn:
			EQUATORIAL(cube, sign)
		elif 'S' in turn:
			STANDING(cube, sign)
		elif 'M' in turn:
			MIDDLE(cube, sign)
		else:
			print('turn: ' + turn + ' is not turn')
#"""



"""
#	ОТКРЫТИЕ В ОКНЕ #??
"""

#import graphics as gr	# Лучше оставить импорт вверху как норм #??

length = 800
height = 900

size = 100
square_size = size - 70
width = 5
x, y = 100, height/2 - 2*size

def background_painting(background_color):
	background_painting =  gr.Rectangle(gr.Point(0, 0), gr.Point(length, height))
	background_painting.setFill(background_color)
	background_painting.draw(window)

def coloring(cube_list, step = 1):
	"""
	Меняет короткие названия цветов на полные
	"""
	if step == 1:
		colors = {'y': 'yellow', 'o': 'orange', 'b': 'blue', 'r': 'red', 'w': 'white','g': 'green'}

		for side in range(len(cube_list)):
			for square in range(len(cube_list[side])):
				color = cube_list[side][square]
				if color in colors:
					cube_list[side][square] = colors.get(color, ' ')
	elif step == 2:
		colors = {'yellow': 'y', 'orange': 'o', 'blue': 'b', 'red': 'r', 'white': 'w','green': 'g'}

		for side in range(len(cube_list)):
			for square in range(len(cube_list[side])):
				color = cube_list[side][square]
				if color in colors:
					cube_list[side][square] = colors.get(color, ' ')
	else:
		print('Wrong step in function: coloring')

	#print(cube_list)
	return cube_list


def painting_cube(cube_list):
	"""
	Выдает координаты по №
	"""
	coloring(cube_list, 1)

	coordinates_side_x = {
		0: x + 2*(size + width),	#0	#top
		1: x,						#1	#left_side
		2: x + 2*(size + width),	#2	#front_side
		3: x + 4*(size + width),	#3	#right_side
		4: x + 2*(size + width),	#4	#bottom
		5: x + 2*(size + width)		#5	#back_side
			}
	
	coordinates_side_y = {
		0: y - 2*(size + width),	#0	#top
		1: y,						#1	#left_side
		2: y,						#2	#front_side
		3: y,						#3	#right_side
		4: y + 2*(size + width),	#4	#bottom
		5: y + 4*(size + width)		#5	#back_side
			}

	for side in range(len(cube_list)):
		temporary_coordinate_side = side
		if temporary_coordinate_side in coordinates_side_x:
			side_x = coordinates_side_x.get(temporary_coordinate_side, ' ')
		if temporary_coordinate_side in coordinates_side_y:
			side_y = coordinates_side_y.get(temporary_coordinate_side, ' ')
		side_painting(side_x, side_y, size)
		
		coordinates_square_x = {
			0: side_x + width,
			1: side_x + width + 2*(width - 3) + 2*square_size,
			2: side_x + width + 4*(width - 3) + 4*square_size,
			3: side_x + width,
			4: side_x + width + 2*(width - 3) + 2*square_size,
			5: side_x + width + 4*(width - 3) + 4*square_size,
			6: side_x + width,
			7: side_x + width + 2*(width - 3) + 2*square_size,
			8: side_x + width + 4*(width - 3) + 4*square_size
				}
	
		coordinates_square_y = {
			0: side_y + width,
			1: side_y + width,
			2: side_y + width,
			3: side_y + width + 2*(width - 3) + 2*square_size,
			4: side_y + width + 2*(width - 3) + 2*square_size,
			5: side_y + width + 2*(width - 3) + 2*square_size,
			6: side_y + width + 4*(width - 3) + 4*square_size,
			7: side_y + width + 4*(width - 3) + 4*square_size,
			8: side_y + width + 4*(width - 3) + 4*square_size
				}
		
		for square in range(len(cube_list[side])):
			temporary_coordinate_square = square
			if temporary_coordinate_square in coordinates_square_x:
				square_x = coordinates_square_x.get(temporary_coordinate_square, ' ')
			if temporary_coordinate_square in coordinates_square_y:
				square_y = coordinates_square_y.get(temporary_coordinate_square, ' ')
			#print(str(square_x) + ' ' + str(square_y))
			square_painting(square_x, square_y, square_size, cube_list[side][square])

	coloring(cube_list, 2)

def side_painting(x, y, size):
	side_painting =  gr.Rectangle(gr.Point(x, y), gr.Point(x + 2*size, y + 2*size))
	side_painting.setFill('gray')
	side_painting.setWidth(width)
	side_painting.draw(window)

def square_painting(x, y, size, color = 'green'):
	square_painting =  gr.Rectangle(gr.Point(x, y), gr.Point(x + 2*size, y + 2*size))
	square_painting.setFill(color)
	square_painting.setWidth(width - 3)
	square_painting.draw(window)




"""
#	ЗАПУСК
#"""

'''Запуск по частям #??
#while True:
print()
#turn_string = 'IUp'#input()
#turn_string = '(ILeftIEquatorial^2ILeft'IEquatorial^2ILeft'IStandingILeftIStanding')'

#turn_string = 'IUpIFrontIRightIDownIBackILeftIEquatorialIStandingIMiddle'
#UP FRONT RIGHT DOWN BACK LEFT EQUATORIAL STANDING MIDDLE
#up front right down back left equatorial standing middle
#U F R D B L E S M '

#Middle Между Left и Right
#Standing Между Front и Back
#Equatorial Между Up и Down

#if turn_string == 'exit' or turn_string == 'Exit' or turn_string == 'e':
#	break 
#check_string(turn_string)
print()
#print(return_rubiks_cube(turn_string, 1), end = '\n\n')
#print(return_rubiks_cube(turn_string, 2), end = '\n\n')
'''

'''
 0		0,1,2 
123		3,4,5
 4		6,7,8
 5
'''

cube_list = [
				['y','y','y',	#0	#top
				 'y','y','y',		
				 'y','y','y'],		
['o','o','o',	#1	#left_side
 'o','o','o',
 'o','o','o'],
				['b','b','b',	#2	#front_side
				 'b','b','b',
				 'b','b','b'],
								['r','r','r',	#3	#right_side
								 'r','r','r',
								 'r','r','r'],
				['w','w','w',	#4	#bottom
				 'w','w','w',
				 'w','w','w'],

				['g','g','g',	#5	#back_side
				 'g','g','g',
				 'g','g','g']]


# Запуск Simulation of cube on computer отдельно
# + ВКЛЮЧИТЬ ИМПОРТ ГРАФИКС
"""
turn_string = "U2 D2 E2 F2 B2 S2 R2 L2 M2"
rotate_cube(check_string(string), cube_list)

print(list_to_string(cube_list))
#string_to_list(list_to_string(cube_list))

#find_different(cube_list, cube_list)

window = gr.GraphWin('Simulation of cube on computer', length, height)

painting_cube(cube_list)
#"""

# Запуск Simulation of cube on computer через main
#"""
turn_string = "U2 D2 E2 F2 B2 S2 R2 L2 M2"	#for check all rotation funtion

#window = gr.GraphWin('Simulation of cube on computer', length, height)
#background_painting('black')

#painting_cube(cube_list)
#"""




"""
#	ЗАПИСЬ В ФАЙЛЫ
#"""

def saving_cube(cube_list_for_saving, with_txt='completely'):
	'''
	Добавляет строку с вращениями и куб в txt
	Cохраняет cube_list в cube save
	'''

	if 'Cube_saves' not in os.getcwd():
		saving_directory = os.path.join(os.getcwd(), 'Cube_saves')
	else:
		saving_directory =  os.getcwd()

	if not os.path.exists(saving_directory):
		os.makedirs(saving_directory)

	os.chdir(saving_directory)

	with_txt = with_txt.lower()
	if with_txt == 'completely' or with_txt == 'c' or with_txt == 'y' or with_txt == 'yes':
		saving_file_txt = os.path.join(	saving_directory, 'Cube_saves.txt')
		super_cube = list_to_string(cube_list_for_saving)
		Cube_saves_file = open(saving_file_txt, 'a')
		
		Cube_saves_file.write(
		wherefrom_string + '\n\n' +
		turn_string + '\n\n' +
		super_cube + '\n\n\n\n'
		)
		
		Cube_saves_file.close()


	shelf_file = shelve.open('cube save')
	shelf_file['cube_list_save'] = cube_list_for_saving # Сохранение
	shelf_file.close
#"""
#saving_cube(cube_list, 'y')

def loading_cube():
	'''
	Загружает cube_list сохранённый в cube save
	Выводит на экран в виде super_cube
	Возвращает загруженый cube_list
	'''
	
	if 'Cube_saves' not in os.getcwd():
		saving_directory = os.path.join(os.getcwd(), 'Cube_saves')
	else:
		saving_directory =  os.getcwd()

	if not os.path.exists(saving_directory):
		print('Saving directory does not exist. Check and try again.')
		return
	else:
		os.chdir(saving_directory)
	
	shelf_file = shelve.open('cube save')	
	cube_list_from_save = shelf_file['cube_list_save'] # Загрузка
	print(list_to_string(cube_list_from_save))
	shelf_file.close
	return cube_list_from_save


word = 'Exit'
#'''ЗАКРЫТИЕ НА КОМПЬЮТЕРЕ
print()
input(word)
#'''


# Временные строки

