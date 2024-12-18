"""
Записать краткий конспект основных
свойств и функций, чтобы выбрать
как проще обрабатывать

	ЧТО ДОБАВИТЬ:
Проверять все принты при запуске: Отправляють print в sms_as_cmd #?

Те функции для которых #нет реализации в main

Исправить:
		? 3d сохраняет не только в папку от запускаемого файла
"""

# ! python3

import re
import os
import shelve
import pprint
# import graphics as gr

os_getcwd = os.getcwd()

"""
#		РАБОТА СО СТРОКАМИ И СПИСКАМИ
#"""

where_from_string = 'Из файла: '


def check_string(main_string):
	"""
	Проверка подходит ли строка для вращения кубика
	потом какая строка: из калькулятора или из блокнота.
	Вывод её в удобном виде и для подачи на вращения кубика
	"""
	""" #?
	Возможно добавить после проверки через regex
	if содержит, что-то чего нет в словаре:
		print('Строка не подходит для вращения кубика')
		input('Попробуйте другую строку:\n')

	else:
		print()#то это нужная строка#Launch(запуск)
	"""
	global where_from_string
	
	string_regex = re.compile(r"[^a-i k-uwA-IK-UW()^'2\\]")
	mo = string_regex.search(main_string)
	if mo is not None:
		print('Строка не подходит для вращения кубика')
		input('Попробуйте другую строку:\n')
	else:
		print('')
	
	main_string = main_string.strip('()')
	main_string = main_string.rstrip(' ')
	if 'I' in main_string:
		where_from_string = 'Из калькулятора: '
		print(where_from_string, end = '\n\n')
		
		main_string = return_rubik_cube(main_string, 1)
		main_string = main_string.strip()
	else:
		where_from_string = 'Из блокнота: '
		print(where_from_string, end = '\n\n')
	print(main_string, end = '\n\n')
	turn_list = main_string.split(' ')
	print(str(turn_list))
	return turn_list


def reverse_and_apostrophe(main_string):
	main_string.reverse()
	for i in range(len(main_string) - 1):
		if "'" in main_string[i]:
			# убрать апостроф
			main_string[i] = main_string[i].replace("'", '')
		elif '2' not in main_string[i]:
			# добавить апостоф
			main_string[i] = main_string[i] + "'"
	return main_string


def return_rubik_cube(main_string, step):
	"""
	Получает строчку из графического калькулятора
	и возвращает строку которая будет обратной,
	то есть справа на лево и штрих убирает,
	если есть или добавляет если нет и нет 2, ещё убирает скобки
	"""
	main_string = main_string.strip('()')
	main_string = main_string.split('I')
	for i in range(len(main_string) - 1):
		main_string[i] = main_string[i].replace('^', '')
	# main_string[i] = main_string[i].upper()
	if step == 2:
		main_string = reverse_and_apostrophe(main_string)
	main_string = ' '.join(main_string)
	return main_string


'''	ПЕРЕПИСАТЬ string to list НОРМАЛЬНО!!!'''  # ???


def string_to_list(super_cube):
	"""
	из строки super_cube
	делает cube_list
	"""
	super_cube = super_cube.replace('_', '')
	super_cube = super_cube.replace('\n', '')
	super_cube = super_cube.replace('\t', '')
	super_cube = super_cube.replace(' ', '')
	cube_list2 = super_cube.split('·')

	for i in range(cube_list2.count('')):
		cube_list2.remove('')
	print(cube_list2)
	
	# [0,1,2,3,4,5,6,7,8]
	cube_list3 = [[9, 9, 9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9, 9, 9],
	              [9, 9, 9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9, 9, 9]]
	
	for side in range(len(cube_list3)):
		if str(side) in '045':
			side_cube_list2 = cube_list2[3 * side] + cube_list2[3 * side + 1] + cube_list2[3 * side + 2]
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
	
	# print(str(cube_list3) + '  cube_list3')
	return cube_list3


'''	ПЕРЕПИСАТЬ list to string НОРМАЛЬНО!!!'''  # ???


def list_to_string(cube_list_local):
	"""
	из списка cube_list
	делает super_cube
	"""
	super_cube = ('\n' +
	              '    ·___·' + cube_list_local[0][0] + cube_list_local[0][1] + cube_list_local[0][2] + '·___·' + '\n' +
	              '    ·___·' + cube_list_local[0][3] + cube_list_local[0][4] + cube_list_local[0][5] + '·___·' + '\n' +
	              '    ·___·' + cube_list_local[0][6] + cube_list_local[0][7] + cube_list_local[0][8] + '·___·' + '\n' +
	              '    ·___     ___·' + '\n' +
	              '    ·' + cube_list_local[1][0] + cube_list_local[1][1] + cube_list_local[1][2] + '·' +
	              cube_list_local[2][0] + cube_list_local[2][1] + cube_list_local[2][2] + '·' +
	              cube_list_local[3][0] + cube_list_local[3][1] + cube_list_local[3][2] + '·' +
	              '\n' +
	              '    ·' + cube_list_local[1][3] + cube_list_local[1][4] + cube_list_local[1][5] + '·' +
	              cube_list_local[2][3] + cube_list_local[2][4] + cube_list_local[2][5] + '·' +
	              cube_list_local[3][3] + cube_list_local[3][4] + cube_list_local[3][5] + '·' +
	              '\n' +
	              '    ·' + cube_list_local[1][6] + cube_list_local[1][7] + cube_list_local[1][8] + '·' +
	              cube_list_local[2][6] + cube_list_local[2][7] + cube_list_local[2][8] + '·' +
	              cube_list_local[3][6] + cube_list_local[3][7] + cube_list_local[3][8] + '·' +
	              '\n' + '    ·___     ___·' + '\n' +
	              '    ·___·' + cube_list_local[4][0] + cube_list_local[4][1] + cube_list_local[4][2] + '·___·' + '\n' +
	              '    ·___·' + cube_list_local[4][3] + cube_list_local[4][4] + cube_list_local[4][5] + '·___·' + '\n' +
	              '    ·___·' + cube_list_local[4][6] + cube_list_local[4][7] + cube_list_local[4][8] + '·___·' + '\n' +
	              '    ·___     ___·' + '\n' +
	              '    ·___·' + cube_list_local[5][0] + cube_list_local[5][1] + cube_list_local[5][2] + '·___·' + '\n' +
	              '    ·___·' + cube_list_local[5][3] + cube_list_local[5][4] + cube_list_local[5][5] + '·___·' + '\n' +
	              '    ·___·' + cube_list_local[5][6] + cube_list_local[5][7] + cube_list_local[5][8] + '·___·' + '\n'
	              )
	return super_cube


def list_to_cube_3d_html(cube_list_local):
	"""
	из списка cube_list
	делает cube_3d_html
	"""
	
	dict_string_to_png = {'b': 'blue', 'g': 'green', 'r': 'red', 'o': 'orange', 'y': 'yellow', 'w': 'white'}
	
	cube_3d_html = (f'''<!DOCTYPE html>
<html>

	<head>
		<meta charset="UTF-8"/>
		<title>3d</title>
		<link href="3d.css" rel="stylesheet" type="text/css"/>
		<script src="3d.js"></script>
	</head>
  
	<body>
		<div class="container">
			<div class="cube">
			
				<table class="side front">blue
					<tr><td><img src="images/
					{dict_string_to_png[cube_list_local[2][0]]}
					.png" height=70px/>0</td><td><img src="images/
					{dict_string_to_png[cube_list_local[2][1]]}
					.png" height=70px/>1</td><td><img src="images/
					{dict_string_to_png[cube_list_local[2][2]]}
					.png" height=70px/>2</td></tr><tr><td><img src="images/
					{dict_string_to_png[cube_list_local[2][3]]}
					.png" height=70px/>3</td><td><img src="images/
					{dict_string_to_png[cube_list_local[2][4]]}
					.png" height=70px/>4</td><td><img src="images/
					{dict_string_to_png[cube_list_local[2][5]]}
					.png" height=70px/>5</td></tr><tr><td><img src="images/
					{dict_string_to_png[cube_list_local[2][6]]}
					.png" height=70px/>6</td><td><img src="images/
					{dict_string_to_png[cube_list_local[2][7]]}
					.png" height=70px/>7</td><td><img src="images/
					{dict_string_to_png[cube_list_local[2][8]]}
					.png" height=70px/>8</td></tr>
				</table>
			
				<table class="side back">green
					<tr><td><img src="images/
					{dict_string_to_png[cube_list_local[5][0]]}
					.png" height=70px/>0</td><td><img src="images/
					{dict_string_to_png[cube_list_local[5][1]]}
					.png" height=70px/>1</td><td><img src="images/
					{dict_string_to_png[cube_list_local[5][2]]}
					.png" height=70px/>2</td></tr><tr><td><img src="images/
					{dict_string_to_png[cube_list_local[5][3]]}
					.png" height=70px/>3</td><td><img src="images/
					{dict_string_to_png[cube_list_local[5][4]]}
					.png" height=70px/>4</td><td><img src="images/
					{dict_string_to_png[cube_list_local[5][5]]}
					.png" height=70px/>5</td></tr><tr><td><img src="images/
					{dict_string_to_png[cube_list_local[5][6]]}
					.png" height=70px/>6</td><td><img src="images/
					{dict_string_to_png[cube_list_local[5][7]]}
					.png" height=70px/>7</td><td><img src="images/
					{dict_string_to_png[cube_list_local[5][8]]}
					.png" height=70px/>8</td></tr>
				</table>
			
				<table class="side right">red
					<tr><td><img src="images/
					{dict_string_to_png[cube_list_local[3][0]]}
					.png" height=70px/>0</td><td><img src="images/
					{dict_string_to_png[cube_list_local[3][1]]}
					.png" height=70px/>1</td><td><img src="images/
					{dict_string_to_png[cube_list_local[3][2]]}
					.png" height=70px/>2</td></tr><tr><td><img src="images/
					{dict_string_to_png[cube_list_local[3][3]]}
					.png" height=70px/>3</td><td><img src="images/
					{dict_string_to_png[cube_list_local[3][4]]}
					.png" height=70px/>4</td><td><img src="images/
					{dict_string_to_png[cube_list_local[3][5]]}
					.png" height=70px/>5</td></tr><tr><td><img src="images/
					{dict_string_to_png[cube_list_local[3][6]]}
					.png" height=70px/>6</td><td><img src="images/
					{dict_string_to_png[cube_list_local[3][7]]}
					.png" height=70px/>7</td><td><img src="images/
					{dict_string_to_png[cube_list_local[3][8]]}
					.png" height=70px/>8</td></tr>
				</table>
			
				<table class="side left">orange
					<tr><td><img src="images/
					{dict_string_to_png[cube_list_local[1][0]]}
					.png" height=70px/>0</td><td><img src="images/
					{dict_string_to_png[cube_list_local[1][1]]}
					.png" height=70px/>1</td><td><img src="images/
					{dict_string_to_png[cube_list_local[1][2]]}
					.png" height=70px/>2</td></tr><tr><td><img src="images/
					{dict_string_to_png[cube_list_local[1][3]]}
					.png" height=70px/>3</td><td><img src="images/
					{dict_string_to_png[cube_list_local[1][4]]}
					.png" height=70px/>4</td><td><img src="images/
					{dict_string_to_png[cube_list_local[1][5]]}
					.png" height=70px/>5</td></tr><tr><td><img src="images/
					{dict_string_to_png[cube_list_local[1][6]]}
					.png" height=70px/>6</td><td><img src="images/
					{dict_string_to_png[cube_list_local[1][7]]}
					.png" height=70px/>7</td><td><img src="images/
					{dict_string_to_png[cube_list_local[1][8]]}
					.png" height=70px/>8</td></tr>
				</table>
			
				<table class="side top">yellow
					<tr><td><img src="images/
					{dict_string_to_png[cube_list_local[0][0]]}
					.png" height=70px/>0</td><td><img src="images/
					{dict_string_to_png[cube_list_local[0][1]]}
					.png" height=70px/>1</td><td><img src="images/
					{dict_string_to_png[cube_list_local[0][2]]}
					.png" height=70px/>2</td></tr><tr><td><img src="images/
					{dict_string_to_png[cube_list_local[0][3]]}
					.png" height=70px/>3</td><td><img src="images/
					{dict_string_to_png[cube_list_local[0][4]]}
					.png" height=70px/>4</td><td><img src="images/
					{dict_string_to_png[cube_list_local[0][5]]}
					.png" height=70px/>5</td></tr><tr><td><img src="images/
					{dict_string_to_png[cube_list_local[0][6]]}
					.png" height=70px/>6</td><td><img src="images/
					{dict_string_to_png[cube_list_local[0][7]]}
					.png" height=70px/>7</td><td><img src="images/
					{dict_string_to_png[cube_list_local[0][8]]}
					.png" height=70px/>8</td></tr>
				</table>
			
				<table class="side bottom">white
					<tr><td><img src="images/
					{dict_string_to_png[cube_list_local[4][0]]}
					.png" height=70px/>0</td><td><img src="images/
					{dict_string_to_png[cube_list_local[4][1]]}
					.png" height=70px/>1</td><td><img src="images/
					{dict_string_to_png[cube_list_local[4][2]]}
					.png" height=70px/>2</td></tr><tr><td><img src="images/
					{dict_string_to_png[cube_list_local[4][3]]}
					.png" height=70px/>3</td><td><img src="images/
					{dict_string_to_png[cube_list_local[4][4]]}
					.png" height=70px/>4</td><td><img src="images/
					{dict_string_to_png[cube_list_local[4][5]]}
					.png" height=70px/>5</td></tr><tr><td><img src="images/
					{dict_string_to_png[cube_list_local[4][6]]}
					.png" height=70px/>6</td><td><img src="images/
					{dict_string_to_png[cube_list_local[4][7]]}
					.png" height=70px/>7</td><td><img src="images/
					{dict_string_to_png[cube_list_local[4][8]]}
					.png" height=70px/>8</td></tr>
				</table>
				
			</div>
		</div>
	</body>

</html>'''
	              )
	return cube_3d_html


def cube_3d_html_to_html(cube_3d_html):
	with open(os.path.join(os_getcwd, '3d', '3d.html'), 'w') as myfile:  # Исправить сохраняет не только в папку от запускаемого файла
		myfile.write(cube_3d_html)


"""
#		СРАВНЕНИЕ КУБИКА
#""" 


def compare_cube(cube_1, cube_2):
	"""
	находит и выводит разные ли
	два кубика
	"""
	if str(type(cube_1)) == "<class 'list'>" and str(type(cube_2)) == "<class 'list'>":
		if string_to_list(list_to_string(cube_1)) == string_to_list(list_to_string(cube_2)):
			print('Cube 1 = Cube 2')
			return True
		else:
			print('				Cube 1 no = Cube 2\n')
			print('Cube 1: ' + '\n\n' + list_to_string(cube_1) + '\n\n\n' + 'Cube 2: ' + '\n\n' + list_to_string(cube_2))
	elif str(type(cube_1)) == "<class 'list'>" and str(type(cube_2)) == "<class 'str'>":
		if string_to_list(list_to_string(cube_1)) == string_to_list(cube_2):
			print('Cube 1 = Cube 2')
		else:
			print('				Cube 1 no = Cube 2\n')
			print('Cube 1: ' + '\n\n' + list_to_string(cube_1) + '\n\n\n' + 'Cube 2: ' + '\n\n' + list_to_string(cube_2))
	elif str(type(cube_1)) == "<class 'str'>" and str(type(cube_2)) == "<class 'list'>":
		if string_to_list(cube_1) == string_to_list(list_to_string(cube_2)):
			print('Cube 1 = Cube 2')
		else:
			print('				Cube 1 no = Cube 2\n')
			print('Cube 1: ' + '\n\n' + list_to_string(cube_1) + '\n\n\n' + 'Cube 2: ' + '\n\n' + list_to_string(cube_2))
	elif str(type(cube_1)) == "<class 'str'>" and str(type(cube_2)) == "<class 'str'>":
		if string_to_list(cube_1) == string_to_list(cube_2):
			print('Cube 1 = Cube 2')
		else:
			print('				Cube 1 no = Cube 2\n')
			print('Cube 1: ' + '\n\n' + list_to_string(cube_1) + '\n\n\n' + 'Cube 2: ' + '\n\n' + list_to_string(cube_2))
	else:
		print('Cube 1 or Cube 2 is not string or list')
		print('Cube 1: ' + '\n\n' + str(cube_1) + '\n\n\n' + 'Cube 2: ' + '\n\n' + str(cube_2))


def compare_cube_by_one(cube_1, cube_2):
	"""
	находит и выводит разницу между
	двумя кубиками
	"""
	if str(type(cube_1)) == "<class 'str'>":
		cube_1 = string_to_list(cube_1)
	if str(type(cube_2)) == "<class 'str'>":
		cube_2 = string_to_list(cube_2)
	
	num_of_coincidence = 0  # max 54
	
	for i in range(6):
		for j in range(9):
			if cube_1[i][j] == cube_2[i][j]:
				num_of_coincidence += 1
	
	return 54 - num_of_coincidence


def try_to_rotate_cube(cube_for_rotation):
	for j in list_of_turns:
		rotate_cube([j], cube_for_rotation)
		print(j)
		return cube_for_rotation


list_of_turns = ['U', 'F', 'R', 'D', 'B', 'L', 'E', 'S', 'M', "U'", "F'", "R'", "D'", "B'", "L'", "E'", "S'", "M'"]


def try_to_solve_cube_part():
	for a in [12, 13, 14, 15, 16, 17]:  # 0-17 - 7 поворотов мало
		print('a = ', a)
		cube = string_to_list(my_cube_string)
		cube_for_rotation = [cube[0][:], cube[1][:], cube[2][:], cube[3][:], cube[4][:], cube[5][:]]
		rotate_cube([list_of_turns[a]], cube_for_rotation)
		try_to_solve_cube(cube_for_rotation)


def try_to_solve_cube(cube):
	start_num = 14  # compare_cube_by_one(cube, start_cube_list)
	cube_for_rotation = [cube[0][:], cube[1][:], cube[2][:], cube[3][:], cube[4][:], cube[5][:]]
	print('start_num = ', str(start_num) + '\n')
	
	for i in list_of_turns:
		cube_for_rotation_1 = [cube_for_rotation[0][:], cube_for_rotation[1][:], cube_for_rotation[2][:], 
							   cube_for_rotation[3][:], cube_for_rotation[4][:], cube_for_rotation[5][:]]
		rotate_cube([i], cube_for_rotation_1)
		num = compare_cube_by_one(cube_for_rotation_1, start_cube_list)
		
		if num < start_num:
			print(i, num)
		else:
			for j in list_of_turns:
				cube_for_rotation_2 = [cube_for_rotation_1[0][:], cube_for_rotation_1[1][:], cube_for_rotation_1[2][:], 
									   cube_for_rotation_1[3][:], cube_for_rotation_1[4][:], cube_for_rotation_1[5][:]]
				rotate_cube([j], cube_for_rotation_2)
				num = compare_cube_by_one(cube_for_rotation_2, start_cube_list)
				
				if num < start_num:
					print(i, j, num)
				else:
					for k in list_of_turns:
						cube_for_rotation_3 = [cube_for_rotation_2[0][:], cube_for_rotation_2[1][:], cube_for_rotation_2[2][:], 
											   cube_for_rotation_2[3][:], cube_for_rotation_2[4][:], cube_for_rotation_2[5][:]]
						rotate_cube([k], cube_for_rotation_3)
						num = compare_cube_by_one(cube_for_rotation_3, start_cube_list)

						if num < start_num:
							print(i, j, k, num)
						else:
							for l in list_of_turns:
								cube_for_rotation_4 = [cube_for_rotation_3[0][:], cube_for_rotation_3[1][:], cube_for_rotation_3[2][:], 
													   cube_for_rotation_3[3][:], cube_for_rotation_3[4][:], cube_for_rotation_3[5][:]]
								rotate_cube([l], cube_for_rotation_4)
								num = compare_cube_by_one(cube_for_rotation_4, start_cube_list)

								if num < start_num:
									print(i, j, k, l, num)
								else:
									for m in list_of_turns:
										cube_for_rotation_5 = [cube_for_rotation_4[0][:], cube_for_rotation_4[1][:], cube_for_rotation_4[2][:], 
															   cube_for_rotation_4[3][:], cube_for_rotation_4[4][:], cube_for_rotation_4[5][:]]
										rotate_cube([m], cube_for_rotation_5)
										num = compare_cube_by_one(cube_for_rotation_5, start_cube_list)

										if num < start_num:
											print(i, j, k, l, m, num)
										else:
											for n in list_of_turns:
												cube_for_rotation_6 = [cube_for_rotation_5[0][:], cube_for_rotation_5[1][:], cube_for_rotation_5[2][:], 
																	   cube_for_rotation_5[3][:], cube_for_rotation_5[4][:], cube_for_rotation_5[5][:]]
												rotate_cube([n], cube_for_rotation_6)
												num = compare_cube_by_one(cube_for_rotation_6, start_cube_list)

												if num < start_num:
													print(i, j, k, l, m, n, num)
		
	print('Finish')


"""
#		ВРАЩЕНИЕ КУБИКА
#""" 


def up(cube, sign):
	def up1(cube1):
		# print('up1')
		t1, t2, t3 = cube1[1][2], cube1[1][5], cube1[1][8]  # бока up1
		cube1[1][2], cube1[1][5], cube1[1][8] = cube1[2][0], cube1[2][1], cube1[2][2]
		cube1[2][0], cube1[2][1], cube1[2][2] = cube1[3][0], cube1[3][3], cube1[3][6]
		cube1[3][0], cube1[3][3], cube1[3][6] = cube1[5][0], cube1[5][1], cube1[5][2]
		cube1[5][0], cube1[5][1], cube1[5][2] = t1, t2, t3
		
		t1, t2, t3 = cube1[0][0], cube1[0][1], cube1[0][2]  # сама сторона up1
		cube1[0][0], cube1[0][1], cube1[0][2] = cube1[0][6], cube1[0][3], cube1[0][0]
		cube1[0][6], cube1[0][3], cube1[0][0] = cube1[0][8], cube1[0][7], cube1[0][6]
		cube1[0][8], cube1[0][7], cube1[0][6] = cube1[0][2], cube1[0][5], cube1[0][8]
		cube1[0][2], cube1[0][5], cube1[0][8] = t1, t2, t3
	
	def up2(cube2):
		# print('up2')
		up1(cube2)
		up1(cube2)
	
	def up_1(cube_1):
		# print('up-1')
		t1, t2, t3 = cube_1[5][0], cube_1[5][1], cube_1[5][2]  # бока up-1
		cube_1[5][0], cube_1[5][1], cube_1[5][2] = cube_1[3][0], cube_1[3][3], cube_1[3][6]
		cube_1[3][0], cube_1[3][3], cube_1[3][6] = cube_1[2][0], cube_1[2][1], cube_1[2][2]
		cube_1[2][0], cube_1[2][1], cube_1[2][2] = cube_1[1][2], cube_1[1][5], cube_1[1][8]
		cube_1[1][2], cube_1[1][5], cube_1[1][8] = t1, t2, t3
		
		t1, t2, t3 = cube_1[0][2], cube_1[0][5], cube_1[0][8]  # сама сторона up-1
		cube_1[0][2], cube_1[0][5], cube_1[0][8] = cube_1[0][8], cube_1[0][7], cube_1[0][6]
		cube_1[0][8], cube_1[0][7], cube_1[0][6] = cube_1[0][6], cube_1[0][3], cube_1[0][0]
		cube_1[0][6], cube_1[0][3], cube_1[0][0] = cube_1[0][0], cube_1[0][1], cube_1[0][2]
		cube_1[0][0], cube_1[0][1], cube_1[0][2] = t1, t2, t3
	
	if sign == "'":
		up_1(cube)
	elif sign == '2':
		up2(cube)
	elif sign == '':
		up1(cube)
	else:
		print('sign error')


def front(cube, sign):
	def front1(cube1):
		# print('front1')
		t1, t2, t3 = cube1[0][6], cube1[0][7], cube1[0][8]  # бока front1
		cube1[0][6], cube1[0][7], cube1[0][8] = cube1[1][6], cube1[1][7], cube1[1][8]
		cube1[1][6], cube1[1][7], cube1[1][8] = cube1[4][0], cube1[4][1], cube1[4][2]
		cube1[4][0], cube1[4][1], cube1[4][2] = cube1[3][6], cube1[3][7], cube1[3][8]
		cube1[3][6], cube1[3][7], cube1[3][8] = t1, t2, t3
		
		t1, t2, t3 = cube1[2][0], cube1[2][1], cube1[2][2]  # сама сторона front1
		cube1[2][0], cube1[2][1], cube1[2][2] = cube1[2][6], cube1[2][3], cube1[2][0]
		cube1[2][6], cube1[2][3], cube1[2][0] = cube1[2][8], cube1[2][7], cube1[2][6]
		cube1[2][8], cube1[2][7], cube1[2][6] = cube1[2][2], cube1[2][5], cube1[2][8]
		cube1[2][2], cube1[2][5], cube1[2][8] = t1, t2, t3
	
	def front2(cube2):
		# print('front2')
		front1(cube2)
		front1(cube2)
	
	def front_1(cube_1):
		# print('front-1')
		t1, t2, t3 = cube_1[3][6], cube_1[3][7], cube_1[3][8]  # бока front-1
		cube_1[3][6], cube_1[3][7], cube_1[3][8] = cube_1[4][0], cube_1[4][1], cube_1[4][2]
		cube_1[4][0], cube_1[4][1], cube_1[4][2] = cube_1[1][6], cube_1[1][7], cube_1[1][8]
		cube_1[1][6], cube_1[1][7], cube_1[1][8] = cube_1[0][6], cube_1[0][7], cube_1[0][8]
		cube_1[0][6], cube_1[0][7], cube_1[0][8] = t1, t2, t3
		
		t1, t2, t3 = cube_1[2][2], cube_1[2][5], cube_1[2][8]  # сама сторона front-1
		cube_1[2][2], cube_1[2][5], cube_1[2][8] = cube_1[2][8], cube_1[2][7], cube_1[2][6]
		cube_1[2][8], cube_1[2][7], cube_1[2][6] = cube_1[2][6], cube_1[2][3], cube_1[2][0]
		cube_1[2][6], cube_1[2][3], cube_1[2][0] = cube_1[2][0], cube_1[2][1], cube_1[2][2]
		cube_1[2][0], cube_1[2][1], cube_1[2][2] = t1, t2, t3
	
	if sign == "'":
		front_1(cube)
	elif sign == '2':
		front2(cube)
	elif sign == '':
		front1(cube)
	else:
		print('sign error')


def right(cube, sign):
	def right1(cube1):
		# print('right1')
		t1, t2, t3 = cube1[0][2], cube1[0][5], cube1[0][8]  # бока right1
		cube1[0][2], cube1[0][5], cube1[0][8] = cube1[2][2], cube1[2][5], cube1[2][8]
		cube1[2][2], cube1[2][5], cube1[2][8] = cube1[4][2], cube1[4][5], cube1[4][8]
		cube1[4][2], cube1[4][5], cube1[4][8] = cube1[5][2], cube1[5][5], cube1[5][8]
		cube1[5][2], cube1[5][5], cube1[5][8] = t1, t2, t3
		
		t1, t2, t3 = cube1[3][0], cube1[3][1], cube1[3][2]  # сама сторона right1
		cube1[3][0], cube1[3][1], cube1[3][3] = cube1[3][6], cube1[3][3], cube1[3][0]
		cube1[3][6], cube1[3][3], cube1[3][0] = cube1[3][8], cube1[3][7], cube1[3][6]
		cube1[3][8], cube1[3][7], cube1[3][6] = cube1[3][2], cube1[3][5], cube1[3][8]
		cube1[3][2], cube1[3][5], cube1[3][8] = t1, t2, t3
	
	def right2(cube2):
		# print('right2')
		right1(cube2)
		right1(cube2)
	
	def right_1(cube_1):
		# print('right-1')
		t1, t2, t3 = cube_1[5][2], cube_1[5][5], cube_1[5][8]  # бока right-1
		cube_1[5][2], cube_1[5][5], cube_1[5][8] = cube_1[4][2], cube_1[4][5], cube_1[4][8]
		cube_1[4][2], cube_1[4][5], cube_1[4][8] = cube_1[2][2], cube_1[2][5], cube_1[2][8]
		cube_1[2][2], cube_1[2][5], cube_1[2][8] = cube_1[0][2], cube_1[0][5], cube_1[0][8]
		cube_1[0][2], cube_1[0][5], cube_1[0][8] = t1, t2, t3
		
		t1, t2, t3 = cube_1[3][2], cube_1[3][5], cube_1[3][8]  # сама сторона right-1
		cube_1[3][2], cube_1[3][5], cube_1[3][8] = cube_1[3][8], cube_1[3][7], cube_1[3][6]
		cube_1[3][8], cube_1[3][7], cube_1[3][6] = cube_1[3][6], cube_1[3][3], cube_1[3][0]
		cube_1[3][6], cube_1[3][3], cube_1[3][0] = cube_1[3][0], cube_1[3][1], cube_1[3][2]
		cube_1[3][0], cube_1[3][1], cube_1[3][2] = t1, t2, t3
	
	if sign == "'":
		right_1(cube)
	elif sign == '2':
		right2(cube)
	elif sign == '':
		right1(cube)
	else:
		print('sign error')


def down(cube, sign):
	def down1(cube1):
		# print('down1')
		t1, t2, t3 = cube1[1][0], cube1[1][3], cube1[1][6]  # бока down1
		cube1[1][0], cube1[1][3], cube1[1][6] = cube1[2][6], cube1[2][7], cube1[2][8]
		cube1[2][6], cube1[2][7], cube1[2][8] = cube1[3][2], cube1[3][5], cube1[3][8]
		cube1[3][2], cube1[3][5], cube1[3][8] = cube1[5][6], cube1[5][7], cube1[5][8]
		cube1[5][6], cube1[5][7], cube1[5][8] = t1, t2, t3
		
		t1, t2, t3 = cube1[4][2], cube1[4][5], cube1[4][8]  # сама сторона down1
		cube1[4][2], cube1[4][5], cube1[4][8] = cube1[4][8], cube1[4][7], cube1[4][6]
		cube1[4][8], cube1[4][7], cube1[4][6] = cube1[4][6], cube1[4][3], cube1[4][0]
		cube1[4][6], cube1[4][3], cube1[4][0] = cube1[4][0], cube1[4][1], cube1[4][2]
		cube1[4][0], cube1[4][1], cube1[4][2] = t1, t2, t3
	
	def down2(cube2):
		# print('down2')
		down1(cube2)
		down1(cube2)
	
	def down_1(cube_1):
		# print('down-1')
		t1, t2, t3 = cube_1[5][6], cube_1[5][7], cube_1[5][8]  # бока down-1
		cube_1[5][6], cube_1[5][7], cube_1[5][8] = cube_1[3][2], cube_1[3][5], cube_1[3][8]
		cube_1[3][2], cube_1[3][5], cube_1[3][8] = cube_1[2][6], cube_1[2][7], cube_1[2][8]
		cube_1[2][6], cube_1[2][7], cube_1[2][8] = cube_1[1][0], cube_1[1][3], cube_1[1][6]
		cube_1[1][0], cube_1[1][3], cube_1[1][6] = t1, t2, t3
		
		t1, t2, t3 = cube_1[4][0], cube_1[4][1], cube_1[4][2]  # сама сторона down-1
		cube_1[4][0], cube_1[4][1], cube_1[4][2] = cube_1[4][6], cube_1[4][3], cube_1[4][0]
		cube_1[4][6], cube_1[4][3], cube_1[4][0] = cube_1[4][8], cube_1[4][7], cube_1[4][6]
		cube_1[4][8], cube_1[4][7], cube_1[4][6] = cube_1[4][2], cube_1[4][5], cube_1[4][8]
		cube_1[4][2], cube_1[4][5], cube_1[4][8] = t1, t2, t3
	
	if sign == "'":
		down_1(cube)
	elif sign == '2':
		down2(cube)
	elif sign == '':
		down1(cube)
	else:
		print('sign error')


def back(cube, sign):
	def back1(cube1):
		# print('back1')
		t1, t2, t3 = cube1[0][0], cube1[0][1], cube1[0][2]  # бока back1
		cube1[0][0], cube1[0][1], cube1[0][2] = cube1[1][0], cube1[1][1], cube1[1][2]
		cube1[1][0], cube1[1][1], cube1[1][2] = cube1[4][6], cube1[4][7], cube1[4][8]
		cube1[4][6], cube1[4][7], cube1[4][8] = cube1[3][0], cube1[3][1], cube1[3][2]
		cube1[3][0], cube1[3][1], cube1[3][2] = t1, t2, t3
		
		t1, t2, t3 = cube1[5][2], cube1[5][5], cube1[5][8]  # сама сторона back1
		cube1[5][2], cube1[5][5], cube1[5][8] = cube1[5][8], cube1[5][7], cube1[5][6]
		cube1[5][8], cube1[5][7], cube1[5][6] = cube1[5][6], cube1[5][3], cube1[5][0]
		cube1[5][6], cube1[5][3], cube1[5][0] = cube1[5][0], cube1[5][1], cube1[5][2]
		cube1[5][0], cube1[5][1], cube1[5][2] = t1, t2, t3
	
	def back2(cube2):
		# print('back2')
		back1(cube2)
		back1(cube2)
	
	def back_1(cube_1):
		# print('back-1')
		t1, t2, t3 = cube_1[3][0], cube_1[3][1], cube_1[3][2]  # бока back-1
		cube_1[3][0], cube_1[3][1], cube_1[3][2] = cube_1[4][6], cube_1[4][7], cube_1[4][8]
		cube_1[4][6], cube_1[4][7], cube_1[4][8] = cube_1[1][0], cube_1[1][1], cube_1[1][2]
		cube_1[1][0], cube_1[1][1], cube_1[1][2] = cube_1[0][0], cube_1[0][1], cube_1[0][2]
		cube_1[0][0], cube_1[0][1], cube_1[0][2] = t1, t2, t3
		
		t1, t2, t3 = cube_1[5][0], cube_1[5][1], cube_1[5][2]  # сама сторона back-1
		cube_1[5][0], cube_1[5][1], cube_1[5][2] = cube_1[5][6], cube_1[5][3], cube_1[5][0]
		cube_1[5][6], cube_1[5][3], cube_1[5][0] = cube_1[5][8], cube_1[5][7], cube_1[5][6]
		cube_1[5][8], cube_1[5][7], cube_1[5][6] = cube_1[5][2], cube_1[5][5], cube_1[5][8]
		cube_1[5][2], cube_1[5][5], cube_1[5][8] = t1, t2, t3
	
	if sign == "'":
		back_1(cube)
	elif sign == '2':
		back2(cube)
	elif sign == '':
		back1(cube)
	else:
		print('sign error')


def left(cube, sign):
	def left1(cube1):
		# print('left1')
		t1, t2, t3 = cube1[0][0], cube1[0][3], cube1[0][6]  # бока left1
		cube1[0][0], cube1[0][3], cube1[0][6] = cube1[2][0], cube1[2][3], cube1[2][6]
		cube1[2][0], cube1[2][3], cube1[2][6] = cube1[4][0], cube1[4][3], cube1[4][6]
		cube1[4][0], cube1[4][3], cube1[4][6] = cube1[5][0], cube1[5][3], cube1[5][6]
		cube1[5][0], cube1[5][3], cube1[5][6] = t1, t2, t3
		
		t1, t2, t3 = cube1[1][2], cube1[1][5], cube1[1][8]  # сама сторона left1
		cube1[1][2], cube1[1][5], cube1[1][8] = cube1[1][8], cube1[1][7], cube1[1][6]
		cube1[1][8], cube1[1][7], cube1[1][6] = cube1[1][6], cube1[1][3], cube1[1][0]
		cube1[1][6], cube1[1][3], cube1[1][0] = cube1[1][0], cube1[1][1], cube1[1][2]
		cube1[1][0], cube1[1][1], cube1[1][2] = t1, t2, t3
	
	def left2(cube2):
		# print('left2')
		left1(cube2)
		left1(cube2)
	
	def left_1(cube_1):
		# print('left-1')
		t1, t2, t3 = cube_1[5][0], cube_1[5][3], cube_1[5][6]  # бока left-1
		cube_1[5][0], cube_1[5][3], cube_1[5][6] = cube_1[4][0], cube_1[4][3], cube_1[4][6]
		cube_1[4][0], cube_1[4][3], cube_1[4][6] = cube_1[2][0], cube_1[2][3], cube_1[2][6]
		cube_1[2][0], cube_1[2][3], cube_1[2][6] = cube_1[0][0], cube_1[0][3], cube_1[0][6]
		cube_1[0][0], cube_1[0][3], cube_1[0][6] = t1, t2, t3
		
		t1, t2, t3 = cube_1[1][0], cube_1[1][1], cube_1[1][2]  # сама сторона left-1
		cube_1[1][0], cube_1[1][1], cube_1[1][3] = cube_1[1][6], cube_1[1][3], cube_1[1][0]
		cube_1[1][6], cube_1[1][3], cube_1[1][0] = cube_1[1][8], cube_1[1][7], cube_1[1][6]
		cube_1[1][8], cube_1[1][7], cube_1[1][6] = cube_1[1][2], cube_1[1][5], cube_1[1][8]
		cube_1[1][2], cube_1[1][5], cube_1[1][8] = t1, t2, t3
	
	if sign == "'":
		left_1(cube)
	elif sign == '2':
		left2(cube)
	elif sign == '':
		left1(cube)
	else:
		print('sign error')


# Между up и down
def equatorial(cube, sign):
	def equatorial1(cube1):
		# print('equatorial1')
		t1, t2, t3 = cube1[1][1], cube1[1][4], cube1[1][7]
		cube1[1][1], cube1[1][4], cube1[1][7] = cube1[2][3], cube1[2][4], cube1[2][5]
		cube1[2][3], cube1[2][4], cube1[2][5] = cube1[3][7], cube1[3][4], cube1[3][1]
		cube1[3][7], cube1[3][4], cube1[3][1] = cube1[5][3], cube1[5][4], cube1[5][5]
		cube1[5][3], cube1[5][4], cube1[5][5] = t1, t2, t3
	
	def equatorial2(cube2):
		# print('equatorial2')
		equatorial1(cube2)
		equatorial1(cube2)
	
	def equatorial_1(cube_1):
		# print('equatorial-1')
		t1, t2, t3 = cube_1[5][3], cube_1[5][4], cube_1[5][5]
		cube_1[5][3], cube_1[5][4], cube_1[5][5] = cube_1[3][7], cube_1[3][4], cube_1[3][1]
		cube_1[3][7], cube_1[3][4], cube_1[3][1] = cube_1[2][3], cube_1[2][4], cube_1[2][5]
		cube_1[2][3], cube_1[2][4], cube_1[2][5] = cube_1[1][1], cube_1[1][4], cube_1[1][7]
		cube_1[1][1], cube_1[1][4], cube_1[1][7] = t1, t2, t3
	
	if sign == "'":
		equatorial_1(cube)
	elif sign == '2':
		equatorial2(cube)
	elif sign == '':
		equatorial1(cube)
	else:
		print('sign error')


# Между front и back
def standing(cube, sign):
	def standing1(cube1):
		# print('standing1')
		t1, t2, t3 = cube1[0][3], cube1[0][4], cube1[0][5]
		cube1[0][3], cube1[0][4], cube1[0][5] = cube1[1][3], cube1[1][4], cube1[1][5]
		cube1[1][3], cube1[1][4], cube1[1][5] = cube1[4][3], cube1[4][4], cube1[4][5]
		cube1[4][3], cube1[4][4], cube1[4][5] = cube1[3][3], cube1[3][4], cube1[3][5]
		cube1[3][3], cube1[3][4], cube1[3][5] = t1, t2, t3
	
	def standing2(cube2):
		# print('standing2')
		standing1(cube2)
		standing1(cube2)
	
	def standing_1(cube_1):
		# print('standing-1')
		t1, t2, t3 = cube_1[3][3], cube_1[3][4], cube_1[3][5]
		cube_1[3][3], cube_1[3][4], cube_1[3][5] = cube_1[4][3], cube_1[4][4], cube_1[4][5]
		cube_1[4][3], cube_1[4][4], cube_1[4][5] = cube_1[1][3], cube_1[1][4], cube_1[1][5]
		cube_1[1][3], cube_1[1][4], cube_1[1][5] = cube_1[0][3], cube_1[0][4], cube_1[0][5]
		cube_1[0][3], cube_1[0][4], cube_1[0][5] = t1, t2, t3
	
	if sign == "'":
		standing_1(cube)
	elif sign == '2':
		standing2(cube)
	elif sign == '':
		standing1(cube)
	else:
		print('sign error')


# Между left и right
def middle(cube, sign):
	def middle1(cube1):
		# print('middle1')
		t1, t2, t3 = cube1[0][1], cube1[0][4], cube1[0][7]
		cube1[0][1], cube1[0][4], cube1[0][7] = cube1[2][1], cube1[2][4], cube1[2][7]
		cube1[2][1], cube1[2][4], cube1[2][7] = cube1[4][1], cube1[4][4], cube1[4][7]
		cube1[4][1], cube1[4][4], cube1[4][7] = cube1[5][1], cube1[5][4], cube1[5][7]
		cube1[5][1], cube1[5][4], cube1[5][7] = t1, t2, t3
	
	def middle2(cube2):
		# print('middle2')
		middle1(cube2)
		middle1(cube2)
	
	def middle_1(cube_1):
		# print('middle-1')
		t1, t2, t3 = cube_1[5][1], cube_1[5][4], cube_1[5][7]
		cube_1[5][1], cube_1[5][4], cube_1[5][7] = cube_1[4][1], cube_1[4][4], cube_1[4][7]
		cube_1[4][1], cube_1[4][4], cube_1[4][7] = cube_1[2][1], cube_1[2][4], cube_1[2][7]
		cube_1[2][1], cube_1[2][4], cube_1[2][7] = cube_1[0][1], cube_1[0][4], cube_1[0][7]
		cube_1[0][1], cube_1[0][4], cube_1[0][7] = t1, t2, t3
	
	if sign == "'":
		middle_1(cube)
	elif sign == '2':
		middle2(cube)
	elif sign == '':
		middle1(cube)
	else:
		print('sign error')


def rotate_cube(turn_list, cube_list_local):
	"""
	собирает все вращения вместе
	и переводит из одного вида в
	другой (написанного в калькуляторе
	или скопированного из блокнота
	и передает их другим функциям
	для вращения кубика и печати его)

	МОЖЕТ ПЕРЕПИСАТЬ ЧЕРЕЗ РЕГУЛЯРНЫЕ ВЫРАЖЕНИЯ ИЛИ СЛОВАРЬ
	"""
	cube = cube_list_local
	for turn in turn_list:
		if '2' in turn:
			sign = '2'
		elif "'" in turn:
			sign = "'"
		else:
			sign = ''
		
		if 'U' in turn:
			up(cube, sign)
		elif 'F' in turn:
			front(cube, sign)
		elif 'R' in turn:
			right(cube, sign)
		elif 'D' in turn:
			down(cube, sign)
		elif 'B' in turn:
			back(cube, sign)
		elif 'L' in turn:
			left(cube, sign)
		elif 'E' in turn:
			equatorial(cube, sign)
		elif 'S' in turn:
			standing(cube, sign)
		elif 'M' in turn:
			middle(cube, sign)
		else:
			print('turn: ' + turn + ' is not turn')


# """


def coloring(cube_list_local, step = 1):
	"""
	Меняет короткие названия цветов на полные
	"""
	
	if step == 1:
		colors = {'y': 'Yellow', 'o': 'Orange', 'b': 'Blue', 'r': 'Red', 'w': 'White', 'g': 'Green'}
		
		for side in range(len(cube_list_local)):
			for square in range(len(cube_list_local[side])):
				color = cube_list_local[side][square]
				if color in colors:
					cube_list_local[side][square] = colors.get(color, ' ')
	elif step == 2:
		colors = {'Yellow': 'y', 'Orange': 'o', 'Blue': 'b', 'Red': 'r', 'White': 'w', 'Green': 'g'}
		
		for side in range(len(cube_list_local)):
			for square in range(len(cube_list_local[side])):
				color = cube_list_local[side][square]
				if color in colors:
					cube_list_local[side][square] = colors.get(color, ' ')
	else:
		print('Wrong step in function: coloring')
	
	# print(cube_list_local)
	return cube_list_local


# Оставить поддержку рисовалки
# """
# 		ОТКРЫТИЕ В ОКНЕ
"""

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


# Оставить на всякий поддержку рисовалки
def painting_cube(cube_list):
	'''
	Выдает координаты по №
	'''
	coloring(1)

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

	coloring(2)

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

#"""

# """
# 		ЗАПУСК
"""

'''Запуск по частям. Оставить для проверки
#while True:
print()
#turn_string = 'Iup'#input()
#turn_string = '(IleftIequatorial^2Ileft'Iequatorial^2Ileft'IstandingIleftIstanding')'

#turn_string = 'IupIfrontIrightIdownIbackIleftIequatorialIstandingImiddle'
#up front right down back left equatorial standing middle
#up front right down back left equatorial standing middle
#U F R D B L E S M '

#middle Между left и right
#standing Между front и back
#equatorial Между up и down

#if turn_string == 'exit' or turn_string == 'Exit' or turn_string == 'e':
#	break 
#check_string(turn_string)
print()
#print(return_rubik_cube(turn_string, 1), end = '\n\n')
#print(return_rubik_cube(turn_string, 2), end = '\n\n')
'''


# Запуск Simulation of cube on computer отдельно
# + ВКЛЮЧИТЬ ИМПОРТ ГРАФИКС
#"#""
turn_string = "U2 D2 E2 F2 B2 S2 R2 L2 M2"
rotate_cube(check_string(string), cube_list)

print(list_to_string(cube_list))
#string_to_list(list_to_string(cube_list))

#compare_cube(cube_list, cube_list)

window = gr.GraphWin('Simulation of cube on computer', length, height)

painting_cube(cube_list)
#"#""

# Запуск Simulation of cube on computer через main
#"#""
#turn_string = "U2 D2 E2 F2 B2 S2 R2 L2 M2"	#for check all rotation funtion

#window = gr.GraphWin('Simulation of cube on computer', length, height)
#background_painting('black')

#painting_cube(cube_list)
#"""

cube_list = [
				[	'y', 'y', 'y',  # 0	#top
					'y', 'y', 'y',
					'y', 'y', 'y'],
[	'o', 'o', 'o',  # 1	#left_side
	'o', 'o', 'o',
	'o', 'o', 'o'],
				[	'b', 'b', 'b',  # 2	#front_side
					'b', 'b', 'b',
					'b', 'b', 'b'],
								[	'r', 'r', 'r',  # 3	#right_side
									'r', 'r', 'r',
									'r', 'r', 'r'],
				[	'w', 'w', 'w',  # 4	#bottom
					'w', 'w', 'w',
					'w', 'w', 'w'],

				[	'g', 'g', 'g',  # 5	#back_side
					'g', 'g', 'g',
					'g', 'g', 'g']]

# '''
start_cube_list = [
				[	'y', 'y', 'y',  # 0	#top
					'y', 'y', 'y',
					'y', 'y', 'y'],
[	'o', 'o', 'o',  # 1	#left_side
	'o', 'o', 'o',
	'o', 'o', 'o'],
				[	'b', 'b', 'b',  # 2	#front_side
					'b', 'b', 'b',
					'b', 'b', 'b'],
								[	'r', 'r', 'r',  # 3	#right_side
									'r', 'r', 'r',
									'r', 'r', 'r'],
				[	'w', 'w', 'w',  # 4	#bottom
					'w', 'w', 'w',
					'w', 'w', 'w'],

				[	'g', 'g', 'g',  # 5	#back_side
					'g', 'g', 'g',
					'g', 'g', 'g']]
# '''

turn_string = "U2 D2 E2 F2 B2 S2 R2 L2 M2"  # for check all rotation funtion

"""
#		СОХРАНЕНИЕ В ФАЙЛЫ И ЗАГРУЗКА ИЗ НИХ
#"""

my_cube_string = '''
	·___·yyy·___·
	·___·yyy·___·
	·___·yyy·___·
	·___     ___·
	·ooo·bbb·rrr·
	·oob·rbo·brr·
	·bor·gbo·bro·
	·___     ___·
	·___·www·___·
	·___·www·___·
	·___·rwg·___·
	·___     ___·
	·___·ggg·___·
	·___·ggg·___·
	·___·wgw·___·

'''

num_cube_string = '''
	·___·012·___·
	·___·345·___·
	·___·678·___·
	·___     ___·
	·012·012·012·
	·345·345·345·
	·678·678·678·
	·___     ___·
	·___·012·___·
	·___·345·___·
	·___·678·___·
	·___     ___·
	·___·012·___·
	·___·345·___·
	·___·678·___·

'''


def saving_cube(cube_list_for_saving,
				where_saving = 'Save_to_last',
				with_txt = 'completely',
				turn_string = 'Empty',
				file_type = 'shelf_file'):
	"""
	Добавляет строку с вращениями и куб в txt
	Cохраняет cube_list в cube save
	"""
	# file_type = 'cube_save_py_file'
	
	if 'Cube_saves' not in os.getcwd():
		saving_directory = os.path.join(os.getcwd(), 'Cube_saves')
	else:
		saving_directory = os.getcwd()
	
	if not os.path.exists(saving_directory):
		os.makedirs(saving_directory)
	
	os.chdir(saving_directory)
	
	with_txt = with_txt.lower()
	if with_txt in ['completely', 'c', 'y', 'yes', 'only']:
		saving_file_txt = os.path.join(saving_directory, 'Cube_saves.txt')
		super_cube = list_to_string(cube_list_for_saving)
		cube_saves_file = open(saving_file_txt, 'a')
		
		cube_saves_file.write(where_from_string + '\n\n' +
								turn_string + ')' + '\n\n' +
								super_cube + '\n\n\n\n'
								)
		
		cube_saves_file.close()
	
	if with_txt != 'only':
		if file_type == 'shelf_file':
			shelf_file = shelve.open('cube save')  # Сохранение в shelf_file
			if where_saving in ['Save_to_last', 'Save_to_mine', 'Temporary_cube']:  # , 'Save_start'
				shelf_file[where_saving] = cube_list_for_saving  # Сохранение
			shelf_file.close()
		# Один раз сохранить, а потом закомментить либо оставить и запускать, чтобы точно был начальным #?
		
		# '''
		elif file_type == 'cube_save_py_file':
			
			if not os.path.isfile(os.path.join(saving_directory, 'cube_saves_file.py')):
				cube_save_py_file = open('cube_saves_file.py', 'a')
				if where_saving in ['Save_to_last', 'Save_to_mine', 'Temporary_cube']:  # , 'Save_start'
					if turn_string != 'Empty':
						cube_save_py_file.write('turn_string' + ' = ' + pprint.pformat(turn_string) + ')\n\n')
					cube_save_py_file.write(where_saving + ' = (\n' + pprint.pformat(cube_list_for_saving) + ')\n\n\n\n')
				
				cube_save_py_file.close()
			
			else:
				pass


# import cube_saves_file # Косяк с перезаписью переменных, тк дописывает их, а не изменяет #?


# '''
# Один раз сохранить, а потом закомментить либо оставить и запускать, чтобы точно был начальным #?


# """
#  # saving_cube(cube_list, 'Save_start', 'n', file_type = 'cube_save_py_file')
# saving_cube(cube_list, 'Save_to_last', 'n', file_type = 'cube_save_py_file')
# saving_cube(cube_list, 'Save_to_mine', 'n', file_type = 'cube_save_py_file')


def loading_cube(where_from_loading = 'Loading_from_last', file_type = 'shelf_file'):
	"""
	Загружает cube_list сохранённый в cube save
	Выводит на экран в виде super_cube
	Возвращает загруженый cube_list
	"""
	# file_type = 'cube_save_py_file'
	cube_list_from_save = []
	
	if 'Cube_saves' not in os.getcwd():
		saving_directory = os.path.join(os.getcwd(), 'Cube_saves')
	else:
		saving_directory = os.getcwd()
	
	if not os.path.exists(saving_directory):
		print('Saving directory does not exist. Check and try again.')
		return
	if file_type == 'shelf_file':
		if not (
				os.path.isfile(os.path.join(saving_directory, 'cube save.bak'))
		) and not (
				os.path.isfile(os.path.join(saving_directory, 'cube save.dat'))
		) and not (
				os.path.isfile(os.path.join(saving_directory, 'cube save.dir'))
		):
			print('Saving files does not exist. Check and try again.')
			return
	
	if file_type == 'cube_save_py_file':
		if not os.path.isfile(os.path.join(saving_directory, 'cube_saves_file.py')):
			print('Saving files does not exist. Check and try again.')
			return

	os.chdir(saving_directory)

	if file_type == 'shelf_file':

		if where_from_loading == 'loading_from_last':
			shelf_file = shelve.open('cube save')
			cube_list_from_save = shelf_file['Save_to_last']  # Загрузка
			shelf_file.close()
		elif where_from_loading == 'loading_from_mine':
			shelf_file = shelve.open('cube save')
			cube_list_from_save = shelf_file['Save_to_mine']  # Загрузка
			shelf_file.close()
		elif where_from_loading == 'loading_from_start':
			cube_list_from_save = [start_cube_list[0][:], start_cube_list[1][:], start_cube_list[2][:], start_cube_list[3][:], start_cube_list[4][:], start_cube_list[5][:]]  # а ещё где-то здесь проблема тк он должен не зависимо от сейвов открывать начальный кубик
	
	print(list_to_string(cube_list_from_save))
	
	return cube_list_from_save


if __name__ == '__main__':
	#'''ЗАКРЫТИЕ НА КОМПЬЮТЕРЕ # Выключать для exe #!!!!
	word = 'Exit'
	print()
	input(word)
	#'''


# Временные строки

