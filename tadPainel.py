#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tadPainel.py
#
#  Autor: Eduardo Couto Rodrigues <eduardocooouto@gmail.com>
#  Criado em: 11/05/16 14:33:12
#  Usuário: Eduardo
#
#  Função do programa: Cria um painel usando tkinter.
#  Versão inicial: 1.0
#  ----------------------------------------------------------------


def cria(x,y,largura,altura,largq,altq,espaco,corOff,corON,corBg):
    return [x,y,largura,altura,largq,altq,espaco,corOff,corON,corBg]
    #       0 1    2       3     4     5    6      7      8    9
#fim def cria

def destroi():
    return None
#fim def destroi

def exibe(tadPainel,window):
    ''' Funcao que exibe o painel com os quadrados demarcados'''
    posX = tadPainel[0]
    posY = tadPainel[1]

    qtd_quadrados_linha = tadPainel[2]
    qtd_quadrados_coluna = tadPainel[3]

    larg_quadrado = tadPainel[4]
    alt_quadrado = tadPainel[5]

    espacamento = tadPainel[6]

    largura_total = len_painel_largura(tadPainel)
    altura_total = len_painel_altura(tadPainel)

    # Criando plano de fundo
    window.create_rectangle(posX, posY,posX+largura_total-1, posY+altura_total-1, width=0, fill=tadPainel[7])

    #Pintando as colunas
    for i in range(qtd_quadrados_linha-1):
        posx_linha = posX+((larg_quadrado+1) *(i+1)+espacamento * (i+1))
        posy_linha = posY
        pos_fimx = posX+((larg_quadrado+1) *(i+1)+espacamento * (i+1))
        pos_fimy = posY+altura_total #+(espacamento*qtd_quadrados_coluna)
        window.create_line(posx_linha, posy_linha, pos_fimx, pos_fimy, fill=tadPainel[9], width=espacamento)
    # fim for

    # Pintando as linhas
    for i in range(qtd_quadrados_coluna - 1):
        posx_linha = posX
        posy_linha = posY + ((alt_quadrado+1) * (i + 1)) + (espacamento * (i+1))
        pos_fimx = posX+largura_total
        pos_fimy = posY + ((alt_quadrado+1) * (i + 1)) + (espacamento * (i+1))
        window.create_line(posx_linha, posy_linha, pos_fimx, pos_fimy, fill=tadPainel[9], width=espacamento)
    # fim for
# fim def exibe

# Função que desliga ou liga algum quadrado do painel.
# Podendo escolher a cor caso necessário.

def onoff(linha,coluna,tadPainel,window,ligado,cor=None):

    larg_quadrado = tadPainel[4]
    alt_quadrado = tadPainel[5]

    espacamento = tadPainel[6]

    inicioX = tadPainel[0] +2
    inicioY = tadPainel[1] +2

    for i in range(coluna-1):
        inicioX += (larg_quadrado+1)+ espacamento
    # fim for
    fimX = inicioX + larg_quadrado

    for j in range(linha-1):
        inicioY += (alt_quadrado + 1) + espacamento

    fimY = inicioY + alt_quadrado
    # fim for
    if cor == None: #Verifica se é precisa pintar como uma cor especial.

        if ligado:
            cor = tadPainel[8]
        #fim if
        else:
            cor = tadPainel[7]
        #fim else
    #atualiza o área quadrado criando outro retângulo.
    window.create_rectangle(inicioX, inicioY, fimX, fimY, width=0, fill=cor)
#fim def onof

def len_painel_altura(tadPainel):

    qtd_quadrados_coluna = tadPainel[3]
    alt_quadrado = tadPainel[5]
    espacamento = tadPainel[6]

    return (alt_quadrado + 1) * qtd_quadrados_coluna + ((qtd_quadrados_coluna - 1) * espacamento)
#fim len_painel_altura

def len_painel_largura(tadPainel):

    qtd_quadrados_linha = tadPainel[2]
    larg_quadrado = tadPainel[4]
    espacamento = tadPainel[6]
    return (larg_quadrado + 1) * qtd_quadrados_linha + ((qtd_quadrados_linha - 1) * espacamento)
#fim def len_painel_largura

#fim tadPainel
