#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  relogio.py
#
#  Autor: Eduardo Couto Rodrigues <eduardocooouto@gmail.com>
#  Criado em: 12/05/16 10:13:08
#  Usuário: Eduardo
#
#  Função do programa: Cria um relogio digital usando tkinter, tadPainel e datetime.
#  Versão inicial: 1.0
#  ----------------------------------------------------------------
import tkinter
import tadPainel
import time
from datetime import datetime
from tkinter import font

def criaRelogio():

    posiX = 30
    posiY = 100 #posicao fixa de y
    espaco = 1
    espaco_digitos = 25
    tamando_quadrado = 25

    lst_digitos = [None]

    #Criando displays horas
    tamanho_painel = 1
    pos = posiX+espaco
    for i in range(3):

        for i in range(2):
            digito = tadPainel.cria(pos, posiY, 4, 5, tamando_quadrado, tamando_quadrado, 2, 'grey', 'red', 'white')
            tamanho_painel = tadPainel.len_painel_largura(digito)
            lst_digitos.append(digito)
            pos += tamanho_painel+espaco_digitos
        pos += 25 #distancia para os 2 pontos separadores


    return lst_digitos

def atualiza_digito(digito,numero,tela):
    dic = {
        0:[[1, 1], [1, 2], [1, 3], [1, 4], [2, 1], [2, 4], [3, 1], [3, 4], [4, 1], [4, 4], [5, 1], [5, 2], [5, 3], [5, 4]],
        1:[[1, 4], [2, 4], [3, 4], [4, 4], [5, 4]],
        2:[[1, 1], [1, 2], [1, 3], [1, 4], [2, 4], [3, 1], [3, 2], [3, 3], [3, 4], [4, 1], [5, 1], [5, 2], [5, 3], [5, 4]],
        3:[[1, 1], [1, 2], [1, 3], [1, 4], [2, 4], [3, 1], [3, 2], [3, 3], [3, 4], [4, 4], [5, 1], [5, 2], [5, 3], [5, 4]],
        4:[[1, 1], [1, 4], [2, 1], [2, 4], [3, 1], [3, 2], [3, 3], [3, 4], [4, 4], [5, 4]],
        5:[[1, 1], [1, 2], [1, 3], [1, 4], [2, 1], [3, 1], [3, 2], [3, 3], [3, 4], [4, 4], [5, 1], [5, 2], [5, 3], [5, 4]],
        6:[[1, 1], [1, 2], [1, 3], [1, 4], [2, 1], [3, 1], [3, 2], [3, 3], [3, 4], [4, 1], [4, 4], [5, 1], [5, 2], [5, 3], [5, 4]],
        7:[[1, 1], [1, 2], [1, 3], [1, 4], [2, 4], [3, 4], [4, 4], [5, 4]],
        8:[[1, 1], [1, 2], [1, 3], [1, 4], [2, 1], [2, 4], [3, 1], [3, 2], [3, 3], [3, 4], [4, 1], [4, 4], [5, 1], [5, 2], [5, 3], [5, 4]],
        9:[[1, 1], [1, 2], [1, 3], [1, 4], [2, 1], [2, 4], [3, 1], [3, 2], [3, 3], [3, 4], [4, 4], [5, 4]]
    }
    lst = dic[numero] # Esta lista contém todos os pontos que devem estar acesos.
    lst2 = [[2,2],[2,3],[4,2],[4,3]]

    #Desliga todos os pontos do digito
    for i in range(5):
        for j in range(4):
            tadPainel.onoff(i+1,j+1,digito,tela,False,'snow2')

    #Faz 2 lacunas no digito
    for tupla in lst2:
        tadPainel.onoff(tupla[0], tupla[1], digito, tela, True,'white')

    # desenha o numero
    for tupla in lst:
        tadPainel.onoff(tupla[0],tupla[1],digito,tela,True)


def main():

    janela = tkinter.Tk()

    # Define as dimensões da área interior da janela, o canvas.
    canvas_altura = 300
    canvas_largura = 900

    # Cria o TAD área de desenho e o encaixa no interior da janela. Janela = canvas + bordas + barra de título.
    #
    # Para outras propriedades do canvas:
    #   http://www.tutorialspoint.com/python/tk_canvas.htm
    #   http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/canvas.html
    #   [x,y,largura,altura,largq,altq,espaco,corOff,corON,corBg]
    #   Imagem com várias cores = http://www.geocities.ws/thezipguy/misc/colornames_1.png

    tela = tkinter.Canvas(janela, bg='white', width=canvas_largura, height=canvas_altura)
    tela.pack()
    font.families()
    courier36 = font.Font(family='Courier', size=18, weight='bold')
    tela.create_text(canvas_largura // 2, 50, text="Relógio Digital", font=courier36)

    relogio = criaRelogio()


    # Atualizando todos os digitos
    while True:
        now = datetime.now()
        hora = str(now.hour)
        if len(hora) == 1:
            hora = '0'+hora
        minutos = str(now.minute)
        if len(minutos) == 1:
            minutos = '0'+minutos
        segundos = str(now.second)
        if len(segundos) == 1:
            segundos = '0'+segundos
        atualiza_digito(relogio[1], int(hora[0]), tela)
        atualiza_digito(relogio[2], int(hora[1]), tela)
        atualiza_digito(relogio[3], int(minutos[0]), tela)
        atualiza_digito(relogio[4], int(minutos[1]), tela)
        atualiza_digito(relogio[5], int(segundos[0]), tela)
        atualiza_digito(relogio[6], int(segundos[1]), tela)
        tela.update()
        time.sleep(0.01)

    # Conclui o arranjo dos elementos no canvas/área de desenho. Nesse caso, não existe
    # nenhum elemento no interior do canvas. Mesmo assim a chamada deve ser feita.
    tela.pack()

    # Ativa a janela processando (desenhando) todos os objetos no interior do seu canvas.
    # No caso corrente, o único elemento no interior do canvas é o próprio canvas, ou a
    # própria superfície de desenho.
    janela.mainloop()
    return 0


if __name__ == '__main__':
    main()
