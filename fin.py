# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 23:38:43 2020

@author: koka5
"""
import init
import tkinter as tk

def start():
    """
    запуск игры после нажатия на кнопку СТАРТ, отрисовка канвас_гейм
    """
    init.canvas_start.destroy()
    init.canvas_game.pack()
    
def play_again():
    """
    игра заново
    """
    init.canvas_finish.destroy()
    init.canvas_game.pack()

def finish(text):
    """
    запуск канвас_финиш, отрисовка его и элементов внутри
    """
    init.canvas_game.destroy()
    init.canvas_finish.pack()
    init.canvas_finish.create_text(400, 300, text=text, justify = tk.LEFT,\
                       font = ("Times", "24", "bold italic"), fill = '#0000ff')
        
    