'''
Сделать переключение между 3 режимами: #?
1 Ввод кубика кнопками в All cube
1.1 Ввод и сохранение
1.2 Загрузка сохранения
1.3 Вывод кубика из сохранения
2 Добавить чтобы кубик сразу вращался при нажатии Enter
XOR
3 чтобы кубик сразу вращался при нажатии кнопок, а не при нажатии Enter
Добавить: #?
Отправляють print в Sms_as_cmd (Проверять все принты при запуске)

открыть мой кубик и пустой кубик, возможно через клиар
или вызывать менюшку при нажатии на лоадинг для выбора загрузки: мой, чистый, последний сохранённый
возможно и в сейв в: мой, последний сохранённый

Cделать так чтобы Sms_as_cmd можно было выключать

Проверять если все 3 сейва, если нет, то записать пустые чтобы можно было запустить или написать, что нет такого сейва
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


# Sms as cmd setup
text_for_sms_as_cmd = ''

def sms_as_cmd_print():
	ui.Sms_as_cmd.setStyleSheet("QTextEdit {\n"
								"  color: gray;\n"
								"  font-size: 14px;\n"
								"  border: 2px solid gray;\n"
								"  selection-background-color: green;\n"
								"}")

	global text_for_sms_as_cmd

	if text_for_sms_as_cmd == 'For convenience, expand the window to full screen':
		text_from_Sms_as_cmd = ''
	else:
		text_from_Sms_as_cmd = ui.Sms_as_cmd.toPlainText() #Проверить что нет так пишет не поддерживает .text #?????

	all_text_for_Sms_as_cmd = text_from_Sms_as_cmd + text_for_sms_as_cmd
	ui.Sms_as_cmd.setText(all_text_for_Sms_as_cmd)
	#ui.Sms_as_cmd.setText(text_for_sms_as_cmd)

	ui.Sms_as_cmd_button.setStyleSheet(	"QPushButton{\n"
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

def sms_as_cmd_unprint():
	ui.Sms_as_cmd.clear()
	ui.Sms_as_cmd.setStyleSheet("QTextEdit {\n"
								"  color: gray;\n"
								"  font-size: 14px;\n"
								"  border: 2px solid black;\n"
								"  selection-background-color: green;\n"
								"}")

	ui.Sms_as_cmd_button.setStyleSheet(	"QPushButton{\n"
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


text_for_sms_as_cmd = 'For convenience, expand the window to full screen\n\n'
sms_as_cmd_print()

ui.Sms_as_cmd_button.clicked.connect( sms_as_cmd_unprint )



# cube_list
#'''
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



'''
		FOR ENTERING CUBE
'''

Entering_cube = False
Entering_cube_loading = False
Typing_rotate = False
Rotating_immediately = False

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
		sms_as_cmd_print()
		
		ui.Enter_cube.setStyleSheet(	"QRadioButton{\n"
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

	elif not ui.Enter_cube.isChecked():
		#print("Enter cube No using\n")
		b_coloring = ''
		c_coloring = ''

		ui.Enter_cube.setStyleSheet(	"QRadioButton{\n"
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

	Entering_cube = ui.Enter_cube.isChecked()


	if ui.Type_rotate.isChecked():
		text_for_sms_as_cmd = 'Using Typing rotate\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_print()

		ui.Type_rotate.setStyleSheet(	"QRadioButton{\n"
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

	elif not ui.Type_rotate.isChecked():
		#print("Typing rotate No using\n")
		ui.Type_rotate.setStyleSheet(	"QRadioButton{\n"
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


	Typing_rotate = ui.Type_rotate.isChecked()


	if ui.Rotate_immediately.isChecked():
		text_for_sms_as_cmd = 'Using Rotate immediately \n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_print()

		ui.Rotate_immediately.setStyleSheet(	"QRadioButton{\n"
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

	elif not ui.Rotate_immediately.isChecked():
		#print("Rotate immediately No using\n\n")
		ui.Rotate_immediately.setStyleSheet("QRadioButton{\n"
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


	Rotating_immediately = ui.Rotate_immediately.isChecked()



ui.Enter_cube.clicked.connect( Choose_mode )
ui.Type_rotate.clicked.connect( Choose_mode )
ui.Rotate_immediately.clicked.connect( Choose_mode )
#"""



# def coloring buttons
b_coloring = ''
c_coloring = ''

def bp_coloring(b_color):
	if Entering_cube or Entering_cube_loading:
		global b_coloring
		global c_coloring

		if b_color == 'Yellow':
			c_coloring = 'y'
			b_coloring = (	"QPushButton{\n"
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

		if b_color == 'Orange':
			c_coloring = 'o'
			b_coloring = (	"QPushButton{\n"
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

		if b_color == 'Blue':
			c_coloring = 'b'
			b_coloring = (	"QPushButton{\n"
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

		if b_color == 'Red':
			c_coloring = 'r'
			b_coloring = (	"QPushButton{\n"
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

		if b_color == 'White':
			c_coloring = 'w'
			b_coloring = (	"QPushButton{\n"
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

		if b_color == 'Green':
			c_coloring = 'g'
			b_coloring = (	"QPushButton{\n"
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
	
	if Entering_cube or Entering_cube_loading:
		if b_coloring == '':
			text_for_sms_as_cmd = 'Choose color\n\n'
			print(text_for_sms_as_cmd, end = '')
			sms_as_cmd_print()
		else:
			if Side_Square == '00':
				ui.Side_0_Square_0.setStyleSheet( b_coloring )
				cube_list[0][0] = c_coloring
			if Side_Square == '01':
				ui.Side_0_Square_1.setStyleSheet( b_coloring )
				cube_list[0][1] = c_coloring
			if Side_Square == '02':
				ui.Side_0_Square_2.setStyleSheet( b_coloring )
				cube_list[0][2] = c_coloring
			if Side_Square == '03':
				ui.Side_0_Square_3.setStyleSheet( b_coloring )
				cube_list[0][3] = c_coloring
			if Side_Square == '04':
				ui.Side_0_Square_4.setStyleSheet( b_coloring )
				cube_list[0][4] = c_coloring
			if Side_Square == '05':
				ui.Side_0_Square_5.setStyleSheet( b_coloring )
				cube_list[0][5] = c_coloring
			if Side_Square == '06':
				ui.Side_0_Square_6.setStyleSheet( b_coloring )
				cube_list[0][6] = c_coloring
			if Side_Square == '07':
				ui.Side_0_Square_7.setStyleSheet( b_coloring )
				cube_list[0][7] = c_coloring
			if Side_Square == '08':
				ui.Side_0_Square_8.setStyleSheet( b_coloring )
				cube_list[0][8] = c_coloring
	
			if Side_Square == '10':
				ui.Side_1_Square_0.setStyleSheet( b_coloring )
				cube_list[1][0] = c_coloring
			if Side_Square == '11':
				ui.Side_1_Square_1.setStyleSheet( b_coloring )
				cube_list[1][1] = c_coloring
			if Side_Square == '12':
				ui.Side_1_Square_2.setStyleSheet( b_coloring )
				cube_list[1][2] = c_coloring
			if Side_Square == '13':
				ui.Side_1_Square_3.setStyleSheet( b_coloring )
				cube_list[1][3] = c_coloring
			if Side_Square == '14':
				ui.Side_1_Square_4.setStyleSheet( b_coloring )
				cube_list[1][4] = c_coloring
			if Side_Square == '15':
				ui.Side_1_Square_5.setStyleSheet( b_coloring )
				cube_list[1][5] = c_coloring
			if Side_Square == '16':
				ui.Side_1_Square_6.setStyleSheet( b_coloring )
				cube_list[1][6] = c_coloring
			if Side_Square == '17':
				ui.Side_1_Square_7.setStyleSheet( b_coloring )
				cube_list[1][7] = c_coloring
			if Side_Square == '18':
				ui.Side_1_Square_8.setStyleSheet( b_coloring )
				cube_list[1][8] = c_coloring

			if Side_Square == '20':
				ui.Side_2_Square_0.setStyleSheet( b_coloring )
				cube_list[2][0] = c_coloring
			if Side_Square == '21':
				ui.Side_2_Square_1.setStyleSheet( b_coloring )
				cube_list[2][1] = c_coloring
			if Side_Square == '22':
				ui.Side_2_Square_2.setStyleSheet( b_coloring )
				cube_list[2][2] = c_coloring
			if Side_Square == '23':
				ui.Side_2_Square_3.setStyleSheet( b_coloring )
				cube_list[2][3] = c_coloring
			if Side_Square == '24':
				ui.Side_2_Square_4.setStyleSheet( b_coloring )
				cube_list[2][4] = c_coloring
			if Side_Square == '25':
				ui.Side_2_Square_5.setStyleSheet( b_coloring )
				cube_list[2][5] = c_coloring
			if Side_Square == '26':
				ui.Side_2_Square_6.setStyleSheet( b_coloring )
				cube_list[2][6] = c_coloring
			if Side_Square == '27':
				ui.Side_2_Square_7.setStyleSheet( b_coloring )
				cube_list[2][7] = c_coloring
			if Side_Square == '28':
				ui.Side_2_Square_8.setStyleSheet( b_coloring )
				cube_list[2][8] = c_coloring

			if Side_Square == '30':
				ui.Side_3_Square_0.setStyleSheet( b_coloring )
				cube_list[3][0] = c_coloring
			if Side_Square == '31':
				ui.Side_3_Square_1.setStyleSheet( b_coloring )
				cube_list[3][1] = c_coloring
			if Side_Square == '32':
				ui.Side_3_Square_2.setStyleSheet( b_coloring )
				cube_list[3][2] = c_coloring
			if Side_Square == '33':
				ui.Side_3_Square_3.setStyleSheet( b_coloring )
				cube_list[3][3] = c_coloring
			if Side_Square == '34':
				ui.Side_3_Square_4.setStyleSheet( b_coloring )
				cube_list[3][4] = c_coloring
			if Side_Square == '35':
				ui.Side_3_Square_5.setStyleSheet( b_coloring )
				cube_list[3][5] = c_coloring
			if Side_Square == '36':
				ui.Side_3_Square_6.setStyleSheet( b_coloring )
				cube_list[3][6] = c_coloring
			if Side_Square == '37':
				ui.Side_3_Square_7.setStyleSheet( b_coloring )
				cube_list[3][7] = c_coloring
			if Side_Square == '38':
				ui.Side_3_Square_8.setStyleSheet( b_coloring )
				cube_list[3][8] = c_coloring

			if Side_Square == '40':
				ui.Side_4_Square_0.setStyleSheet( b_coloring )
				cube_list[4][0] = c_coloring
			if Side_Square == '41':
				ui.Side_4_Square_1.setStyleSheet( b_coloring )
				cube_list[4][1] = c_coloring
			if Side_Square == '42':
				ui.Side_4_Square_2.setStyleSheet( b_coloring )
				cube_list[4][2] = c_coloring
			if Side_Square == '43':
				ui.Side_4_Square_3.setStyleSheet( b_coloring )
				cube_list[4][3] = c_coloring
			if Side_Square == '44':
				ui.Side_4_Square_4.setStyleSheet( b_coloring )
				cube_list[4][4] = c_coloring
			if Side_Square == '45':
				ui.Side_4_Square_5.setStyleSheet( b_coloring )
				cube_list[4][5] = c_coloring
			if Side_Square == '46':
				ui.Side_4_Square_6.setStyleSheet( b_coloring )
				cube_list[4][6] = c_coloring
			if Side_Square == '47':
				ui.Side_4_Square_7.setStyleSheet( b_coloring )
				cube_list[4][7] = c_coloring
			if Side_Square == '48':
				ui.Side_4_Square_8.setStyleSheet( b_coloring )
				cube_list[4][8] = c_coloring

			if Side_Square == '50':
				ui.Side_5_Square_0.setStyleSheet( b_coloring )
				cube_list[5][0] = c_coloring
			if Side_Square == '51':
				ui.Side_5_Square_1.setStyleSheet( b_coloring )
				cube_list[5][1] = c_coloring
			if Side_Square == '52':
				ui.Side_5_Square_2.setStyleSheet( b_coloring )
				cube_list[5][2] = c_coloring
			if Side_Square == '53':
				ui.Side_5_Square_3.setStyleSheet( b_coloring )
				cube_list[5][3] = c_coloring
			if Side_Square == '54':
				ui.Side_5_Square_4.setStyleSheet( b_coloring )
				cube_list[5][4] = c_coloring
			if Side_Square == '55':
				ui.Side_5_Square_5.setStyleSheet( b_coloring )
				cube_list[5][5] = c_coloring
			if Side_Square == '56':
				ui.Side_5_Square_6.setStyleSheet( b_coloring )
				cube_list[5][6] = c_coloring
			if Side_Square == '57':
				ui.Side_5_Square_7.setStyleSheet( b_coloring )
				cube_list[5][7] = c_coloring
			if Side_Square == '58':
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
		FOR ROTATING CUBE
'''

# def as calculator buttons # Возможно тоже сделать в одну функцию #?
def bp_x2():
	text = ui.turn_line.text()
	text = text.rstrip()
	ui.turn_line.setText(text + '2 ')
def bp_Apostrophe():
	text = ui.turn_line.text()
	text = text.rstrip()
	ui.turn_line.setText(text + "' ")
def bp_bra():
	text = ui.turn_line.text()
	ui.turn_line.setText(text + '(')
def bp_ket():
	text = ui.turn_line.text()
	text = text.rstrip()
	ui.turn_line.setText(text + ')')

def bp_U():
	text = ui.turn_line.text()
	ui.turn_line.setText(text + 'U ')
def bp_F():
	text = ui.turn_line.text()
	ui.turn_line.setText(text + 'F ')
def bp_R():
	text = ui.turn_line.text()
	ui.turn_line.setText(text + 'R ')
def bp_D():
	text = ui.turn_line.text()
	ui.turn_line.setText(text + 'D ')
def bp_B():
	text = ui.turn_line.text()
	ui.turn_line.setText(text + 'B ')
def bp_L():
	text = ui.turn_line.text()
	ui.turn_line.setText(text + 'L ')
def bp_E():
	text = ui.turn_line.text()
	ui.turn_line.setText(text + 'E ')
def bp_S():
	text = ui.turn_line.text()
	ui.turn_line.setText(text + 'S ')
def bp_M():
	text = ui.turn_line.text()
	ui.turn_line.setText(text + 'M ')

def bp_Backspace():
	text = ui.turn_line.text()
	text = text.rstrip()
	ui.turn_line.setText(text)
	ui.turn_line.backspace()

def bp_Enter(): # Проверить как лучше с сохранением и запуском в обоих режимах #?
	#'''
	pass
	'''
	# Rotation painting cube
	global cube_list
	turn_string = ui.turn_line.text()
	SCube.rotate_cube(SCube.check_string(turn_string), cube_list)
	print(SCube.list_to_string(cube_list))
	SCube.saving_cube(cube_list)
	#SCube.painting_cube(cube_list)



	#cube_list_to_buttons_cube()



	#global text_for_sms_as_cmd
	#text_for_sms_as_cmd = ''
	#sms_as_cmd_print()
	
	#Откуда:
	"""
	из SCube.check_string 
	print('Строка не подходит для вращения кубика')
	print(wherefrom_string, end = '\n\n') х2
	
	
	из SCube.rotate_cube
	print('turn: ' + turn + ' is not turn')
	
	
	из SCube.loading_cube
	print('Saving directory does not exist. Check and try again.')
	"""

	#'''

def bp_Clear_all():
	ui.turn_line.clear()

def bp_Cut():
	ui.turn_line.selectAll()
	ui.turn_line.cut()
def bp_Copy():
	ui.turn_line.selectAll()
	ui.turn_line.copy()
def bp_Paste():
	ui.turn_line.end(False)
	ui.turn_line.paste()


# Using as calculator buttons
ui.x2.clicked.connect( bp_x2 )
ui.Apostrophe.clicked.connect( bp_Apostrophe )
ui.bra.clicked.connect( bp_bra )
ui.ket.clicked.connect( bp_ket )

ui.U.clicked.connect( bp_U )
ui.F.clicked.connect( bp_F )
ui.R.clicked.connect( bp_R )
ui.D.clicked.connect( bp_D )
ui.B.clicked.connect( bp_B )
ui.L.clicked.connect( bp_L )
ui.E.clicked.connect( bp_E )
ui.S.clicked.connect( bp_S )
ui.M.clicked.connect( bp_M )

ui.Backspace.clicked.connect( bp_Backspace )
ui.Enter.clicked.connect( bp_Enter )
ui.Clear_all.clicked.connect( bp_Clear_all )
ui.Cut.clicked.connect( bp_Cut )
ui.Copy.clicked.connect( bp_Copy )
ui.Paste.clicked.connect( bp_Paste )



# Choose Save or Load Cube
#"""

Saving_to_last = False
Saving_to_mine = False

Loading_from_last = False
Loading_from_start = False
Loading_from_mine = False


def Choose_save_or_load():
	global text_for_sms_as_cmd

	global Saving_to_last
	global Saving_to_mine

	if ui.Save_to_last.isChecked():
		text_for_sms_as_cmd = 'Using Saving to last\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_print()

		ui.Save_to_last.setStyleSheet(	"QRadioButton{\n"
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

	elif not ui.Save_to_last.isChecked():
		ui.Save_to_last.setStyleSheet(	"QRadioButton{\n"
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

	Saving_to_last = ui.Save_to_last.isChecked()


	if ui.Save_to_mine.isChecked():
		text_for_sms_as_cmd = 'Using Saving to mine\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_print()

		ui.Save_to_mine.setStyleSheet(	"QRadioButton{\n"
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

	elif not ui.Save_to_mine.isChecked():
		ui.Save_to_mine.setStyleSheet(	"QRadioButton{\n"
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

	Saving_to_mine = ui.Save_to_mine.isChecked()


#def Choose_load(): #?
#	global text_for_sms_as_cmd

	global Loading_from_last
	global Loading_from_start
	global Loading_from_mine

	if ui.Load_from_last.isChecked():
		text_for_sms_as_cmd = 'Using Loading from last\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_print()

		ui.Load_from_last.setStyleSheet(	"QRadioButton{\n"
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

	elif not ui.Load_from_last.isChecked():
		ui.Load_from_last.setStyleSheet(	"QRadioButton{\n"
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

	Loading_from_last = ui.Load_from_last.isChecked()


	if ui.Load_from_start.isChecked():
		text_for_sms_as_cmd = 'Using Loading from start\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_print()

		ui.Load_from_start.setStyleSheet(	"QRadioButton{\n"
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

	elif not ui.Load_from_start.isChecked():
		ui.Load_from_start.setStyleSheet(	"QRadioButton{\n"
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

	Loading_from_start = ui.Load_from_start.isChecked()


	if ui.Load_from_mine.isChecked():
		text_for_sms_as_cmd = 'Using Loading from mine\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_print()

		ui.Load_from_mine.setStyleSheet(	"QRadioButton{\n"
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

	elif not ui.Load_from_mine.isChecked():
		ui.Load_from_mine.setStyleSheet(	"QRadioButton{\n"
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

	Loading_from_mine = ui.Load_from_mine.isChecked()

ui.Save_to_last.clicked.connect( Choose_save_or_load )#Choose_save
ui.Save_to_mine.clicked.connect( Choose_save_or_load )#Choose_save

ui.Load_from_last.clicked.connect( Choose_save_or_load )#Choose_load
ui.Load_from_start.clicked.connect( Choose_save_or_load )#Choose_load
ui.Load_from_mine.clicked.connect( Choose_save_or_load )#Choose_load
#"""

'''
def coloring(step = 1): #Переписать норм #???
	"""
	Меняет короткие названия цветов на полные
	"""
	global cube_list

	if step == 1:
		colors = {'y': 'Yellow', 'o': 'Orange', 'b': 'Blue', 'r': 'Red', 'w': 'White','g': 'Green'}

		for side in range(len(cube_list)):
			for square in range(len(cube_list[side])):
				color = cube_list[side][square]
				if color in colors:
					cube_list[side][square] = colors.get(color, ' ')
	elif step == 2:
		colors = {'Yellow': 'y', 'Orange': 'o', 'Blue': 'b', 'Red': 'r', 'White': 'w','Green': 'g'}

		for side in range(len(cube_list)):
			for square in range(len(cube_list[side])):
				color = cube_list[side][square]
				if color in colors:
					cube_list[side][square] = colors.get(color, ' ')
	else:
		print('Wrong step in function: coloring')

	#print(cube_list)
	return cube_list
'''

# Rotate buttons cube # Работает при вкл Enter_cube
def cube_list_to_buttons_cube(cube_buttons): # Перекинуть ближе к концу, для избежания ошибок #?
	global Entering_cube_loading

	cube_buttons = SCube.coloring(cube_buttons, 1)
	print(SCube.list_to_string(cube_buttons))

	Entering_cube_loading = True
	
	for side in range(len(cube_buttons)):
		for square in range(len(cube_buttons[side])):
			color = cube_buttons[side][square]
			bp_coloring(color)
			SS = str(side) + str(square)
			bp_SS(SS)

	Entering_cube_loading = False


	'''									#?
	
	global Typing_rotate				#?
	global Rotating_immediately			#?

	if Typing_rotate: # Typing_rotate or Rotating_immediately:
		

	if Rotating_immediately:

	#'''




#Save and Load Cube #Посмотреть как сохранять в txt либо при нажатии на энтер либо выбор возле сейв
#"""

def save(cube_list_for_saving=[], with_txt='No'): #????
	global cube_list
	global text_for_sms_as_cmd

	where_saving = ''

	if cube_list_for_saving == []:
		text_for_sms_as_cmd = 'cube_list_for_saving is empty. cube_list will saving\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_print()
	cube_list_for_saving = cube_list

	if Saving_to_last:
		where_saving = 'Save_to_last'
	elif Saving_to_mine:
		where_saving = 'Save_to_mine'
	else:
		text_for_sms_as_cmd = 'Chose where saving\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_print()

	if where_saving != '':
		text_for_sms_as_cmd = 'Saving...\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_print()
		SCube.saving_cube(cube_list_for_saving, where_saving, with_txt)
		text_for_sms_as_cmd = 'Saving complite\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_print()

	#ui.Save_to_last.setChecked(False)
	#ui.Save_to_mine.setChecked(False)
	#При нажати на кнопки после сохранеия убирает выбор #.setChecked(False) #?


def load():
	global cube_list
	global text_for_sms_as_cmd

	wherefrom_loading = ''

	if Loading_from_last:
		wherefrom_loading = 'Loading_from_last'
	elif Loading_from_start:
		wherefrom_loading = 'Loading_from_start'
	elif Loading_from_mine:
		wherefrom_loading = 'Loading_from_mine'
	else:
		text_for_sms_as_cmd = 'Chose what loading\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_print()

	if wherefrom_loading != '':
		text_for_sms_as_cmd = 'Loading...\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_print()
		
		cube_list = SCube.loading_cube(wherefrom_loading)
		cube_list_to_buttons_cube(cube_list) #?
		
		text_for_sms_as_cmd = 'Loading complite\n\n'
		print(text_for_sms_as_cmd, end = '')
		sms_as_cmd_print()

	#ui.Load_from_last.setChecked(False)
	#ui.Load_from_start.setChecked(False)
	#ui.Load_from_mine.setChecked(False)
	#При нажати на кнопки после загрузки убирает выбор #.setChecked(False) #?
	

ui.Save.clicked.connect( save ) #????
ui.Load.clicked.connect( load ) #???? Проверить как работает
#"""


# Run main loop
sys.exit(app.exec_())




# Временные строки

