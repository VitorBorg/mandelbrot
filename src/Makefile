install_python:
	pip install pysimplegui

compile_windows: 
	g++ -o mlib.so --shared -fPIC mandelbrotExt.c

windows: compile_windows
	python interface.py