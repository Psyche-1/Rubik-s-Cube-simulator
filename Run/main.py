"""Оставить описание функций проги: #?
1 Переключение между 3 режимами:
	1.1 Ввод кубика кнопками
	1.2 Ввод списка движений и вращение при нажати на Enter
	1.3 Вращение кубика сразу при нажатии на кнопки
2 Сохранение кубика:
	2.1 В двоичные файлы-хранилище (в той же папке в папку Cube_saves): сами кубики для загрузки. С выбором: LAST и MINE
	2.2 В txt файл: строку с вращениями и куб (в виде my_cube_string)
3 Загрузка и вывод кубика из сохранения. С выбором: START, LAST и MINE
Доп:
	Вывод основных моментов в sms_as_cmd с его очисткой и выключением
	Работа с буфером обмена с помощью кнопок

Тех_док: #?
Python 3.7.2
Pyside2 VERSION 5.13.1

Дата последней редакции кода: 27.09.2019. Версия 0.8.1 main						ПРОВЕРИТЬ НА БАГИ И ДОДЕЛАТЬ #?
Дата последней редакции оформления: 26.09.2019. Версия 0.1.7 All_Cube

Мне делать:
Возможно:
	Добавить светлую тему #?
	Cделать то же самое на телефоне #?

Добавить:
	Проверять все принты при запуске: Отправляють print в sms_as_cmd_display (sms_as_cmd_display = print) #?

	#Откуда: Возможно вставить это в bp_enter # ??

	из SCube.check_string
	принт('Строка не подходит для вращения кубика')
	принт(wherefrom_string, end = '\n\n') х2


	из SCube.rotate_cube
	принт('turn: ' + turn + ' is not turn')


	из SCube.loading_cube
	принт('Saving directory does not exist. Check and try again.')
	


	Проверять если все 3 сейва, если нет, то записать пустые чтобы можно было запустить
		или написать, что нет такого сейва #????

	Кат и паст доделать
		чтобы вращался сразу при изменении строки
	
	Доделать новые функции из нового олл_куб
	
	
	Проверить деф сейв() и деф лоад здесь и в фор_кубик:
		Использовать = лист(старт_куб_лист)
		и проверить где ещё не обработка, а копирование
		
"""
# ! python3

import sys

from functools import partial

from PySide2 import QtWidgets

from All_Cube import Ui_Window

# Найти как передать переменную в Simulation_of_cube_comp word = 'Open' #?
import for_Cubic as SCube

# Create application
app = QtWidgets.QApplication(sys.argv)

# Create window and init UI
Window = QtWidgets.QWidget()
ui = Ui_Window()
ui.setupUi(Window)
Window.show()

# Hook logic

# ALL variables
# variables for Sms as cmd setup
text_for_sms_as_cmd = '''For convenience, expand the window to full screen.

Also save last and mine cube before loading it'''

sms_as_cmd_turned_on = True

text_edit_style_sheet_on = (
			"QTextEdit {\n"
			"  color: gray;\n"
			"  font-size: 14px;\n"
			"  border: 2px solid black;\n"
			"  selection-background-color: green;\n"
			"}")

text_edit_style_sheet_off = (
		"QTextEdit {\n"
		"  color: gray;\n"
		"  font-size: 14px;\n"
		"  border: 2px solid black;\n"
		"  selection-background-color: green;\n"
		"}")

# variables for Choose mode
Entering_cube = False
Entering_cube_for_loading = False
Typing_rotate = False
Rotating_immediately = False

choose_mode_radio_buttons_style_sheet_on = (
	"QRadioButton{\n"
	"  color: green;\n"
	"  font-size: 14px;\n"
	"  font-weight: bold;\n"
	"  border: none;\n"
	"  text-align: center;\n"
	"}\n"
	"\n"
	"QRadioButton:pressed {\n"
	"  color: gray;\n"
	"}")

choose_mode_radio_buttons_style_sheet_off = (
	"QRadioButton{\n"
	"  color: rgb(160, 0, 0);\n"
	"  font-size: 14px;\n"
	"  font-weight: bold;\n"
	"  border: none;\n"
	"  text-align: center;\n"
	"}\n"
	"\n"
	"QRadioButton:pressed {\n"
	"  color: gray;\n"
	"}")


# variables cube_list
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


my_cube_string = '''
	·___·yyy·___·
	·___·yyy·___·
	·___·yyy·___·
	·___	 ___·
	·ooo·bbb·rrr·
	·oob·rbo·brr·
	·bor·gbo·bro·
	·___	 ___·
	·___·www·___·
	·___·www·___·
	·___·rwg·___·
	·___	 ___·
	·___·ggg·___·
	·___·ggg·___·
	·___·wgw·___·

'''

# variables for def coloring buttons
b_coloring = ''
c_coloring = ''

# variables for def as calculator buttons
last_turn = ''

# variables for Choose Save or Load Cube
saving_to_last = False
saving_to_mine = False

Saving_in_Temporary_cube = False


loading_from_last = False
loading_from_start = False
loading_from_mine = False

save_or_load_radio_buttons_style_sheet_on = (
	"QRadioButton{\n"
	"  spacing: 2;\n"
	"  background-color: black;\n"
	"  color: green;\n"
	"  font-size: 8px;\n"
	"  font-weight: normal;\n"
	"}\n"
	"\n"
	"QRadioButton::indicator {\n"
	"  width: 8px;\n"
	"  height: 8px;\n"
	"}\n"
	"\n"
	"QRadioButton:pressed {\n"
	"	color: gray;\n"
	"}")

save_or_load_radio_buttons_style_sheet_off = (
	"QRadioButton{\n"
	"  spacing: 2;\n"
	"  background-color: black;\n"
	"  color: rgb(160, 0, 0);\n"
	"  font-size: 8px;\n"
	"  font-weight: normal;\n"
	"}\n"
	"\n"
	"QRadioButton::indicator {\n"
	"  width: 8px;\n"
	"  height: 8px;\n"
	"}\n"
	"\n"
	"QRadioButton:pressed {\n"
	"	color: gray;\n"
	"}")


# ALL def

# def sms_as_cmd
def sms_as_cmd_turn_on():
	global sms_as_cmd_turned_on
	
	if ui.sms_as_cmd_on.isChecked():
		sms_as_cmd_turned_on = True
		ui.sms_as_cmd_on.setText('ON')
	
	elif not ui.sms_as_cmd_on.isChecked():
		sms_as_cmd_turned_on = False
		ui.sms_as_cmd_on.setText('OFF')
		ui.sms_as_cmd.clear()
		ui.sms_as_cmd.setStyleSheet(text_edit_style_sheet_off)
		
		ui.sms_as_cmd_button.setStyleSheet(
			"QPushButton{\n"
			"  color: black;\n"
			"  background-color: black;\n"
			"  font-size: 11px;\n"
			"  font-weight: normal;\n"
			"  border: none;\n"
			"  text-align: center;\n"
			"}\n"
			"\n"
			"QPushButton:hover {\n"
			"  background-color: rgb(10, 10, 10);\n"
			"}\n"
			"\n"
			"QPushButton:pressed {\n"
			"  background-color:  rgb(20, 20, 20);\n"
			"}")


def sms_as_cmd_display():
	"""print sms to as_cmd"""
	if sms_as_cmd_turned_on:
		ui.sms_as_cmd.setStyleSheet(text_edit_style_sheet_on)
		
		global text_for_sms_as_cmd
		
		if text_for_sms_as_cmd == 'For convenience, expand the window to full screen':
			text_from_sms_as_cmd = ''
		else:
			text_from_sms_as_cmd = ui.sms_as_cmd.toPlainText()
		
		all_text_for_sms_as_cmd = text_from_sms_as_cmd + text_for_sms_as_cmd
		ui.sms_as_cmd.setText(all_text_for_sms_as_cmd)
		# ui.sms_as_cmd.setText(text_for_sms_as_cmd)
		
		ui.sms_as_cmd_button.setStyleSheet(
			"QPushButton{\n"
			"  color: gray;\n"
			"  background-color: black;\n"
			"  font-size: 11px;\n"
			"  font-weight: normal;\n"
			"  border: none;\n"
			"  text-align: center;\n"
			"}\n"
			"\n"
			"QPushButton:hover {\n"
			"  background-color: rgb(10, 10, 10);\n"
			"}\n"
			"\n"
			"QPushButton:pressed {\n"
			"  background-color:  rgb(20, 20, 20);\n"
			"}")
	else:
		pass


def sms_as_cmd_undisplay():
	ui.sms_as_cmd.clear()
	ui.sms_as_cmd.setStyleSheet(text_edit_style_sheet_off)
	
	ui.sms_as_cmd_button.setStyleSheet(
		"QPushButton{\n"
		"  color: black;\n"
		"  background-color: black;\n"
		"  font-size: 11px;\n"
		"  font-weight: normal;\n"
		"  border: none;\n"
		"  text-align: center;\n"
		"}\n"
		"\n"
		"QPushButton:hover {\n"
		"  background-color: rgb(10, 10, 10);\n"
		"}\n"
		"\n"
		"QPushButton:pressed {\n"
		"  background-color:  rgb(20, 20, 20);\n"
		"}")


print(text_for_sms_as_cmd)
sms_as_cmd_display()

ui.sms_as_cmd_on.clicked.connect(sms_as_cmd_turn_on)
ui.sms_as_cmd_button.clicked.connect(sms_as_cmd_undisplay)

'''
#		FOR ENTERING CUBE
'''


# Choose mode
# """

def choose_mode():
	global Entering_cube
	global Typing_rotate
	global Rotating_immediately
	global text_for_sms_as_cmd
	global b_coloring
	global c_coloring
	
	if ui.enter_cube.isChecked():
		text_for_sms_as_cmd = 'Using Enter cube\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_display()
		
		ui.enter_cube.setStyleSheet(choose_mode_radio_buttons_style_sheet_on)
	
	elif not ui.enter_cube.isChecked():
		b_coloring = ''
		c_coloring = ''
		
		ui.enter_cube.setStyleSheet(choose_mode_radio_buttons_style_sheet_off)
	
	Entering_cube = ui.enter_cube.isChecked()
	
	if ui.type_rotate.isChecked():
		text_for_sms_as_cmd = 'Using Typing rotate\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_display()
		
		ui.type_rotate.setStyleSheet(choose_mode_radio_buttons_style_sheet_on)
	
	elif not ui.type_rotate.isChecked():
		ui.type_rotate.setStyleSheet(choose_mode_radio_buttons_style_sheet_off)
	
	Typing_rotate = ui.type_rotate.isChecked()
	
	if ui.rotate_immediately.isChecked():
		text_for_sms_as_cmd = 'Using Rotate immediately \n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_display()
		
		ui.rotate_immediately.setStyleSheet(choose_mode_radio_buttons_style_sheet_on)
	
	elif not ui.rotate_immediately.isChecked():
		ui.rotate_immediately.setStyleSheet(choose_mode_radio_buttons_style_sheet_off)
	
	Rotating_immediately = ui.rotate_immediately.isChecked()


ui.enter_cube.clicked.connect(choose_mode)
ui.type_rotate.clicked.connect(choose_mode)
ui.rotate_immediately.clicked.connect(choose_mode)


# """


# def coloring buttons

def bp_coloring(b_color):
	if Entering_cube or Entering_cube_for_loading:
		global b_coloring
		global c_coloring
		
		if b_color == 'Yellow':
			c_coloring = 'y'
			b_coloring = (
				"QPushButton{\n"
				"  color: rgb(183, 180, 0);\n"
				"  background-color: rgb(183, 180, 0);\n"
				"  width: 50px;\n"
				"  height: 50px;\n"
				"}\n"
				"\n"
				"QPushButton:hover {\n"
				"  color: gray;\n"
				"  background-color: gray;\n"
				"}\n"
				"\n"
				"QPushButton:pressed {\n"
				"  color:yellow;\n"
				"  background-color: yellow;\n"
				"}")
		
		elif b_color == 'Orange':
			c_coloring = 'o'
			b_coloring = (
				"QPushButton{\n"
				"  color: rgb(193, 122, 0);\n"
				"  background-color: rgb(193, 122, 0);\n"
				"  width: 50px;\n"
				"  height: 50px;\n"
				"}\n"
				"\n"
				"QPushButton:hover {\n"
				"  color: gray;\n"
				"  background-color: gray;\n"
				"}\n"
				"\n"
				"QPushButton:pressed {\n"
				"  color: orange;\n"
				"  background-color: orange;\n"
				"}")
		
		elif b_color == 'Blue':
			c_coloring = 'b'
			b_coloring = (
				"QPushButton{\n"
				"  color: rgb(0, 0, 170);\n"
				"  background-color: rgb(0, 0, 170);\n"
				"  width: 50px;\n"
				"  height: 50px;\n"
				"}\n"
				"\n"
				"QPushButton:hover {\n"
				"  color: gray ;\n"
				"  background-color: gray;\n"
				"}\n"
				"\n"
				"QPushButton:pressed {\n"
				"  color: blue;\n"
				"  background-color: blue;\n"
				"}")
		
		elif b_color == 'Red':
			c_coloring = 'r'
			b_coloring = (
				"QPushButton{\n"
				"  color: rgb(160, 0, 0);\n"
				"  background-color: rgb(160, 0, 0);\n"
				"  width: 50px;\n"
				"  height: 50px;\n"
				"}\n"
				"\n"
				"QPushButton:hover {\n"
				"  color: gray;\n"
				"  background-color: gray;\n"
				"}\n"
				"\n"
				"QPushButton:pressed {\n"
				"  color: red ;\n"
				"  background-color: red;\n"
				"}")
		
		elif b_color == 'White':
			c_coloring = 'w'
			b_coloring = (
				"QPushButton{\n"
				"  color: silver ;\n"
				"  background-color: silver;\n"
				"  width: 50px;\n"
				"  height: 50px;\n"
				"}\n"
				"\n"
				"QPushButton:hover {\n"
				"  color: gray;\n"
				"  background-color: gray;\n"
				"\n"
				"}\n"
				"\n"
				"QPushButton:pressed {\n"
				"  color: white;\n"
				"  background-color: white;\n"
				"}")
		
		elif b_color == 'Green':
			c_coloring = 'g'
			b_coloring = (
				"QPushButton{\n"
				"  color: green;\n"
				"  background-color: green;\n"
				"  width: 50px;\n"
				"  height: 50px;\n"
				"}\n"
				"\n"
				"QPushButton:hover {\n"
				"  color: gray;\n"
				"  background-color: gray;\n"
				"}\n"
				"\n"
				"QPushButton:pressed {\n"
				"  color: rgb(0, 160, 0);\n"
				"  background-color: rgb(0, 160, 0);\n"
				"}")


# def side square buttons coloring
# '''
def bp_ss(side_square):
	global text_for_sms_as_cmd
	
	if Entering_cube or Entering_cube_for_loading:
		if b_coloring == '':
			text_for_sms_as_cmd = 'Choose color\n\n'
			print(text_for_sms_as_cmd, end = '')
			sms_as_cmd_display()
		else:
			if side_square == '00':
				ui.side_0_square_0.setStyleSheet(b_coloring)
				cube_list[0][0] = c_coloring
			elif side_square == '01':
				ui.side_0_square_1.setStyleSheet(b_coloring)
				cube_list[0][1] = c_coloring
			elif side_square == '02':
				ui.side_0_square_2.setStyleSheet(b_coloring)
				cube_list[0][2] = c_coloring
			elif side_square == '03':
				ui.side_0_square_3.setStyleSheet(b_coloring)
				cube_list[0][3] = c_coloring
			elif side_square == '04':
				ui.side_0_square_4.setStyleSheet(b_coloring)
				cube_list[0][4] = c_coloring
			elif side_square == '05':
				ui.side_0_square_5.setStyleSheet(b_coloring)
				cube_list[0][5] = c_coloring
			elif side_square == '06':
				ui.side_0_square_6.setStyleSheet(b_coloring)
				cube_list[0][6] = c_coloring
			elif side_square == '07':
				ui.side_0_square_7.setStyleSheet(b_coloring)
				cube_list[0][7] = c_coloring
			elif side_square == '08':
				ui.side_0_square_8.setStyleSheet(b_coloring)
				cube_list[0][8] = c_coloring
			
			elif side_square == '10':
				ui.side_1_square_0.setStyleSheet(b_coloring)
				cube_list[1][0] = c_coloring
			elif side_square == '11':
				ui.side_1_square_1.setStyleSheet(b_coloring)
				cube_list[1][1] = c_coloring
			elif side_square == '12':
				ui.side_1_square_2.setStyleSheet(b_coloring)
				cube_list[1][2] = c_coloring
			elif side_square == '13':
				ui.side_1_square_3.setStyleSheet(b_coloring)
				cube_list[1][3] = c_coloring
			elif side_square == '14':
				ui.side_1_square_4.setStyleSheet(b_coloring)
				cube_list[1][4] = c_coloring
			elif side_square == '15':
				ui.side_1_square_5.setStyleSheet(b_coloring)
				cube_list[1][5] = c_coloring
			elif side_square == '16':
				ui.side_1_square_6.setStyleSheet(b_coloring)
				cube_list[1][6] = c_coloring
			elif side_square == '17':
				ui.side_1_square_7.setStyleSheet(b_coloring)
				cube_list[1][7] = c_coloring
			elif side_square == '18':
				ui.side_1_square_8.setStyleSheet(b_coloring)
				cube_list[1][8] = c_coloring
			
			elif side_square == '20':
				ui.side_2_square_0.setStyleSheet(b_coloring)
				cube_list[2][0] = c_coloring
			elif side_square == '21':
				ui.side_2_square_1.setStyleSheet(b_coloring)
				cube_list[2][1] = c_coloring
			elif side_square == '22':
				ui.side_2_square_2.setStyleSheet(b_coloring)
				cube_list[2][2] = c_coloring
			elif side_square == '23':
				ui.side_2_square_3.setStyleSheet(b_coloring)
				cube_list[2][3] = c_coloring
			elif side_square == '24':
				ui.side_2_square_4.setStyleSheet(b_coloring)
				cube_list[2][4] = c_coloring
			elif side_square == '25':
				ui.side_2_square_5.setStyleSheet(b_coloring)
				cube_list[2][5] = c_coloring
			elif side_square == '26':
				ui.side_2_square_6.setStyleSheet(b_coloring)
				cube_list[2][6] = c_coloring
			elif side_square == '27':
				ui.side_2_square_7.setStyleSheet(b_coloring)
				cube_list[2][7] = c_coloring
			elif side_square == '28':
				ui.side_2_square_8.setStyleSheet(b_coloring)
				cube_list[2][8] = c_coloring
			
			elif side_square == '30':
				ui.side_3_square_0.setStyleSheet(b_coloring)
				cube_list[3][0] = c_coloring
			elif side_square == '31':
				ui.side_3_square_1.setStyleSheet(b_coloring)
				cube_list[3][1] = c_coloring
			elif side_square == '32':
				ui.side_3_square_2.setStyleSheet(b_coloring)
				cube_list[3][2] = c_coloring
			elif side_square == '33':
				ui.side_3_square_3.setStyleSheet(b_coloring)
				cube_list[3][3] = c_coloring
			elif side_square == '34':
				ui.side_3_square_4.setStyleSheet(b_coloring)
				cube_list[3][4] = c_coloring
			elif side_square == '35':
				ui.side_3_square_5.setStyleSheet(b_coloring)
				cube_list[3][5] = c_coloring
			elif side_square == '36':
				ui.side_3_square_6.setStyleSheet(b_coloring)
				cube_list[3][6] = c_coloring
			elif side_square == '37':
				ui.side_3_square_7.setStyleSheet(b_coloring)
				cube_list[3][7] = c_coloring
			elif side_square == '38':
				ui.side_3_square_8.setStyleSheet(b_coloring)
				cube_list[3][8] = c_coloring
			
			elif side_square == '40':
				ui.side_4_square_0.setStyleSheet(b_coloring)
				cube_list[4][0] = c_coloring
			elif side_square == '41':
				ui.side_4_square_1.setStyleSheet(b_coloring)
				cube_list[4][1] = c_coloring
			elif side_square == '42':
				ui.side_4_square_2.setStyleSheet(b_coloring)
				cube_list[4][2] = c_coloring
			elif side_square == '43':
				ui.side_4_square_3.setStyleSheet(b_coloring)
				cube_list[4][3] = c_coloring
			elif side_square == '44':
				ui.side_4_square_4.setStyleSheet(b_coloring)
				cube_list[4][4] = c_coloring
			elif side_square == '45':
				ui.side_4_square_5.setStyleSheet(b_coloring)
				cube_list[4][5] = c_coloring
			elif side_square == '46':
				ui.side_4_square_6.setStyleSheet(b_coloring)
				cube_list[4][6] = c_coloring
			elif side_square == '47':
				ui.side_4_square_7.setStyleSheet(b_coloring)
				cube_list[4][7] = c_coloring
			elif side_square == '48':
				ui.side_4_square_8.setStyleSheet(b_coloring)
				cube_list[4][8] = c_coloring
			
			elif side_square == '50':
				ui.side_5_square_0.setStyleSheet(b_coloring)
				cube_list[5][0] = c_coloring
			elif side_square == '51':
				ui.side_5_square_1.setStyleSheet(b_coloring)
				cube_list[5][1] = c_coloring
			elif side_square == '52':
				ui.side_5_square_2.setStyleSheet(b_coloring)
				cube_list[5][2] = c_coloring
			elif side_square == '53':
				ui.side_5_square_3.setStyleSheet(b_coloring)
				cube_list[5][3] = c_coloring
			elif side_square == '54':
				ui.side_5_square_4.setStyleSheet(b_coloring)
				cube_list[5][4] = c_coloring
			elif side_square == '55':
				ui.side_5_square_5.setStyleSheet(b_coloring)
				cube_list[5][5] = c_coloring
			elif side_square == '56':
				ui.side_5_square_6.setStyleSheet(b_coloring)
				cube_list[5][6] = c_coloring
			elif side_square == '57':
				ui.side_5_square_7.setStyleSheet(b_coloring)
				cube_list[5][7] = c_coloring
			elif side_square == '58':
				ui.side_5_square_8.setStyleSheet(b_coloring)
				cube_list[5][8] = c_coloring


# '''


# Using coloring buttons
ui.yellow_button.clicked.connect(partial(bp_coloring, 'Yellow'))
ui.orange_button.clicked.connect(partial(bp_coloring, 'Orange'))
ui.blue_button.clicked.connect(partial(bp_coloring, 'Blue'))
ui.red_button.clicked.connect(partial(bp_coloring, 'Red'))
ui.white_button.clicked.connect(partial(bp_coloring, 'White'))
ui.green_button.clicked.connect(partial(bp_coloring, 'Green'))

# Using side square buttons coloring
ui.side_0_square_0.clicked.connect(partial(bp_ss, '00'))
ui.side_0_square_1.clicked.connect(partial(bp_ss, '01'))
ui.side_0_square_2.clicked.connect(partial(bp_ss, '02'))
ui.side_0_square_3.clicked.connect(partial(bp_ss, '03'))
ui.side_0_square_4.clicked.connect(partial(bp_ss, '04'))
ui.side_0_square_5.clicked.connect(partial(bp_ss, '05'))
ui.side_0_square_6.clicked.connect(partial(bp_ss, '06'))
ui.side_0_square_7.clicked.connect(partial(bp_ss, '07'))
ui.side_0_square_8.clicked.connect(partial(bp_ss, '08'))

ui.side_1_square_0.clicked.connect(partial(bp_ss, '10'))
ui.side_1_square_1.clicked.connect(partial(bp_ss, '11'))
ui.side_1_square_2.clicked.connect(partial(bp_ss, '12'))
ui.side_1_square_3.clicked.connect(partial(bp_ss, '13'))
ui.side_1_square_4.clicked.connect(partial(bp_ss, '14'))
ui.side_1_square_5.clicked.connect(partial(bp_ss, '15'))
ui.side_1_square_6.clicked.connect(partial(bp_ss, '16'))
ui.side_1_square_7.clicked.connect(partial(bp_ss, '17'))
ui.side_1_square_8.clicked.connect(partial(bp_ss, '18'))

ui.side_2_square_0.clicked.connect(partial(bp_ss, '20'))
ui.side_2_square_1.clicked.connect(partial(bp_ss, '21'))
ui.side_2_square_2.clicked.connect(partial(bp_ss, '22'))
ui.side_2_square_3.clicked.connect(partial(bp_ss, '23'))
ui.side_2_square_4.clicked.connect(partial(bp_ss, '24'))
ui.side_2_square_5.clicked.connect(partial(bp_ss, '25'))
ui.side_2_square_6.clicked.connect(partial(bp_ss, '26'))
ui.side_2_square_7.clicked.connect(partial(bp_ss, '27'))
ui.side_2_square_8.clicked.connect(partial(bp_ss, '28'))

ui.side_3_square_0.clicked.connect(partial(bp_ss, '30'))
ui.side_3_square_1.clicked.connect(partial(bp_ss, '31'))
ui.side_3_square_2.clicked.connect(partial(bp_ss, '32'))
ui.side_3_square_3.clicked.connect(partial(bp_ss, '33'))
ui.side_3_square_4.clicked.connect(partial(bp_ss, '34'))
ui.side_3_square_5.clicked.connect(partial(bp_ss, '35'))
ui.side_3_square_6.clicked.connect(partial(bp_ss, '36'))
ui.side_3_square_7.clicked.connect(partial(bp_ss, '37'))
ui.side_3_square_8.clicked.connect(partial(bp_ss, '38'))

ui.side_4_square_0.clicked.connect(partial(bp_ss, '40'))
ui.side_4_square_1.clicked.connect(partial(bp_ss, '41'))
ui.side_4_square_2.clicked.connect(partial(bp_ss, '42'))
ui.side_4_square_3.clicked.connect(partial(bp_ss, '43'))
ui.side_4_square_4.clicked.connect(partial(bp_ss, '44'))
ui.side_4_square_5.clicked.connect(partial(bp_ss, '45'))
ui.side_4_square_6.clicked.connect(partial(bp_ss, '46'))
ui.side_4_square_7.clicked.connect(partial(bp_ss, '47'))
ui.side_4_square_8.clicked.connect(partial(bp_ss, '48'))

ui.side_5_square_0.clicked.connect(partial(bp_ss, '50'))
ui.side_5_square_1.clicked.connect(partial(bp_ss, '51'))
ui.side_5_square_2.clicked.connect(partial(bp_ss, '52'))
ui.side_5_square_3.clicked.connect(partial(bp_ss, '53'))
ui.side_5_square_4.clicked.connect(partial(bp_ss, '54'))
ui.side_5_square_5.clicked.connect(partial(bp_ss, '55'))
ui.side_5_square_6.clicked.connect(partial(bp_ss, '56'))
ui.side_5_square_7.clicked.connect(partial(bp_ss, '57'))
ui.side_5_square_8.clicked.connect(partial(bp_ss, '58'))

'''
#		FOR ROTATING CUBE
'''


# def as calculator buttons

def brackets(bracket):
	if Entering_cube or Entering_cube_for_loading or Typing_rotate:
		if bracket == '(':
			text = ui.turn_line.text()
			ui.turn_line.setText(text + '(')
		elif bracket == ')':
			text = ui.turn_line.text()
			text = text.rstrip()
			ui.turn_line.setText(text + ')')


def rotation(turn):
	global cube_list
	global last_turn
	global text_for_sms_as_cmd
	
	if Entering_cube or Entering_cube_for_loading or Typing_rotate:
		if turn in ['U', 'F', 'R', 'D', 'B', 'L', 'E', 'S', 'M']:
			text = ui.turn_line.text()
			ui.turn_line.setText(text + turn + ' ')
		
		elif turn in ['2', "'"]:
			text = ui.turn_line.text()
			text = text.rstrip()
			ui.turn_line.setText(text + turn + ' ')
	
	elif Rotating_immediately:
		if turn in ['U', 'F', 'R', 'D', 'B', 'L', 'E', 'S', 'M']:
			text = ui.turn_line.text()
			ui.turn_line.setText(text + turn + ' ')
			
			SCube.rotate_cube(SCube.check_string(turn + ' '), cube_list)
			cube_list_to_buttons_cube(cube_list)
			last_turn = turn
		
		elif turn == '2':
			text = ui.turn_line.text()
			text = text.rstrip()
			ui.turn_line.setText(text + turn + ' ')
			
			SCube.rotate_cube(SCube.check_string(last_turn + ' '), cube_list)
			cube_list_to_buttons_cube(cube_list)
		
		elif turn == "'":
			text = ui.turn_line.text()
			text = text.rstrip()
			ui.turn_line.setText(text + turn + ' ')
			
			SCube.rotate_cube(SCube.check_string(last_turn + "' "), cube_list)
			cube_list_to_buttons_cube(cube_list)
		
		else:
			text_for_sms_as_cmd = 'Error in rotation. In Rotating_immediately mode'
			print(text_for_sms_as_cmd, end = '')
			sms_as_cmd_display()


def bp_backspace():
	global cube_list
	global text_for_sms_as_cmd
	
	if Entering_cube or Entering_cube_for_loading or Typing_rotate:
		text = ui.turn_line.text()
		text = text.rstrip()
		ui.turn_line.setText(text)
		ui.turn_line.backspace()
	
	elif Rotating_immediately:
		text = ui.turn_line.text()
		text = text.rstrip()
		ui.turn_line.setText(text)
		ui.turn_line.backspace()
		
		if text == '':
			pass
		else:
			sign = text[-1]
			if sign == "'":
				turn = text[-2]
				SCube.rotate_cube(SCube.check_string(turn + ' '), cube_list)
				cube_list_to_buttons_cube(cube_list)
			
			elif sign == '2':
				turn = text[-2]
				SCube.rotate_cube(SCube.check_string(turn + '2 '), cube_list)
				cube_list_to_buttons_cube(cube_list)
				ui.turn_line.backspace()
			
			elif sign in ['U', 'F', 'R', 'D', 'B', 'L', 'E', 'S', 'M']:
				SCube.rotate_cube(SCube.check_string(sign + "' "), cube_list)
				cube_list_to_buttons_cube(cube_list)
			
			else:
				text_for_sms_as_cmd = 'Error in bp_backspace. In Rotating_immediately mode'
				print(text_for_sms_as_cmd, end = '')
				sms_as_cmd_display()


def bp_clear_all():
	if Entering_cube or Entering_cube_for_loading or Typing_rotate:
		ui.turn_line.clear()
	elif Rotating_immediately:  # Возможно сделать так чтобы он всё таки выполнял это, то есть все шаги возвращал
		save(cube_list, with_txt = 'Only', turn_string = ui.turn_line.text())
		while ui.turn_line.text() != '':
			bp_backspace()


def use_clipboard(function):
	if function == 'Cut':
		ui.turn_line.selectAll()
		ui.turn_line.cut()
		# Добавить, чтобы в режиме немедленного вращения тоже вращало сразу
	elif function == 'Copy':
		ui.turn_line.selectAll()
		ui.turn_line.copy()
	elif function == 'Paste':
		ui.turn_line.end(False)
		ui.turn_line.paste()
		# Добавить, чтобы в режиме немедленного вращения тоже вращало сразу


def bp_enter():
	"""
	pass
	"""
	"""
	# Rotation painting cube # Оставить поддержку рисовалки
	global cube_list
	turn_string = ui.turn_line.text()
	SCube.rotate_cube(SCube.check_string(turn_string), cube_list)
	принт(SCube.list_to_string(cube_list))
	#SCube.painting_cube(cube_list)
	"""
	
	global cube_list
	global Saving_in_Temporary_cube
	
	if Typing_rotate or Rotating_immediately:
		turn_string = ui.turn_line.text()
		SCube.rotate_cube(SCube.check_string(turn_string), cube_list)
		cube_list_to_buttons_cube(cube_list)
		Saving_in_Temporary_cube = True
		save(cube_list, 'Yes', turn_string)


def convert_cube_buttons_to_3d_cube():
	SCube.cube_3d_html_to_html(SCube.list_to_cube_3d_html(cube_list))
	print('3d was created')


# Using as calculator buttons
ui.x2.clicked.connect(partial(rotation, '2'))
ui.apostrophe.clicked.connect(partial(rotation, "'"))
ui.bra.clicked.connect(partial(brackets, '('))
ui.ket.clicked.connect(partial(brackets, ')'))

ui.u.clicked.connect(partial(rotation, 'U'))
ui.f.clicked.connect(partial(rotation, 'F'))
ui.r.clicked.connect(partial(rotation, 'R'))
ui.d.clicked.connect(partial(rotation, 'D'))
ui.b.clicked.connect(partial(rotation, 'B'))
ui.l.clicked.connect(partial(rotation, 'L'))
ui.e.clicked.connect(partial(rotation, 'E'))
ui.s.clicked.connect(partial(rotation, 'S'))
ui.m.clicked.connect(partial(rotation, 'M'))

ui.backspace.clicked.connect(bp_backspace)  # ( partial(rotation, 'Backspace') )
ui.enter.clicked.connect(bp_enter)
ui.clear_all.clicked.connect(bp_clear_all)  # ( partial(rotation, 'Clear_all') ) # Возможно #?

ui.cut.clicked.connect(partial(use_clipboard, 'Cut'))
ui.copy.clicked.connect(partial(use_clipboard, 'Copy'))
ui.paste.clicked.connect(partial(use_clipboard, 'Paste'))

# Using 3d
ui.cube_buttons_to_3d_cube.clicked.connect(convert_cube_buttons_to_3d_cube)

# Choose Save or Load Cube
# """


def choose_save_or_load():
	# Save
	global text_for_sms_as_cmd
	
	global saving_to_last
	global saving_to_mine
	
	if ui.save_to_last.isChecked():
		text_for_sms_as_cmd = 'Using Saving to last\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_display()
		
		ui.save_to_last.setStyleSheet(save_or_load_radio_buttons_style_sheet_on)
	
	elif not ui.save_to_last.isChecked():
		ui.save_to_last.setStyleSheet(save_or_load_radio_buttons_style_sheet_off)
	
	saving_to_last = ui.save_to_last.isChecked()
	
	if ui.save_to_mine.isChecked():
		text_for_sms_as_cmd = 'Using Saving to mine\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_display()
		
		ui.save_to_mine.setStyleSheet(save_or_load_radio_buttons_style_sheet_on)
	
	elif not ui.save_to_mine.isChecked():
		ui.save_to_mine.setStyleSheet(save_or_load_radio_buttons_style_sheet_off)
	
	saving_to_mine = ui.save_to_mine.isChecked()
	
	# Load
	global loading_from_last
	global loading_from_start
	global loading_from_mine
	
	if ui.load_from_last.isChecked():
		text_for_sms_as_cmd = 'Using Loading from last\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_display()
		
		ui.load_from_last.setStyleSheet(save_or_load_radio_buttons_style_sheet_on)
	
	elif not ui.load_from_last.isChecked():
		ui.load_from_last.setStyleSheet(save_or_load_radio_buttons_style_sheet_off)
	
	loading_from_last = ui.load_from_last.isChecked()
	
	if ui.load_from_start.isChecked():
		text_for_sms_as_cmd = 'Using Loading from start\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_display()
		
		ui.load_from_start.setStyleSheet(save_or_load_radio_buttons_style_sheet_on)
	
	elif not ui.load_from_start.isChecked():
		ui.load_from_start.setStyleSheet(save_or_load_radio_buttons_style_sheet_off)
	
	loading_from_start = ui.load_from_start.isChecked()
	
	if ui.load_from_mine.isChecked():
		text_for_sms_as_cmd = 'Using Loading from mine\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_display()
		
		ui.load_from_mine.setStyleSheet(save_or_load_radio_buttons_style_sheet_on)
	
	elif not ui.load_from_mine.isChecked():
		ui.load_from_mine.setStyleSheet(save_or_load_radio_buttons_style_sheet_off)
	
	loading_from_mine = ui.load_from_mine.isChecked()


ui.save_to_last.clicked.connect(choose_save_or_load)  # Choose_save
ui.save_to_mine.clicked.connect(choose_save_or_load)  # Choose_save

ui.load_from_last.clicked.connect(choose_save_or_load)  # Choose_load
ui.load_from_start.clicked.connect(choose_save_or_load)  # Choose_load
ui.load_from_mine.clicked.connect(choose_save_or_load)  # Choose_load


# """


def cube_list_to_buttons_cube(cube_buttons):
	global Entering_cube_for_loading
	
	cube_buttons = SCube.coloring(cube_buttons, 1)
	
	Entering_cube_for_loading = True
	
	for side in range(len(cube_buttons)):
		for square in range(len(cube_buttons[side])):
			color = cube_buttons[side][square]
			bp_coloring(color)
			ss = str(side) + str(square)
			bp_ss(ss)
	
	Entering_cube_for_loading = False


# Save and Load Cube #Посмотреть как сохранять в txt либо при нажатии на энтер либо выбор возле сейв
# """

def save(cube_list_for_saving = '[]', with_txt = 'No', turn_string = 'Empty'):  # Видимо проблема именно в этом сейв тк он берёт не тот куб_лист
	# global cube_list
	global text_for_sms_as_cmd
	global Saving_in_Temporary_cube
	
	where_saving = ''
	
	if cube_list_for_saving == '[]':
		text_for_sms_as_cmd = 'cube_list_for_saving is empty. cube_list will saving\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_display()
		cube_list_for_saving = list(cube_list)
	
	if saving_to_last:
		where_saving = 'Save_to_last'
	elif saving_to_mine:
		where_saving = 'Save_to_mine'
	elif Saving_in_Temporary_cube:
		text_for_sms_as_cmd = 'Saving in Temporary_cube.\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_display()
		where_saving = 'Temporary_cube'
		Saving_in_Temporary_cube = False
	elif with_txt == 'Only':
		SCube.saving_cube(cube_list_for_saving, where_saving, with_txt = 'Only', turn_string = turn_string)
	else:
		text_for_sms_as_cmd = 'Chose where saving.\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_display()
	
	if where_saving != '':
		text_for_sms_as_cmd = 'Saving...\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_display()
		
		SCube.saving_cube(cube_list_for_saving, where_saving, with_txt, turn_string)
		
		text_for_sms_as_cmd = 'Saving complite\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_display()
	
	ui.save_to_last.setChecked(False)
	ui.save_to_last.setStyleSheet(save_or_load_radio_buttons_style_sheet_off)
	
	ui.save_to_mine.setChecked(False)
	ui.save_to_mine.setStyleSheet(save_or_load_radio_buttons_style_sheet_off)
	
	ui.nothing.setChecked(True)


def load():  # Сделать что-то с загрузкой до сохранения #????
	global cube_list
	global text_for_sms_as_cmd
	
	where_from_loading = ''
	
	if loading_from_last:
		where_from_loading = 'loading_from_last'
	elif loading_from_start:
		where_from_loading = 'loading_from_start'
	elif loading_from_mine:
		where_from_loading = 'loading_from_mine'
	else:
		text_for_sms_as_cmd = 'Chose what loading\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_display()
	
	if where_from_loading != '':
		text_for_sms_as_cmd = 'Loading...\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_display()
		
		cube_list = SCube.loading_cube(where_from_loading)
		cube_list_to_buttons_cube(cube_list)
		
		text_for_sms_as_cmd = 'Loading complete\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_display()
	
	ui.load_from_last.setChecked(False)
	ui.load_from_last.setStyleSheet(save_or_load_radio_buttons_style_sheet_off)
	
	ui.load_from_start.setChecked(False)
	ui.load_from_start.setStyleSheet(save_or_load_radio_buttons_style_sheet_off)
	
	ui.load_from_mine.setChecked(False)
	ui.load_from_mine.setStyleSheet(save_or_load_radio_buttons_style_sheet_off)
	
	ui.nothing.setChecked(True)


ui.save.clicked.connect(save)  # (partial(save, cube_list))
ui.load.clicked.connect(load)
# """


# Use cube_to_cube_buttons and cube_buttons_to_cube
def use_cube_to_cube_buttons():
	if ui.use_cube_1_on.isChecked():
		cube_list_to_buttons_cube(SCube.string_to_list(ui.use_cube_1.toPlainText()))


def use_cube_buttons_to_cube():
	if ui.use_cube_2_on.isChecked():
		ui.use_cube_2.setText(SCube.list_to_string(cube_list))


ui.cube_to_cube_buttons.clicked.connect(use_cube_to_cube_buttons)
ui.cube_buttons_to_cube.clicked.connect(use_cube_buttons_to_cube)


# Use compare_cube
def use_compare_cube():
	if ui.compare_cube_on.isChecked():
		SCube.compare_cube(SCube.string_to_list(ui.use_cube_1.toPlainText()), SCube.string_to_list(ui.use_cube_2.toPlainText()))


ui.launch.clicked.connect(use_compare_cube)


# Run main loop
sys.exit(app.exec_())

# Временные строки

