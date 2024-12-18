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
"""
#	ОТКРЫТИЕ В ОКНЕ
"""

import graphics as gr

length = 800
height = 900
window = gr.GraphWin('Simulation of cube on computer', length, height)
size = 100
square_size = size - 70
width = 5
x, y = 100, height/2 - 2*size



def coloring(cube_list):
	"""
	Меняет короткие названия цветов на полные
	"""
	colors = {'y': 'yellow', 'o': 'orange', 'b': 'blue', 'r': 'red', 'w': 'white','g': 'green'}

	for side in range(len(cube_list)):
		for square in range(len(cube_list[side])):
			color = cube_list[side][square]
			if color in colors:
				cube_list[side][square] = colors.get(color, ' ')

	#print(cube_list)
	return cube_list

#print(coloring(cube_list))
coloring(cube_list)

def painting_cube():
	"""
	Выдает координаты по #
	"""
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

painting_cube()

"""
def painting_all_cube():
	'''
	Возможно можно ещё сократить сделав с side тоже что и с square
	'''

																			#left_side
	side_x, side_y = x, y
	side_painting(side_x, side_y, size)
	painting_cube(side_x, side_y)
																			#front_side
	side_x, side_y = x + 2*(size + width), y
	side_painting(side_x, side_y, size)
	painting_cube(side_x, side_y)

																			#right_side
	side_x, side_y = x + 4*(size + width), y
	side_painting(side_x, side_y, size)
	painting_cube(side_x, side_y)
																			#top
	side_x, side_y = x + 2*(size + width), y - 2*(size + width)
	side_painting(side_x, side_y, size)
	painting_cube(side_x, side_y)
																			#bottom
	side_x, side_y = x + 2*(size + width), y + 2*(size + width)
	side_painting(side_x, side_y, size)
	painting_cube(side_x, side_y)
																			#back_side
	side_x, side_y = x + 2*(size + width), y + 4*(size + width)
	side_painting(side_x, side_y, size)
	painting_cube(side_x, side_y)

painting_all_cube()
"""
'''
	coordinates_square_x = {	0: side_x + width,
								1: side_x + width + 2*(width - 3) + 2*square_size,
								2: side_x + width + 4*(width - 3) + 4*square_size,
								3: side_x + width,
								4: side_x + width + 2*(width - 3) + 2*square_size,
								5: side_x + width + 4*(width - 3) + 4*square_size,
								6: side_x + width,
								7: side_x + width + 2*(width - 3) + 2*square_size,
								8: side_x + width + 4*(width - 3) + 4*square_size
							}
	
	coordinates_square_y = {	0: side_y + width,
								1: side_y + width,
								2: side_y + width,
								3: side_y + width + 2*(width - 3) + 2*square_size,
								4: side_y + width + 2*(width - 3) + 2*square_size,
								5: side_y + width + 2*(width - 3) + 2*square_size,
								6: side_y + width + 4*(width - 3) + 4*square_size,
								7: side_y + width + 4*(width - 3) + 4*square_size,
								8: side_y + width + 4*(width - 3) + 4*square_size
							}
'''

#'''ЗАКРЫТИЕ НА КОМПЬЮТЕРЕ
print()
input('Exit')
#'''
