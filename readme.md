# Implementação com visualização gráfica e duas linguagens de programação

Trabalho prático onde deve ser implementado algum cálculo através da linguagem c, e prover uma interface em python para fazer a comunicação e obter os dados.

## Arquivos

* interface.py - Onde está presente a construção da interface, e a própria leitura da biblioteca)
* mandelbrotExt.c - Arquivo de geração de uma imagem de uma fractal de mandelbrot

## Como compilar e executar (Feito no windows)
Dentro da pasta src execute os comandos:

* gcc -fPIC -shared -o mlibExt.so mandelbrotExt.c
* py interface.py

## Parâmetros recomendados:
* xmin = -2.0 ou 0.27085
* xmax = 2.0 ou 0.27100
* ymin = -2.0 ou 0.004640
* ymax = 2.0 ou 0.004810

## Screenshot

![alt text](https://i.postimg.cc/kXvq0j1N/Captura-de-Tela-77.png)