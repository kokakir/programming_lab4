"""
@author: koka
"""
import const
import init
import classTank
import os
from PIL import ImageTk, Image


class Cannon(classTank.Tank):
    def __init__(self, cannon_img, x, y):
        """
        все тоже что есть в прародители, угол, вызов проверки неба, изображение
        """
        super().__init__(cannon_img, x, y)
        self.angle = 0
        self.chek_sky(True)
        self.__can_img = 0
        
    def movementD(self, can):
        """
        движение вверх
        """
        self.angle = 0
        if can == 1:
            p = ImageTk.PhotoImage(Image.open(os.path.join(const.img_folder, 'tank1-cannon.png')))
        else:
            p = ImageTk.PhotoImage(Image.open(os.path.join(const.img_folder, 'tank2-cannon.png')))
        init.canvas_game.itemconfig(self.obj, image = p)
        self.obj.update()
        init.canvas_game.update()
            
                
    def movementU(self, can):
        """
        движение вниз
        """
        if can == 1:
            if self.angle >= 60:
                pass
            else:
                self.angle = self.angle + 10
                self.__can_img = Image.open(os.path.join(const.img_folder, 'tank1-cannon.png'))
                img = self.__can_img.rotate(self.angle)
                img.save('tank1-cannon_.png')
                p = ImageTk.PhotoImage(Image.open(os.path.join(const.game_folder, 'tank1-cannon_.png')))
                init.canvas_game.itemconfig(self.obj, image = p)
                self.obj.update()
                init.canvas_game.update()
        else:
            if self.angle <= -80:
                pass
            else:
                self.angle = self.angle - 10
                self.__can_img = Image.open(os.path.join(const.img_folder, 'tank2-cannon.png'))
                img = self.__can_img.rotate(self.angle)
                img.save('tank2-cannon_.png')
                p = ImageTk.PhotoImage(Image.open(os.path.join(const.game_folder, 'tank2-cannon_.png')))
                init.canvas_game.itemconfig(self.obj, image = p)
                self.obj.update()
                init.canvas_game.update()
            
            

