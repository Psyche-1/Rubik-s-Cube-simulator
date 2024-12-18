'''
Сделать переключение между 3 режимами:
1 Ввод кубика кнопками в All cube
2 Добавить чтобы кубик сразу вращался при нажатии Enter
ИЛИ
3, чтобы кубик сразу вращался при нажатии кнопок, а не при нажатии Enter
'''

from PySide2 import QtCore, QtGui, QtWidgets
import sys
#from Buttons_and_RadioButton_2 import Ui_Window
from All_Cube import Ui_Window
# Найти как передать переменную в Simulation_of_cube_comp word = 'Open'
#import Simulation_of_cube_comp as SCube

# Create application
app = QtWidgets.QApplication(sys.argv)


# Create window and init UI
Window = QtWidgets.QWidget()
ui = Ui_Window()
ui.setupUi(Window)
Window.show()

# Hook logic
def radio_button_Enter_cube():
	print("Enter_cube_Yes")
	#print("Enter_cube_No") # Если найду как поймать не только включение, но и выключение

def radio_button_Typing_rotate():
	print("Typing_rotate_Yes")
	#print("Typing_rotate_No")

def radio_button_Rotate_immediately():
	print("Rotate_immediately_Yes")
	#print("Rotate_immediately_No")

ui.Enter_cube.clicked.connect( radio_button_Enter_cube )
ui.Typing_rotate.clicked.connect( radio_button_Typing_rotate )
ui.Rotate_immediately.clicked.connect( radio_button_Rotate_immediately )



def bp_x2():
	text = ui.lineEdit.text()
	text = text.rstrip()
	ui.lineEdit.setText(text + '2 ')
def bp_Apostrophe():
	text = ui.lineEdit.text()
	text = text.rstrip()
	ui.lineEdit.setText(text + "' ")
def bp_bra():
	text = ui.lineEdit.text()
	ui.lineEdit.setText(text + '(')
def bp_ket():
	text = ui.lineEdit.text()
	ui.lineEdit.setText(text + ')')

def bp_U():
	text = ui.lineEdit.text()
	ui.lineEdit.setText(text + 'U ')
def bp_F():
	text = ui.lineEdit.text()
	ui.lineEdit.setText(text + 'F ')
def bp_R():
	text = ui.lineEdit.text()
	ui.lineEdit.setText(text + 'R ')
def bp_D():
	text = ui.lineEdit.text()
	ui.lineEdit.setText(text + 'D ')
def bp_B():
	text = ui.lineEdit.text()
	ui.lineEdit.setText(text + 'B ')
def bp_L():
	text = ui.lineEdit.text()
	ui.lineEdit.setText(text + 'L ')
def bp_E():
	text = ui.lineEdit.text()
	ui.lineEdit.setText(text + 'E ')
def bp_S():
	text = ui.lineEdit.text()
	ui.lineEdit.setText(text + 'S ')
def bp_M():
	text = ui.lineEdit.text()
	ui.lineEdit.setText(text + 'M ')

def bp_Backspace():
	text = ui.lineEdit.text()
	text = text.rstrip()
	ui.lineEdit.setText(text)
	ui.lineEdit.backspace()

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

def bp_Enter():
	#'''
	pass
	'''
	string = ui.lineEdit.text()
	SCube.rotate_cube(SCube.check_string(string), cube_list)
	print(SCube.list_to_string(cube_list))
	SCube.painting_cube(cube_list)
	#'''


def bp_Clear_all():
	ui.lineEdit.clear()

def bp_Cut():
	ui.lineEdit.selectAll()
	ui.lineEdit.cut()
def bp_Copy():
	ui.lineEdit.selectAll()
	ui.lineEdit.copy()
def bp_Paste():
	ui.lineEdit.end(False)
	ui.lineEdit.paste()


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


b_coloring = ''

def bp_Yellow_Button():
	global b_coloring
	b_coloring = ("QPushButton{\n"
"  background-color: rgb(183, 180, 0);\n"
"  width: 50px;\n"
"  height: 50px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: yellow;\n"
"}")

def bp_Orange_Button():
	global b_coloring
	b_coloring = ("QPushButton{\n"
"  background-color: rgb(193, 122, 0);\n"
"  width: 50px;\n"
"  height: 50px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: silver;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: orange;\n"
"}")

def bp_Blue_Button():
	global b_coloring
	b_coloring = ("QPushButton{\n"
"  background-color: rgb(0, 0, 170);\n"
"  width: 50px;\n"
"  height: 50px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: blue;\n"
"}")

def bp_Red_Button():
	global b_coloring
	b_coloring = ("QPushButton{\n"
"  background-color: rgb(160, 0, 0);\n"
"  width: 50px;\n"
"  height: 50px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: silver;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: red;\n"
"}")

def bp_White_Button():
	global b_coloring
	b_coloring = ("QPushButton{\n"
"  background-color: silver;\n"
"  width: 50px;\n"
"  height: 50px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: gray;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: white;\n"
"}")

def bp_Green_Button():
	global b_coloring
	b_coloring = ("QPushButton{\n"
"  background-color: green;\n"
"  width: 50px;\n"
"  height: 50px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: silver;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: rgb(0, 160, 0);\n"
"}")


def bp_00():
	ui.Side_0_Square_0.setStyleSheet( b_coloring )
def bp_01():
	ui.Side_0_Square_1.setStyleSheet( b_coloring )
def bp_02():
	ui.Side_0_Square_2.setStyleSheet( b_coloring )
def bp_03():
	ui.Side_0_Square_3.setStyleSheet( b_coloring )
def bp_04():
	ui.Side_0_Square_4.setStyleSheet( b_coloring )
def bp_05():
	ui.Side_0_Square_5.setStyleSheet( b_coloring )
def bp_06():
	ui.Side_0_Square_6.setStyleSheet( b_coloring )
def bp_07():
	ui.Side_0_Square_7.setStyleSheet( b_coloring )
def bp_08():
	ui.Side_0_Square_8.setStyleSheet( b_coloring )

def bp_10():
	ui.Side_1_Square_0.setStyleSheet( b_coloring )
def bp_11():
	ui.Side_1_Square_1.setStyleSheet( b_coloring )
def bp_12():
	ui.Side_1_Square_2.setStyleSheet( b_coloring )
def bp_13():
	ui.Side_1_Square_3.setStyleSheet( b_coloring )
def bp_14():
	ui.Side_1_Square_4.setStyleSheet( b_coloring )
def bp_15():
	ui.Side_1_Square_5.setStyleSheet( b_coloring )
def bp_16():
	ui.Side_1_Square_6.setStyleSheet( b_coloring )
def bp_17():
	ui.Side_1_Square_7.setStyleSheet( b_coloring )
def bp_18():
	ui.Side_1_Square_8.setStyleSheet( b_coloring )

def bp_20():
	ui.Side_2_Square_0.setStyleSheet( b_coloring )
def bp_21():
	ui.Side_2_Square_1.setStyleSheet( b_coloring )
def bp_22():
	ui.Side_2_Square_2.setStyleSheet( b_coloring )
def bp_23():
	ui.Side_2_Square_3.setStyleSheet( b_coloring )
def bp_24():
	ui.Side_2_Square_4.setStyleSheet( b_coloring )
def bp_25():
	ui.Side_2_Square_5.setStyleSheet( b_coloring )
def bp_26():
	ui.Side_2_Square_6.setStyleSheet( b_coloring )
def bp_27():
	ui.Side_2_Square_7.setStyleSheet( b_coloring )
def bp_28():
	ui.Side_2_Square_8.setStyleSheet( b_coloring )

def bp_30():
	ui.Side_3_Square_0.setStyleSheet( b_coloring )
def bp_31():
	ui.Side_3_Square_1.setStyleSheet( b_coloring )
def bp_32():
	ui.Side_3_Square_2.setStyleSheet( b_coloring )
def bp_33():
	ui.Side_3_Square_3.setStyleSheet( b_coloring )
def bp_34():
	ui.Side_3_Square_4.setStyleSheet( b_coloring )
def bp_35():
	ui.Side_3_Square_5.setStyleSheet( b_coloring )
def bp_36():
	ui.Side_3_Square_6.setStyleSheet( b_coloring )
def bp_37():
	ui.Side_3_Square_7.setStyleSheet( b_coloring )
def bp_38():
	ui.Side_3_Square_8.setStyleSheet( b_coloring )

def bp_40():
	ui.Side_4_Square_0.setStyleSheet( b_coloring )
def bp_41():
	ui.Side_4_Square_1.setStyleSheet( b_coloring )
def bp_42():
	ui.Side_4_Square_2.setStyleSheet( b_coloring )
def bp_43():
	ui.Side_4_Square_3.setStyleSheet( b_coloring )
def bp_44():
	ui.Side_4_Square_4.setStyleSheet( b_coloring )
def bp_45():
	ui.Side_4_Square_5.setStyleSheet( b_coloring )
def bp_46():
	ui.Side_4_Square_6.setStyleSheet( b_coloring )
def bp_47():
	ui.Side_4_Square_7.setStyleSheet( b_coloring )
def bp_48():
	ui.Side_4_Square_8.setStyleSheet( b_coloring )

def bp_50():
	ui.Side_5_Square_0.setStyleSheet( b_coloring )
def bp_51():
	ui.Side_5_Square_1.setStyleSheet( b_coloring )
def bp_52():
	ui.Side_5_Square_2.setStyleSheet( b_coloring )
def bp_53():
	ui.Side_5_Square_3.setStyleSheet( b_coloring )
def bp_54():
	ui.Side_5_Square_4.setStyleSheet( b_coloring )
def bp_55():
	ui.Side_5_Square_5.setStyleSheet( b_coloring )
def bp_56():
	ui.Side_5_Square_6.setStyleSheet( b_coloring )
def bp_57():
	ui.Side_5_Square_7.setStyleSheet( b_coloring )
def bp_58():
	ui.Side_5_Square_8.setStyleSheet( b_coloring )



ui.Yellow_Button.clicked.connect( bp_Yellow_Button )
ui.Orange_Button.clicked.connect( bp_Orange_Button )
ui.Blue_Button.clicked.connect( bp_Blue_Button )
ui.Red_Button.clicked.connect( bp_Red_Button )
ui.White_Button.clicked.connect( bp_White_Button )
ui.Green_Button.clicked.connect( bp_Green_Button )


ui.Side_0_Square_0.clicked.connect( bp_00 )
ui.Side_0_Square_1.clicked.connect( bp_01 )
ui.Side_0_Square_2.clicked.connect( bp_02 )
ui.Side_0_Square_3.clicked.connect( bp_03 )
ui.Side_0_Square_4.clicked.connect( bp_04 )
ui.Side_0_Square_5.clicked.connect( bp_05 )
ui.Side_0_Square_6.clicked.connect( bp_06 )
ui.Side_0_Square_7.clicked.connect( bp_07 )
ui.Side_0_Square_8.clicked.connect( bp_08 )

ui.Side_1_Square_0.clicked.connect( bp_10 )
ui.Side_1_Square_1.clicked.connect( bp_11 )
ui.Side_1_Square_2.clicked.connect( bp_12 )
ui.Side_1_Square_3.clicked.connect( bp_13 )
ui.Side_1_Square_4.clicked.connect( bp_14 )
ui.Side_1_Square_5.clicked.connect( bp_15 )
ui.Side_1_Square_6.clicked.connect( bp_16 )
ui.Side_1_Square_7.clicked.connect( bp_17 )
ui.Side_1_Square_8.clicked.connect( bp_18 )

ui.Side_2_Square_0.clicked.connect( bp_20 )
ui.Side_2_Square_1.clicked.connect( bp_21 )
ui.Side_2_Square_2.clicked.connect( bp_22 )
ui.Side_2_Square_3.clicked.connect( bp_23 )
ui.Side_2_Square_4.clicked.connect( bp_24 )
ui.Side_2_Square_5.clicked.connect( bp_25 )
ui.Side_2_Square_6.clicked.connect( bp_26 )
ui.Side_2_Square_7.clicked.connect( bp_27 )
ui.Side_2_Square_8.clicked.connect( bp_28 )

ui.Side_3_Square_0.clicked.connect( bp_30 )
ui.Side_3_Square_1.clicked.connect( bp_31 )
ui.Side_3_Square_2.clicked.connect( bp_32 )
ui.Side_3_Square_3.clicked.connect( bp_33 )
ui.Side_3_Square_4.clicked.connect( bp_34 )
ui.Side_3_Square_5.clicked.connect( bp_35 )
ui.Side_3_Square_6.clicked.connect( bp_36 )
ui.Side_3_Square_7.clicked.connect( bp_37 )
ui.Side_3_Square_8.clicked.connect( bp_38 )

ui.Side_4_Square_0.clicked.connect( bp_40 )
ui.Side_4_Square_1.clicked.connect( bp_41 )
ui.Side_4_Square_2.clicked.connect( bp_42 )
ui.Side_4_Square_3.clicked.connect( bp_43 )
ui.Side_4_Square_4.clicked.connect( bp_44 )
ui.Side_4_Square_5.clicked.connect( bp_45 )
ui.Side_4_Square_6.clicked.connect( bp_46 )
ui.Side_4_Square_7.clicked.connect( bp_47 )
ui.Side_4_Square_8.clicked.connect( bp_48 )

ui.Side_5_Square_0.clicked.connect( bp_50 )
ui.Side_5_Square_1.clicked.connect( bp_51 )
ui.Side_5_Square_2.clicked.connect( bp_52 )
ui.Side_5_Square_3.clicked.connect( bp_53 )
ui.Side_5_Square_4.clicked.connect( bp_54 )
ui.Side_5_Square_5.clicked.connect( bp_55 )
ui.Side_5_Square_6.clicked.connect( bp_56 )
ui.Side_5_Square_7.clicked.connect( bp_57 )
ui.Side_5_Square_8.clicked.connect( bp_58 )

# Run main loop
sys.exit(app.exec_())
