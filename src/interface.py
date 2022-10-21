import PySimpleGUI as sg
import ctypes

#
imageSizes = [
    '128', '512', '1024'
    ]

#Variavel de definicao de formato da interface, alem da especificacao dos objetos 
layout = [
    [sg.Text('Tamanho da imagem (nxn)'), sg.OptionMenu(values=imageSizes, default_value='128', key='size')],
    [sg.Text('valores x minimo e maximo'), sg.Input(key="xmin"), sg.Input(key="xmax")],
    [sg.Text('Valores sugeridos: -2, e 2')],
    [sg.Text('valores y minimo e maximo'), sg.Input(key="ymin"), sg.Input(key="ymax")],
    [sg.Text('Valores sugeridos: -2, e 2')],
    [sg.Button('Gerar imagem')],
    [sg.Text('', key='message')],
    [sg.Image("", key="image")]
]

def main():
    #criacao da instancia da interface
    window = sg.Window('Mandelbrot', layout)

    #carregamento da biblioteca compartilhada
    lib = ctypes.CDLL("mlibExt.so", winmode=0x8)

    #loop do programa
    while True:
        #variaveis de evento e dados da interface
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == 'Gerar imagem':
            size = int(float(values['size']))
            ymin = values['ymin']
            xmin = values['xmin']
            ymax = values['ymax']
            xmax = values['xmax']

            #validacao dos campos
            if ymin == '' or xmin == '' or ymax == '' or xmax == '':
                window['message'].update('Todos os campos devem ser preenchidos!')
            else:
                window['message'].update('')

                #especificacao dos tipos dos argumentos do metodo da biblioteca compartilhada
                lib.mandelbrotExtExecute.argtypes = (ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int, ctypes.c_int)
                
                #execucao do metodo
                lib.mandelbrotExtExecute(ctypes.c_double(float(xmin)), ctypes.c_double(float(xmax)), ctypes.c_double(float(ymin)),ctypes.c_double(float(ymax)), ctypes.c_int(1000), ctypes.c_int(size))

                #obtem a imagem gerada e coloca na interface
                window['image'].Update('pic.ppm')

main()
                

    