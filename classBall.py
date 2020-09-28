"""
@author: koka
"""

import const
import init
import tkinter as tk
import math as m
import time

class Ball():
    def __init__(self, ball_img, x, y):
        """
        класс типо снаряд, объект, и время полета
        """
        self.ball = init.canvas_game.create_image(x, y, image = ball_img, anchor = tk.NW)
        self.__t = 0
        
    def check_sky(self):
        """
        проверка неба для снаряда
        """
        if init.tank == init.tank1:
            sky_color1 = const.back.getpixel((init.canvas_game.coords(self.ball)[0],\
                                                  init.canvas_game.coords(self.ball)[1] + 10))
        else:
            sky_color1 = const.back.getpixel((init.canvas_game.coords(self.ball)[0] - 10,\
                                                  init.canvas_game.coords(self.ball)[1]))
        if sky_color1 == const.SKY:
            con = True
        elif sky_color1 == const.DIRT:
            con = False
        return con
        
    
    def chekCorR(self, elem):
        """
        проверка правой границы
        """
        if elem < 790:
            return True
        else: 
            return False
    
    def chekCorL(self, elem):
        """
        проверка левой границы
        """
        if elem > 20:
            return True
        else: 
            return False
    
    def hit(self):
        """
        проверка попадения
        """
        if init.tank == init.tank1:
            if abs(init.canvas_game.coords(init.tank2.obj)[0] - init.canvas_game.coords(self.ball)[0]) < 20 and\
               abs(init.canvas_game.coords(init.tank2.obj)[1] - init.canvas_game.coords(self.ball)[1]) < 20:
                   return True
        else:
            if abs(init.canvas_game.coords(init.tank1.obj)[0] - init.canvas_game.coords(self.ball)[0]) < 20 and\
               abs(init.canvas_game.coords(init.tank1.obj)[1] - init.canvas_game.coords(self.ball)[1]) < 20:
                   return True
        return False
    
    def stshoot(self, angle, x, y):
        """
        выстрел
        """
        if init.tank == init.tank1:
            init.canvas_game.move(self.ball, x + 30, y) 
        else:
            init.canvas_game.move(self.ball, x, y) 
        x_const_1 = x + 60
        x_const_2 = x - 60
        con = True
        self.__t = 0
        start_time = time.time()
        while con:
            if time.time() - start_time >= 0.06:
                if self.check_sky() and self.chekCorL(init.canvas_game.coords(self.ball)[0]) and\
                    self.chekCorR(init.canvas_game.coords(self.ball)[0]):
                    if init.tank == init.tank1:
                        part1 = (init.canvas_game.coords(self.ball)[0] - x_const_1) * m.tan(m.radians(angle))
                        part2 = const.g * (init.canvas_game.coords(self.ball)[0] - x_const_1)**2 / 2 / const.v**2 / m.cos(m.radians(angle))**2
                        cor_y = round((part1 - part2))
                        init.canvas_game.move(self.ball, const.v * m.cos(m.radians(angle)) * self.__t, cor_y)   
                        if self.hit():
                            init.tank2.life()
                    else:
                        part1 = (init.canvas_game.coords(self.ball)[0] - x_const_2) * m.tan(m.radians(angle))
                        part2 = const.g * (init.canvas_game.coords(self.ball)[0] - x_const_2)**2 / 2 / const.v**2 / m.cos(m.radians(angle))**2
                        cor_y = round((part1 - part2))
                        init.canvas_game.move(self.ball, -const.v * m.cos(m.radians(angle)) * self.__t, cor_y)
                        if self.hit():
                            init.tank1.life()
                    init.canvas_game.update()
                    self.__t += 0.3
                    start_time = time.time()
                else:
                    con = False    
        init.canvas_game.after(1000, self.start_pos)
        
    def start_pos(self):
        x__, y__ = init.canvas_game.coords(self.ball)
        init.canvas_game.move(self.ball, -x__, -y__)
            
