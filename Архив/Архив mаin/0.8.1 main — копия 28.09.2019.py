'''Оставить описание функций проги: #?
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
'''

'''Тех_док: #?
Python 3.7.2
PySide2 VERSION 5.13.1

Дата последней редакции кода: 27.09.2019. Версия 0.8.1 main						ПРОВЕРИТЬ НА БАГИ И ДОДЕЛАТЬ #?
Дата последней редакции оформления: 26.09.2019. Версия 0.1.7 All_Cube
'''


'''Мне делать:
Возможно:
	Добавить светлую тему #?
	Cделать то же самое на телефоне #?

Добавить:
	Проверять все принты при запуске: Отправляють print в sms_as_cmd_display (sms_as_cmd_display = print) #?

	#Откуда: Возможно вставить это в bp_Enter
	"""							 #??
	из SCube.check_string 
	принт('Строка не подходит для вращения кубика')
	принт(wherefrom_string, end = '\n\n') х2


	из SCube.rotate_cube
	принт('turn: ' + turn + ' is not turn')


	из SCube.loading_cube
	принт('Saving directory does not exist. Check and try again.')
	"""


	Проверять если все 3 сейва, если нет, то записать пустые чтобы можно было запустить или написать, что нет такого сейва #????
'''

#! python3

import sys, os, shelve
from functools import partial

from PySide2 import QtCore, QtGui, QtWidgets

from All_Cube import Ui_Window

#Найти как передать переменную в Simulation_of_cube_comp word = 'Open' #?
import Simulation_of_cube_comp as SCube

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
text_for_sms_as_cmd = 'For convenience, expand the window to full screen.\n\n Also save last and mine cube before loading it'
sms_as_cmd_turned_on = True


# variables for Choose Save or Load Cube
Saving_to_last = False
Saving_to_mine = False

Loading_from_last = False
Loading_from_start = False
Loading_from_mine = False


# variables for Choose mode
Entering_cube = False
Entering_cube_for_loading = False
Typing_rotate = False
Rotating_immediately = False

Choose_mode_radio_buttons_style_sheet_on = (
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
	"}" )

Choose_mode_radio_buttons_style_sheet_off = (
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
	"}" )


# variables cube_list
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
#'''


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

# variables for def coloring buttons
b_coloring = ''
c_coloring = ''

# variables for def as calculator buttons
last_turn = ''

# Choose Save or Load Cube
Saving_to_last = False
Saving_to_mine = False

Loading_from_last = False
Loading_from_start = False
Loading_from_mine = False



# ALL def

#def sms_as_cmd
def sms_as_cmd_turn_on():
	global sms_as_cmd_turned_on

	if ui.Sms_as_cmd_on.isChecked():
		sms_as_cmd_turned_on = True
		ui.Sms_as_cmd_on.setText('ON')

	elif not ui.Sms_as_cmd_on.isChecked():
		sms_as_cmd_turned_on = False
		ui.Sms_as_cmd_on.setText('OFF')
		ui.Sms_as_cmd.clear()
		ui.Sms_as_cmd.setStyleSheet(
			"QTextEdit {\n"
			"  color: gray;\n"
			"  font-size: 14px;\n"
			"  border: 2px solid black;\n"
			"  selection-background-color: green;\n"
			"}")

		ui.Sms_as_cmd_button.setStyleSheet(
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
	'''print sms to as_cmd'''
	if sms_as_cmd_turned_on:
		ui.Sms_as_cmd.setStyleSheet(
			"QTextEdit {\n"
			"  color: gray;\n"
			"  font-size: 14px;\n"
			"  border: 2px solid gray;\n"
			"  selection-background-color: green;\n"
			"}")

		global text_for_sms_as_cmd

		if text_for_sms_as_cmd == 'For convenience, expand the window to full screen':
			text_from_Sms_as_cmd = ''
		else:
			text_from_Sms_as_cmd = ui.Sms_as_cmd.toPlainText()

		all_text_for_Sms_as_cmd = text_from_Sms_as_cmd + text_for_sms_as_cmd
		ui.Sms_as_cmd.setText(all_text_for_Sms_as_cmd)
		#ui.Sms_as_cmd.setText(text_for_sms_as_cmd)

		ui.Sms_as_cmd_button.setStyleSheet(
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
	ui.Sms_as_cmd.clear()
	ui.Sms_as_cmd.setStyleSheet(
		"QTextEdit {\n"
		"  color: gray;\n"
		"  font-size: 14px;\n"
		"  border: 2px solid black;\n"
		"  selection-background-color: green;\n"
		"}")

	ui.Sms_as_cmd_button.setStyleSheet(
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

ui.Sms_as_cmd_on.clicked.connect( sms_as_cmd_turn_on )
ui.Sms_as_cmd_button.clicked.connect( sms_as_cmd_undisplay )






'''
#		FOR ENTERING CUBE
'''

# Choose mode
#"""

def Choose_mode():
	global Entering_cube
	global Typing_rotate
	global Rotating_immediately
	global text_for_sms_as_cmd
	global b_coloring
	global c_coloring

	if ui.Enter_cube.isChecked():
		text_for_sms_as_cmd = 'Using Enter cube\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_display()

		ui.Enter_cube.setStyleSheet( Choose_mode_radio_buttons_style_sheet_on )

	elif not ui.Enter_cube.isChecked():
		b_coloring = ''
		c_coloring = ''

		ui.Enter_cube.setStyleSheet( Choose_mode_radio_buttons_style_sheet_off )

	Entering_cube = ui.Enter_cube.isChecked()


	if ui.Type_rotate.isChecked():
		text_for_sms_as_cmd = 'Using Typing rotate\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_display()

		ui.Type_rotate.setStyleSheet( Choose_mode_radio_buttons_style_sheet_on )

	elif not ui.Type_rotate.isChecked():
		ui.Type_rotate.setStyleSheet( Choose_mode_radio_buttons_style_sheet_off )


	Typing_rotate = ui.Type_rotate.isChecked()


	if ui.Rotate_immediately.isChecked():
		text_for_sms_as_cmd = 'Using Rotate immediately \n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_display()

		ui.Rotate_immediately.setStyleSheet( Choose_mode_radio_buttons_style_sheet_on )

	elif not ui.Rotate_immediately.isChecked():
		ui.Rotate_immediately.setStyleSheet( Choose_mode_radio_buttons_style_sheet_off )


	Rotating_immediately = ui.Rotate_immediately.isChecked()



ui.Enter_cube.clicked.connect( Choose_mode )
ui.Type_rotate.clicked.connect( Choose_mode )
ui.Rotate_immediately.clicked.connect( Choose_mode )
#"""



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


# def Side Square buttons coloring
#'''
def bp_SS(Side_Square):
	global text_for_sms_as_cmd

	if Entering_cube or Entering_cube_for_loading:
		if b_coloring == '':
			text_for_sms_as_cmd = 'Choose color\n\n'
			print(text_for_sms_as_cmd, end = '')
			sms_as_cmd_display()
		else:
			if Side_Square == '00':
				ui.Side_0_Square_0.setStyleSheet( b_coloring )
				cube_list[0][0] = c_coloring
			elif Side_Square == '01':
				ui.Side_0_Square_1.setStyleSheet( b_coloring )
				cube_list[0][1] = c_coloring
			elif Side_Square == '02':
				ui.Side_0_Square_2.setStyleSheet( b_coloring )
				cube_list[0][2] = c_coloring
			elif Side_Square == '03':
				ui.Side_0_Square_3.setStyleSheet( b_coloring )
				cube_list[0][3] = c_coloring
			elif Side_Square == '04':
				ui.Side_0_Square_4.setStyleSheet( b_coloring )
				cube_list[0][4] = c_coloring
			elif Side_Square == '05':
				ui.Side_0_Square_5.setStyleSheet( b_coloring )
				cube_list[0][5] = c_coloring
			elif Side_Square == '06':
				ui.Side_0_Square_6.setStyleSheet( b_coloring )
				cube_list[0][6] = c_coloring
			elif Side_Square == '07':
				ui.Side_0_Square_7.setStyleSheet( b_coloring )
				cube_list[0][7] = c_coloring
			elif Side_Square == '08':
				ui.Side_0_Square_8.setStyleSheet( b_coloring )
				cube_list[0][8] = c_coloring

			elif Side_Square == '10':
				ui.Side_1_Square_0.setStyleSheet( b_coloring )
				cube_list[1][0] = c_coloring
			elif Side_Square == '11':
				ui.Side_1_Square_1.setStyleSheet( b_coloring )
				cube_list[1][1] = c_coloring
			elif Side_Square == '12':
				ui.Side_1_Square_2.setStyleSheet( b_coloring )
				cube_list[1][2] = c_coloring
			elif Side_Square == '13':
				ui.Side_1_Square_3.setStyleSheet( b_coloring )
				cube_list[1][3] = c_coloring
			elif Side_Square == '14':
				ui.Side_1_Square_4.setStyleSheet( b_coloring )
				cube_list[1][4] = c_coloring
			elif Side_Square == '15':
				ui.Side_1_Square_5.setStyleSheet( b_coloring )
				cube_list[1][5] = c_coloring
			elif Side_Square == '16':
				ui.Side_1_Square_6.setStyleSheet( b_coloring )
				cube_list[1][6] = c_coloring
			elif Side_Square == '17':
				ui.Side_1_Square_7.setStyleSheet( b_coloring )
				cube_list[1][7] = c_coloring
			elif Side_Square == '18':
				ui.Side_1_Square_8.setStyleSheet( b_coloring )
				cube_list[1][8] = c_coloring

			elif Side_Square == '20':
				ui.Side_2_Square_0.setStyleSheet( b_coloring )
				cube_list[2][0] = c_coloring
			elif Side_Square == '21':
				ui.Side_2_Square_1.setStyleSheet( b_coloring )
				cube_list[2][1] = c_coloring
			elif Side_Square == '22':
				ui.Side_2_Square_2.setStyleSheet( b_coloring )
				cube_list[2][2] = c_coloring
			elif Side_Square == '23':
				ui.Side_2_Square_3.setStyleSheet( b_coloring )
				cube_list[2][3] = c_coloring
			elif Side_Square == '24':
				ui.Side_2_Square_4.setStyleSheet( b_coloring )
				cube_list[2][4] = c_coloring
			elif Side_Square == '25':
				ui.Side_2_Square_5.setStyleSheet( b_coloring )
				cube_list[2][5] = c_coloring
			elif Side_Square == '26':
				ui.Side_2_Square_6.setStyleSheet( b_coloring )
				cube_list[2][6] = c_coloring
			elif Side_Square == '27':
				ui.Side_2_Square_7.setStyleSheet( b_coloring )
				cube_list[2][7] = c_coloring
			elif Side_Square == '28':
				ui.Side_2_Square_8.setStyleSheet( b_coloring )
				cube_list[2][8] = c_coloring

			elif Side_Square == '30':
				ui.Side_3_Square_0.setStyleSheet( b_coloring )
				cube_list[3][0] = c_coloring
			elif Side_Square == '31':
				ui.Side_3_Square_1.setStyleSheet( b_coloring )
				cube_list[3][1] = c_coloring
			elif Side_Square == '32':
				ui.Side_3_Square_2.setStyleSheet( b_coloring )
				cube_list[3][2] = c_coloring
			elif Side_Square == '33':
				ui.Side_3_Square_3.setStyleSheet( b_coloring )
				cube_list[3][3] = c_coloring
			elif Side_Square == '34':
				ui.Side_3_Square_4.setStyleSheet( b_coloring )
				cube_list[3][4] = c_coloring
			elif Side_Square == '35':
				ui.Side_3_Square_5.setStyleSheet( b_coloring )
				cube_list[3][5] = c_coloring
			elif Side_Square == '36':
				ui.Side_3_Square_6.setStyleSheet( b_coloring )
				cube_list[3][6] = c_coloring
			elif Side_Square == '37':
				ui.Side_3_Square_7.setStyleSheet( b_coloring )
				cube_list[3][7] = c_coloring
			elif Side_Square == '38':
				ui.Side_3_Square_8.setStyleSheet( b_coloring )
				cube_list[3][8] = c_coloring

			elif Side_Square == '40':
				ui.Side_4_Square_0.setStyleSheet( b_coloring )
				cube_list[4][0] = c_coloring
			elif Side_Square == '41':
				ui.Side_4_Square_1.setStyleSheet( b_coloring )
				cube_list[4][1] = c_coloring
			elif Side_Square == '42':
				ui.Side_4_Square_2.setStyleSheet( b_coloring )
				cube_list[4][2] = c_coloring
			elif Side_Square == '43':
				ui.Side_4_Square_3.setStyleSheet( b_coloring )
				cube_list[4][3] = c_coloring
			elif Side_Square == '44':
				ui.Side_4_Square_4.setStyleSheet( b_coloring )
				cube_list[4][4] = c_coloring
			elif Side_Square == '45':
				ui.Side_4_Square_5.setStyleSheet( b_coloring )
				cube_list[4][5] = c_coloring
			elif Side_Square == '46':
				ui.Side_4_Square_6.setStyleSheet( b_coloring )
				cube_list[4][6] = c_coloring
			elif Side_Square == '47':
				ui.Side_4_Square_7.setStyleSheet( b_coloring )
				cube_list[4][7] = c_coloring
			elif Side_Square == '48':
				ui.Side_4_Square_8.setStyleSheet( b_coloring )
				cube_list[4][8] = c_coloring

			elif Side_Square == '50':
				ui.Side_5_Square_0.setStyleSheet( b_coloring )
				cube_list[5][0] = c_coloring
			elif Side_Square == '51':
				ui.Side_5_Square_1.setStyleSheet( b_coloring )
				cube_list[5][1] = c_coloring
			elif Side_Square == '52':
				ui.Side_5_Square_2.setStyleSheet( b_coloring )
				cube_list[5][2] = c_coloring
			elif Side_Square == '53':
				ui.Side_5_Square_3.setStyleSheet( b_coloring )
				cube_list[5][3] = c_coloring
			elif Side_Square == '54':
				ui.Side_5_Square_4.setStyleSheet( b_coloring )
				cube_list[5][4] = c_coloring
			elif Side_Square == '55':
				ui.Side_5_Square_5.setStyleSheet( b_coloring )
				cube_list[5][5] = c_coloring
			elif Side_Square == '56':
				ui.Side_5_Square_6.setStyleSheet( b_coloring )
				cube_list[5][6] = c_coloring
			elif Side_Square == '57':
				ui.Side_5_Square_7.setStyleSheet( b_coloring )
				cube_list[5][7] = c_coloring
			elif Side_Square == '58':
				ui.Side_5_Square_8.setStyleSheet( b_coloring )
				cube_list[5][8] = c_coloring
#'''



# Using coloring buttons
ui.Yellow_Button.clicked.connect( partial(bp_coloring, 'Yellow') )
ui.Orange_Button.clicked.connect( partial(bp_coloring, 'Orange') )
ui.Blue_Button.clicked.connect( partial(bp_coloring, 'Blue') )
ui.Red_Button.clicked.connect( partial(bp_coloring, 'Red') )
ui.White_Button.clicked.connect( partial(bp_coloring, 'White') )
ui.Green_Button.clicked.connect( partial(bp_coloring, 'Green') )

# Using Side Square buttons coloring
ui.Side_0_Square_0.clicked.connect( partial(bp_SS,'00') )
ui.Side_0_Square_1.clicked.connect( partial(bp_SS,'01') )
ui.Side_0_Square_2.clicked.connect( partial(bp_SS,'02') )
ui.Side_0_Square_3.clicked.connect( partial(bp_SS,'03') )
ui.Side_0_Square_4.clicked.connect( partial(bp_SS,'04') )
ui.Side_0_Square_5.clicked.connect( partial(bp_SS,'05') )
ui.Side_0_Square_6.clicked.connect( partial(bp_SS,'06') )
ui.Side_0_Square_7.clicked.connect( partial(bp_SS,'07') )
ui.Side_0_Square_8.clicked.connect( partial(bp_SS,'08') )

ui.Side_1_Square_0.clicked.connect( partial(bp_SS,'10') )
ui.Side_1_Square_1.clicked.connect( partial(bp_SS,'11') )
ui.Side_1_Square_2.clicked.connect( partial(bp_SS,'12') )
ui.Side_1_Square_3.clicked.connect( partial(bp_SS,'13') )
ui.Side_1_Square_4.clicked.connect( partial(bp_SS,'14') )
ui.Side_1_Square_5.clicked.connect( partial(bp_SS,'15') )
ui.Side_1_Square_6.clicked.connect( partial(bp_SS,'16') )
ui.Side_1_Square_7.clicked.connect( partial(bp_SS,'17') )
ui.Side_1_Square_8.clicked.connect( partial(bp_SS,'18') )

ui.Side_2_Square_0.clicked.connect( partial(bp_SS,'20') )
ui.Side_2_Square_1.clicked.connect( partial(bp_SS,'21') )
ui.Side_2_Square_2.clicked.connect( partial(bp_SS,'22') )
ui.Side_2_Square_3.clicked.connect( partial(bp_SS,'23') )
ui.Side_2_Square_4.clicked.connect( partial(bp_SS,'24') )
ui.Side_2_Square_5.clicked.connect( partial(bp_SS,'25') )
ui.Side_2_Square_6.clicked.connect( partial(bp_SS,'26') )
ui.Side_2_Square_7.clicked.connect( partial(bp_SS,'27') )
ui.Side_2_Square_8.clicked.connect( partial(bp_SS,'28') )

ui.Side_3_Square_0.clicked.connect( partial(bp_SS,'30') )
ui.Side_3_Square_1.clicked.connect( partial(bp_SS,'31') )
ui.Side_3_Square_2.clicked.connect( partial(bp_SS,'32') )
ui.Side_3_Square_3.clicked.connect( partial(bp_SS,'33') )
ui.Side_3_Square_4.clicked.connect( partial(bp_SS,'34') )
ui.Side_3_Square_5.clicked.connect( partial(bp_SS,'35') )
ui.Side_3_Square_6.clicked.connect( partial(bp_SS,'36') )
ui.Side_3_Square_7.clicked.connect( partial(bp_SS,'37') )
ui.Side_3_Square_8.clicked.connect( partial(bp_SS,'38') )

ui.Side_4_Square_0.clicked.connect( partial(bp_SS,'40') )
ui.Side_4_Square_1.clicked.connect( partial(bp_SS,'41') )
ui.Side_4_Square_2.clicked.connect( partial(bp_SS,'42') )
ui.Side_4_Square_3.clicked.connect( partial(bp_SS,'43') )
ui.Side_4_Square_4.clicked.connect( partial(bp_SS,'44') )
ui.Side_4_Square_5.clicked.connect( partial(bp_SS,'45') )
ui.Side_4_Square_6.clicked.connect( partial(bp_SS,'46') )
ui.Side_4_Square_7.clicked.connect( partial(bp_SS,'47') )
ui.Side_4_Square_8.clicked.connect( partial(bp_SS,'48') )

ui.Side_5_Square_0.clicked.connect( partial(bp_SS,'50') )
ui.Side_5_Square_1.clicked.connect( partial(bp_SS,'51') )
ui.Side_5_Square_2.clicked.connect( partial(bp_SS,'52') )
ui.Side_5_Square_3.clicked.connect( partial(bp_SS,'53') )
ui.Side_5_Square_4.clicked.connect( partial(bp_SS,'54') )
ui.Side_5_Square_5.clicked.connect( partial(bp_SS,'55') )
ui.Side_5_Square_6.clicked.connect( partial(bp_SS,'56') )
ui.Side_5_Square_7.clicked.connect( partial(bp_SS,'57') )
ui.Side_5_Square_8.clicked.connect( partial(bp_SS,'58') )



'''
#		FOR ROTATING CUBE
'''


# def as calculator buttons

def brakets(braket):
	if Entering_cube or Entering_cube_for_loading or Typing_rotate:
		if braket == '(':
			text = ui.turn_line.text()
			ui.turn_line.setText(text + '(')
		elif braket == ')':
			text = ui.turn_line.text()
			text = text.rstrip()
			ui.turn_line.setText(text + ')')


def rotation(turn):
	global cube_list
	global last_turn

	if Entering_cube or Entering_cube_for_loading or Typing_rotate:
		if turn in ['U', 'F', 'R', 'D', 'B', 'L' ,'E' ,'S' ,'M']:
			text = ui.turn_line.text()
			ui.turn_line.setText(text + turn + ' ')

		elif turn in ['2', "'"]:
			text = ui.turn_line.text()
			text = text.rstrip()
			ui.turn_line.setText(text + turn + ' ')


	elif Rotating_immediately:
		if turn in ['U', 'F', 'R', 'D', 'B', 'L' ,'E' ,'S' ,'M']:
			text = ui.turn_line.text()
			ui.turn_line.setText(text + turn + ' ')

			SCube.rotate_cube(SCube.check_string(turn + ' '), cube_list)
			cube_list_to_buttons_cube(cube_list)
			last_turn = turn
			sign = ''

		elif turn == '2':
			text = ui.turn_line.text()
			text = text.rstrip()
			ui.turn_line.setText(text + turn + ' ')

			SCube.rotate_cube(SCube.check_string(last_turn + ' '), cube_list)
			cube_list_to_buttons_cube(cube_list)
			sign = '2'

		elif turn == "'":
			text = ui.turn_line.text()
			text = text.rstrip()
			ui.turn_line.setText(text + turn + ' ')

			SCube.rotate_cube(SCube.check_string(last_turn + "' "), cube_list)
			cube_list_to_buttons_cube(cube_list)
			sign = "'"

		else:
			text_for_sms_as_cmd = 'Error in rotation. In Rotating_immediately mode'
			print(text_for_sms_as_cmd, end = '')
			sms_as_cmd_display()


def bp_Backspace():
	global cube_list

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

			elif sign in ['U', 'F', 'R', 'D', 'B', 'L' ,'E' ,'S' ,'M']:
				SCube.rotate_cube(SCube.check_string(sign + "' "), cube_list)
				cube_list_to_buttons_cube(cube_list)

			else:
				text_for_sms_as_cmd = 'Error in bp_Backspace. In Rotating_immediately mode'
				print(text_for_sms_as_cmd, end = '')
				sms_as_cmd_display()


def bp_Clear_all():
	if Entering_cube or Entering_cube_for_loading or Typing_rotate:
		ui.turn_line.clear()
	elif Rotating_immediately: #Возможно сделать так чтобы он всё таки выполнял это, то есть все шаги возвращал
		save(cube_list, with_txt = 'Only', turn_string = ui.turn_line.text())
		while ui.turn_line.text() != '':
			bp_Backspace()

def use_clipboard(function):
	if function == 'Cut':
		ui.turn_line.selectAll()
		ui.turn_line.cut()
	elif function == 'Copy':
		ui.turn_line.selectAll()
		ui.turn_line.copy()
	elif function == 'Paste':
		ui.turn_line.end(False)
		ui.turn_line.paste()


Saving_in_Temporary_cube = False

def bp_Enter():
	'''
	pass
	'''
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


# Using as calculator buttons
ui.x2.clicked.connect( partial(rotation, '2') )
ui.Apostrophe.clicked.connect( partial(rotation, "'") )
ui.bra.clicked.connect( partial(brakets, '(') )
ui.ket.clicked.connect( partial(brakets, ')') )

ui.U.clicked.connect( partial(rotation, 'U') )
ui.F.clicked.connect( partial(rotation, 'F') )
ui.R.clicked.connect( partial(rotation, 'R') )
ui.D.clicked.connect( partial(rotation, 'D') )
ui.B.clicked.connect( partial(rotation, 'B') )
ui.L.clicked.connect( partial(rotation, 'L') )
ui.E.clicked.connect( partial(rotation, 'E') )
ui.S.clicked.connect( partial(rotation, 'S') )
ui.M.clicked.connect( partial(rotation, 'M') )

ui.Backspace.clicked.connect( bp_Backspace ) # ( partial(rotation, 'Backspace') )
ui.Enter.clicked.connect( bp_Enter )
ui.Clear_all.clicked.connect( bp_Clear_all )# ( partial(rotation, 'Clear_all') ) # Возможно #?

ui.Cut.clicked.connect( partial(use_clipboard, 'Cut') )
ui.Copy.clicked.connect( partial(use_clipboard, 'Copy') )
ui.Paste.clicked.connect( partial(use_clipboard, 'Paste') )



# Choose Save or Load Cube
#"""

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
	"    color: gray;\n"
	"}" )

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
	"    color: gray;\n"
	"}" )


def Choose_save_or_load():

#Save
	global text_for_sms_as_cmd

	global Saving_to_last
	global Saving_to_mine

	if ui.Save_to_last.isChecked():
		text_for_sms_as_cmd = 'Using Saving to last\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_display()

		ui.Save_to_last.setStyleSheet(	save_or_load_radio_buttons_style_sheet_on )

	elif not ui.Save_to_last.isChecked():
		ui.Save_to_last.setStyleSheet(	save_or_load_radio_buttons_style_sheet_off )

	Saving_to_last = ui.Save_to_last.isChecked()


	if ui.Save_to_mine.isChecked():
		text_for_sms_as_cmd = 'Using Saving to mine\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_display()

		ui.Save_to_mine.setStyleSheet(	save_or_load_radio_buttons_style_sheet_on )

	elif not ui.Save_to_mine.isChecked():
		ui.Save_to_mine.setStyleSheet(	save_or_load_radio_buttons_style_sheet_off )

	Saving_to_mine = ui.Save_to_mine.isChecked()


#Load
	global Loading_from_last
	global Loading_from_start
	global Loading_from_mine

	if ui.Load_from_last.isChecked():
		text_for_sms_as_cmd = 'Using Loading from last\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_display()

		ui.Load_from_last.setStyleSheet(	save_or_load_radio_buttons_style_sheet_on )

	elif not ui.Load_from_last.isChecked():
		ui.Load_from_last.setStyleSheet(	save_or_load_radio_buttons_style_sheet_off )

	Loading_from_last = ui.Load_from_last.isChecked()


	if ui.Load_from_start.isChecked():
		text_for_sms_as_cmd = 'Using Loading from start\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_display()

		ui.Load_from_start.setStyleSheet(	save_or_load_radio_buttons_style_sheet_on )

	elif not ui.Load_from_start.isChecked():
		ui.Load_from_start.setStyleSheet(	save_or_load_radio_buttons_style_sheet_off )

	Loading_from_start = ui.Load_from_start.isChecked()


	if ui.Load_from_mine.isChecked():
		text_for_sms_as_cmd = 'Using Loading from mine\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_display()

		ui.Load_from_mine.setStyleSheet(	save_or_load_radio_buttons_style_sheet_on )

	elif not ui.Load_from_mine.isChecked():
		ui.Load_from_mine.setStyleSheet(	save_or_load_radio_buttons_style_sheet_off )

	Loading_from_mine = ui.Load_from_mine.isChecked()

ui.Save_to_last.clicked.connect( Choose_save_or_load )#Choose_save
ui.Save_to_mine.clicked.connect( Choose_save_or_load )#Choose_save

ui.Load_from_last.clicked.connect( Choose_save_or_load )#Choose_load
ui.Load_from_start.clicked.connect( Choose_save_or_load )#Choose_load
ui.Load_from_mine.clicked.connect( Choose_save_or_load )#Choose_load
#"""



def cube_list_to_buttons_cube(cube_buttons):
	global Entering_cube_for_loading

	cube_buttons = SCube.coloring(cube_buttons, 1)

	Entering_cube_for_loading = True

	for side in range(len(cube_buttons)):
		for square in range(len(cube_buttons[side])):
			color = cube_buttons[side][square]
			bp_coloring(color)
			SS = str(side) + str(square)
			bp_SS(SS)

	Entering_cube_for_loading = False



#Save and Load Cube #Посмотреть как сохранять в txt либо при нажатии на энтер либо выбор возле сейв
#"""

def save(cube_list_for_saving = [], with_txt = 'No', turn_string = 'Empty'):
	global cube_list
	global text_for_sms_as_cmd
	global Saving_in_Temporary_cube

	where_saving = ''

	if cube_list_for_saving == []:
		text_for_sms_as_cmd = 'cube_list_for_saving is empty. cube_list will saving\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_display()
	cube_list_for_saving = cube_list

	if Saving_to_last:
		where_saving = 'Save_to_last'
	elif Saving_to_mine:
		where_saving = 'Save_to_mine'
	elif Saving_in_Temporary_cube:
		text_for_sms_as_cmd = 'Saving in Temporary_cube.\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_display()
		where_saving = 'Temporary_cube'
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

	ui.Save_to_last.setChecked(False)
	ui.Save_to_last.setStyleSheet(	save_or_load_radio_buttons_style_sheet_off )

	ui.Save_to_mine.setChecked(False)
	ui.Save_to_mine.setStyleSheet(	save_or_load_radio_buttons_style_sheet_off )

	ui.Nothing.setChecked(True)


def load(): # Сделать что-то с загрузкой до сохранения #????
	global cube_list
	global text_for_sms_as_cmd

	wherefrom_loading = ''

	if Loading_from_last:
		wherefrom_loading = 'Loading_from_last'
	elif Loading_from_start:
		wherefrom_loading = 'Loading_from_start' #'Loading_from_start'
	elif Loading_from_mine:
		wherefrom_loading = 'Loading_from_mine'
	else:
		text_for_sms_as_cmd = 'Chose what loading\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_display()

	if wherefrom_loading != '':
		text_for_sms_as_cmd = 'Loading...\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_display()

		cube_list = SCube.loading_cube(wherefrom_loading)
		cube_list_to_buttons_cube(cube_list)

		text_for_sms_as_cmd = 'Loading complite\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_display()

	ui.Load_from_last.setChecked(False)
	ui.Load_from_last.setStyleSheet( save_or_load_radio_buttons_style_sheet_off )

	ui.Load_from_start.setChecked(False)
	ui.Load_from_start.setStyleSheet( save_or_load_radio_buttons_style_sheet_off )

	ui.Load_from_mine.setChecked(False)
	ui.Load_from_mine.setStyleSheet( save_or_load_radio_buttons_style_sheet_off )

	ui.Nothing.setChecked(True)


ui.Save.clicked.connect( save )
ui.Load.clicked.connect( load )
#"""


# Run main loop
sys.exit(app.exec_())




# Временные строки

