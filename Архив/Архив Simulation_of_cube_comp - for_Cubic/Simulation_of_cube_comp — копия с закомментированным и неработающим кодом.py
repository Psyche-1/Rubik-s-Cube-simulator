"""
Записать краткий конспект основных
свойств и функций, чтобы выбрать 
как проще обрабатывать
"""

"""	ЧТО ДОБАВИТЬ:
Добавить в конце сохранение в файл(ы)
строку с поворотами, кубик до и после 
+ может сам куб в питон файле чтобы оттуда сразу открывать
"""

"""
#	РАБОТА СО СТРОКАМИ И СПИСКАМИ
#

string = 'Up'#input()

def check_string(main_string):
	'''
	Проверка какая строка 
	из калькулятора или из блокнота.
	Вывод её в удобном виде и 
	для подачи на вращения кубика
	'''
	'''
	Добавить
	if содержит только из словаря 
		то это нужная строка 
	else:
		print('String contains something else, not only lost of turn)
	'''
	main_string = main_string.strip('()')
	if 'I' in string:
		print('из калькулятора', end = '\n\n')
		main_string = return_rubiks_cube(main_string, 1)
		main_string = main_string.strip()
	else:
		print('из блокнота', end = '\n\n')
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


'''Запуск по частям'''
#while True:
print()
#string = 'IUp'#input()
#string = '(ILeftIEquatorial^2ILeft'IEquatorial^2ILeft'IStandingILeftIStanding')'

#string = 'IUpIFrontIRightIDownIBackILeftIEquatorialIStandingIMiddle'
#UP FRONT RIGHT DOWN BACK LEFT EQUATORIAL STANDING MIDDLE
#up front right down back left equatorial standing middle

#if string == 'exit' or string == 'Exit' or string == 'e':
#	break 
#check_string(string)
print()
#print(return_rubiks_cube(string, 1), end = '\n\n')
#print(return_rubiks_cube(string, 2), end = '\n\n')



def string_to_list(super_cube):
	'''
	из строки super_cube
	делает cube_list 
	'''
	super_cube = super_cube.replace('_', '')
	super_cube = super_cube.replace('\n', '')
	super_cube = super_cube.replace(' ', '')
	cube_list2 = super_cube.split('·')
	
	for i in range(len(cube_list2) - 23):
		if cube_list2[i] == '':
			del cube_list2[i]
	
	for i in range(len(cube_list2) - 10):
		if cube_list2[i] == '':
			del cube_list2[i]
	
	for i in range(len(cube_list2) - 5):
		if cube_list2[i] == '':
			del cube_list2[i]
	
	print(len(cube_list2))
	#cube_list3 = cube_list
	#cube_list3[0][0] = cube_list2[0][0]
	print(str(cube_list2))
	
	#return cube_list2



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


def find_different():
	'''
	находит и выводит разницу между 
	двумя кубиками до и после вращения
	'''
	pass
"""


"""
#	ВРАЩЕНИЕ КУБИКА
#

def UP(cube, sign):
	def up1(cube):
		print('up1')
		#t1
	def up2(cube):
		print('up2')
		up1(cube)
		up1(cube)
	def up·1(cube):
		print('up-1')
		#t1

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
		print('front1')
		#t1
	def front2(cube):
		print('front2')
		front1(cube)
		front1(cube)
	def front·1(cube):
		print('front-1')
		#t1

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
		print('right1')
		#t1
	def right2(cube):
		print('right2')
		right1(cube)
		right1(cube)
	def right·1(cube):
		print('right-1')
		#t1

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
		print('down1')
		#t1
	def down2(cube):
		print('down2')
		down1(cube)
		down1(cube)
	def down·1(cube):
		print('down-1')
		#t1

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
		print('back1')
		#t1
	def back2(cube):
		print('back2')
		back1(cube)
		back1(cube)
	def back·1(cube):
		print('back-1')
		#t1

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
		print('left1')
		#t1
	def left2(cube):
		print('left2')
		left1(cube)
		left1(cube)
	def left·1(cube):
		print('left-1')
		#t1

	if sign == "'":
		left·1(cube)
	elif sign == '2':
		left2(cube)
	elif sign == '':
		left1(cube)
	else:
		print('sign error')

def EQUATORIAL(cube, sign):
	def equatorial1(cube):
		print('equatorial1')
		#t1
	def equatorial2(cube):
		print('equatorial2')
		equatorial1(cube)
		equatorial1(cube)
	def equatorial·1(cube):
		print('equatorial-1')
		#t1

	if sign == "'":
		equatorial·1(cube)
	elif sign == '2':
		equatorial2(cube)
	elif sign == '':
		equatorial1(cube)
	else:
		print('sign error')

def STANDING(cube, sign):
	def standing1(cube):
		print('standing1')
		#t1
	def standing2(cube):
		print('standing2')
		standing1(cube)
		standing1(cube)
	def standing·1(cube):
		print('standing-1')
		#t1

	if sign == "'":
		standing·1(cube)
	elif sign == '2':
		standing2(cube)
	elif sign == '':
		standing1(cube)
	else:
		print('sign error')


def MIDDLE(cube, sign):
	def middle1(cube):
		print('middle1')
		t1, t2, t3 = cube[0][1], cube[0][4], cube[0][7]
		cube[0][1], cube[0][4], cube[0][7] = cube[2][1], cube[2][4], cube[2][7]
		cube[2][1], cube[2][4], cube[2][7] = cube[4][1], cube[4][4], cube[4][7]
		cube[4][1], cube[4][4], cube[4][7] = cube[5][1], cube[5][4], cube[5][7]
		cube[5][1], cube[5][4], cube[5][7] = t1, t2, t3
	def middle2(cube):
		print('middle2')
		middle1(cube)
		middle1(cube)
	def middle·1(cube):
		print('middle-1')
		t1, t2, t3 = cube[5][1], cube[5][4], cube[5][7]
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

'''
 0
123
 4
 5
'''
cube_list = [
				['y','y','y',	#0	#0,1,2
				 'y','y','y',		#3,4,5
		 		 'y','y','y'],		#6,7,8
['o','o','o',	#1
 'o','o','o',
 'o','o','o'],
				['b','b','b',	#2
				 'b','b','b',
				 'b','b','b'],
								['r','r','r',	#3
								 'r','r','r',
								 'r','r','r'],
				['w','w','w',	#4
				 'w','w','w',
				 'w','w','w'],

				['g','g','g',	#5
				 'g','g','g',
				 'g','g','g']]


def rotate_cube(turn_list, cube_list):
	'''
	собирает все вращения вместе 
	и переводит из одного вида в 
	другой (написанного в калькуляторе 
	или скопированного из блокнота 
	и передает их другим функциям 
	для вращения кубика и печати его)
	
	МОЖЕТ ПЕРЕПИСАТЬ ЧЕРЕЗ РЕГУЛЯРНЫЕ ВЫРАЖЕНИЯ
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
"""


"""
#	ЗАПУСК
#

#print(super_cube)
#print(str(cube_list))
print()

rotate_cube(check_string(string), cube_list)

print(list_to_string(cube_list))
string_to_list(list_to_string(cube_list))
#"""


"""
#	ОТКРЫТИЕ В ОКНЕ
"""
import graphics as gr

length = 800
height = 900
window = gr.GraphWin('Simulation of cube computer', length, height)


def painting_cube():
	size = 100
	width = 5
	x, y = 100, height/2 - 2*size
	def side(x, y, size):
		side =  gr.Rectangle(gr.Point(x, y), gr.Point(x + 2*size, y + 2*size))
		side.setFill('gray')
		side.setWidth(width)
		side.draw(window)

	side(x, y, size)											#left_side
	side(x + 2*(size + width), y, size)							#front_side
	side(x + 4*(size + width), y, size)							#right_side
	side(x + 2*(size + width), y - 2*(size + width), size)		#top
	side(x + 2*(size + width), y + 2*(size + width), size)		#bottom
	side(x + 2*(size + width), y + 4*(size + width), size)		#back_side


painting_cube()





"""
Варианты хранения: 
#1 с подписями
cube_list = [
[
['y','y','y'],
['y','y','y'],
['y','y','y']],#top
[
#left_side	 front_side	right_side
['o','o','o'],['b','b','b'],['r','r','r'],
['o','o','o'],['b','b','b'],['r','r','r'],
['o','o','o'],['b','b','b'],['r','r','r']],
[
['w','w','w'],
['w','w','w'],
['w','w','w']],#bottom
[
['g','g','g'],
['g','g','g'],
['g','g','g']]]#back_side


#2
cube_list = [
['y','y','y',
'y','y','y',
'y','y','y'],#top 
#left_side	 front_side	right_side
['o','o','o','b','b','b','r','r','r',
'o','o','o','b','b','b','r','r','r',
'o','o','o','b','b','b','r','r','r'],
['w','w','w',
'w','w','w',
'w','w','w'],#bottom
['g','g','g',
'g','g','g',
'g','g','g']]#back_side



#3 с подписями
cube_list = [
['y','y','y',
'y','y','y',
'y','y','y'],#top
['o','o','o',
'o','o','o',
'o','o','o'],#left_side
['b','b','b',
'b','b','b',
'b','b','b'],#front_side
['r','r','r',
'r','r','r',
'r','r','r'],#right_side
['w','w','w',
'w','w','w',
'w','w','w'],#bottom
['g','g','g',
'g','g','g',
'g','g','g']]#back_side

#3.1
cube_list = [
				['y','y','y',
				 'y','y','y',
		 		 'y','y','y'],
['o','o','o',
 'o','o','o',
 'o','o','o'],
				['b','b','b',
				 'b','b','b',
				 'b','b','b'],
								['r','r','r',
								 'r','r','r',
								 'r','r','r'],
				['w','w','w',
				 'w','w','w',
				 'w','w','w'],

				['g','g','g',
				 'g','g','g',
				 'g','g','g']]

#3.2 с подписями
'''
 0
123
 4
 5
'''
cube_list = [
				['y','y','y',	#0	#0,1,2
				 'y','y','y',		#3,4,5
		 		 'y','y','y'],		#6,7,8
['o','o','o',	#1
 'o','o','o',
 'o','o','o'],
				['b','b','b',	#2
				 'b','b','b',
				 'b','b','b'],
								['r','r','r',	#3
								 'r','r','r',
								 'r','r','r'],
				['w','w','w',	#4
				 'w','w','w',
				 'w','w','w'],

				['g','g','g',	#5
				 'g','g','g',
				 'g','g','g']]


#то как выводиться кубик
super_cube = (
'''
	·___·yyy·___·
	·___·yyy·___·
	·___·yyy·___·
	·___	 ___·
	·ooo·bbb·rrr·
	·ooo·bbb·rrr·
	·ooo·bbb·rrr·
	·___	 ___·
	·___·www·___·
	·___·www·___·
	·___·www·___·
	·___	 ___·
	·___·ggg·___·
	·___·ggg·___·
	·___·ggg·___·
''')

super_cube = ('\n' +
'	·___·' +  cube_list[0][0] + cube_list[0][1] + cube_list[0][2] + '·___·' + '\n' +
'	·___·' +  cube_list[0][3] + cube_list[0][4] + cube_list[0][5] + '·___·' + '\n' + 
'	·___·' +  cube_list[0][6] + cube_list[0][7] + cube_list[0][8] + '·___·' + '\n' +
'	·___	 ___·' + '\n' +
'	·' + cube_list[1][0] + cube_list[1][1] + cube_list[1][2] + '·' +
cube_list[2][0] + cube_list[2][1] + cube_list[2][2] + '·' +
cube_list[3][0] + cube_list[3][1] + cube_list[3][2] + '·' +
'\n' +
'	·' + cube_list[1][3] + cube_list[1][4] + cube_list[1][5] + '·' +
cube_list[2][3] + cube_list[2][4] + cube_list[2][5] + '·' +
cube_list[3][3] + cube_list[3][4] + cube_list[3][5] + '·' +
'\n' +
'	·' + cube_list[1][6] + cube_list[1][7] + cube_list[1][8] + '·' +
cube_list[2][6] + cube_list[2][7] + cube_list[2][8] + '·' +
cube_list[3][6] + cube_list[3][7] + cube_list[3][8] + '·' +
'\n' + '	·___	 ___·' + '\n' +
'	·___·' +  cube_list[4][0] + cube_list[4][1] + cube_list[4][2] + '·___·' + '\n' +
'	·___·' +  cube_list[4][3] + cube_list[4][4] + cube_list[4][5] + '·___·' + '\n' + 
'	·___·' +  cube_list[4][6] + cube_list[4][7] + cube_list[4][8] + '·___·' + '\n' +
'	·___	 ___·' + '\n' +
'	·___·' +  cube_list[5][0] + cube_list[5][1] + cube_list[5][2] + '·___·' + '\n' +
'	·___·' +  cube_list[5][3] + cube_list[5][4] + cube_list[5][5] + '·___·' + '\n' + 
'	·___·' +  cube_list[5][6] + cube_list[5][7] + cube_list[5][8] + '·___·' + '\n'
)

"""

"""
	НЕ РАБОТАЮЩИЙ КОД
def printing_cube():
	#Не пашет
	i = 0
	for side in cube_list:
		for square in side:
			i += 1
			print(square, end = '')
			if i == 3:
				print()
				i = 0
		print()
	'''
	'''
	i,k = 0, 0
	for side in cube_list:
		for square in side:
			i += 1
			k += 1
			print(square, end = '')
			if i == 3:
				print()
				i = 0
		break
	print()
"""

#'''ЗАКРЫТИЕ НА КОМПЬЮТЕРЕ
print()
input('Exit')
#'''
