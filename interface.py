import PySimpleGUI as sg
import ctypes

imageSizes = [
    '128', '512', '1024'
    ]

layout = [
    [sg.Text('Tamanho da imagem (nxn)'), sg.OptionMenu(values=imageSizes, default_value='128', key='size')],
    [sg.Text('valores x minimo e maximo'), sg.Input(key="xmin"), sg.Input(key="xmax")],
    [sg.Text('Valores sugeridos: 0.27085, e 0.27100')],
    [sg.Text('valores y minimo e maximo'), sg.Input(key="ymin"), sg.Input(key="ymax")],
    [sg.Text('Valores sugeridos: 0.004640, e 0.004810')],
    [sg.Button('Gerar imagem')],
    [sg.Text('', key='message')],
    [sg.Image("", key="image")]
]

window = sg.Window('Mandelbrot', layout)
lib = ctypes.CDLL("mlibExt.so", winmode=0x8)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == 'Gerar imagem':
        size = int(float(values['size']))
        ymin = values['ymin']
        xmin = values['xmin']
        ymax = values['ymax']
        xmax = values['xmax']

        if ymin == '' or xmin == '' or ymax == '' or xmax == '':
            window['message'].update('Todos os campos devem ser preenchidos!')
        else:
            window['message'].update('')

            lib.mandelbrotExtExecute.argtypes = (ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int, ctypes.c_int)
            lib.mandelbrotExtExecute(ctypes.c_double(float(xmin)), ctypes.c_double(float(xmax)), ctypes.c_double(float(ymin)),ctypes.c_double(float(ymax)), ctypes.c_int(1000), ctypes.c_int(size))

            window['image'].Update('pic.ppm')
            

    