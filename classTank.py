"""
@author: koka
"""
import const
import init
import tkinter as tk
import fin

class Tank():
    def __init__(self, obj_img, x, y):
        """
        объект типо танк, его изображение, проверка неба, жизни
        """
        self.obj = init.canvas_game.create_image(x, y, image = obj_img, anchor = tk.NW)
        self.chek_sky(False)
        self.__lifes = 3
    
    def moveR(self, cannon = False):
        """
        метод движения вправо
        """
        if init.canvas_game.coords(self.obj)[0] + 30 > const.WIDTH:
            init.canvas_game.move(self.obj, -10, 0)
        elif init.canvas_game.coords(self.obj)[0] < 0:
            init.canvas_game.move(self.obj, 10, 0)
        else:
            init.canvas_game.move(self.obj, 3, 0)              
            self.chek_sky(cannon)
        
    def moveL(self, cannon = False):
        """
        метод движения влево
        """
        if init.canvas_game.coords(self.obj)[0] + 30 > const.WIDTH:
            init.canvas_game.move(self.obj, -10, 0)
        elif init.canvas_game.coords(self.obj)[0] < 0:
            init.canvas_game.move(self.obj, 10, 0)
        else:
            init.canvas_game.move(self.obj, -3, 0)             
            self.chek_sky(cannon)
                
    def chek_sky(self, cannon):
        """
        проверка того где сейчас танк
        """
        con = True
        while con:
            sky_color = const.back.getpixel((init.canvas_game.coords(self.obj)[0],\
                                              init.canvas_game.coords(self.obj)[1]))
            if sky_color == const.SKY:
                init.canvas_game.move(self.obj, 0, 1)
            elif cannon == True and sky_color == const.DIRT:
                init.canvas_game.move(self.obj, 0, -28)
                con = False
            elif sky_color == const.DIRT:
                init.canvas_game.move(self.obj, 0, -15)
                con = False
                
    def life(self):
        """
        проверка жизней при попадение
        """
        if self.__lifes - 1 >= 1:
            self.__lifes -= 1
            if init.tank == init.tank1:
                init.canvas_game.itemconfig(init.s2, text = self.__lifes)
            else:
                init.canvas_game.itemconfig(init.s1, text = self.__lifes)
        else:
            if init.tank == init.tank1:
                fin.finish("ПОБЕДИЛ ПЕРВЫЙ ИГРОК!!!!!")
            else:
                fin.finish("ПОБЕДИЛ ВТОРОЙ ИГРОК!!!!!")