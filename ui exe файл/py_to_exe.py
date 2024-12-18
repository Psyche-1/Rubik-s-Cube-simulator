# python 6_py_to_exe.py

import os
import shutil

import PyInstaller.__main__


launch_folder = os.getcwd()
file_name = input('file_name: ')  # 'use_asu.py'
file_name_exe = file_name.replace('py', 'exe')
file_name_new_exe = file_name.replace('.py', '_new.exe')

# from_path = os.path.join(os.path.abspath('..'), file_name)
to_path = os.path.join(launch_folder, file_name)

# shutil.copyfile(from_path, to_path)


def py_to_exe():
	PyInstaller.__main__.run([
		file_name,
		'--onefile',
	])


py_to_exe()
# subprocess.call(r"python --onefile add_new_expertise.py")

from_path = os.path.join(launch_folder, 'dist', file_name_exe)
to_path = os.path.join(os.path.abspath('..'), file_name_exe)

shutil.move(from_path, to_path)

shutil.rmtree(os.path.join(launch_folder, '__pycache__'))
shutil.rmtree(os.path.join(launch_folder, 'build'))
shutil.rmtree(os.path.join(launch_folder, 'dist'))

os.unlink(file_name.replace('py', 'spec'))

input('Finish')
