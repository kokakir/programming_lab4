"""
@author: koka
"""
import init
import os
from PIL import ImageTk, Image
import const
        
def space():
    """
    обновление объкутов Пушка, установка изначального изображения
    """
    init.cannon1.angle = 0
    init.cannon2.angle = 0
    p1 = ImageTk.PhotoImage(Image.open(os.path.join(const.img_folder, 'tank1-cannon.png')))
    p2 = ImageTk.PhotoImage(Image.open(os.path.join(const.img_folder, 'tank2-cannon.png')))
    init.canvas_game.itemconfig(init.cannon1.obj, image = p1)
    init.canvas_game.itemconfig(init.cannon2.obj, image = p2)
    init.cannon1.obj.update()
    init.cannon2.obj.update()
    
def change(event):
    """
    Смена хода игравков и выстрел игрока который походил
    """
    if init.tank == init.tank1:
        init.ball.stshoot(init.cannon1.angle, init.canvas_game.coords(init.tank1.obj)[0], init.canvas_game.coords(init.tank1.obj)[1])
        init.tank = init.tank2
        init.cannon = init.cannon2
    else:
        init.ball.stshoot(init.cannon2.angle, init.canvas_game.coords(init.tank2.obj)[0], init.canvas_game.coords(init.tank2.obj)[1])
        init.tank = init.tank1
        init.cannon = init.cannon1
    space()
        
def moveLeft(event):
    """
    Ловим ивент левой кнопки и в зависимрсти от того чей ход вызываем метод движения
    """
    if init.tank == init.tank1:
        init.tank1.moveL()
        init.cannon1.moveL(True)
    else:
        init.tank2.moveL()
        init.cannon2.moveL(True)
        
def moveRight(event):
    """
    Ловим ивент правой кнопки и в зависимрсти от того чей ход вызываем метод движения
    """
    if init.tank == init.tank1:
        init.tank1.moveR()
        init.cannon1.moveR(True)
    else:
        init.tank2.moveR()
        init.cannon2.moveR(True)
        
def moveUp(event):
    """
    Ловим ивент верхней кнопки и в зависимрсти от того чей ход вызываем метод движения пушки
    """
    if init.cannon == init.cannon1:
        init.cannon1.movementU(1)
    else:
        init.cannon2.movementU(2)
        
def moveDown(event):
    """
    Ловим ивент нижней кнопки и в зависимрсти от того чей ход вызываем метод движения пушки
    """
    if init.cannon == init.cannon1:
        init.cannon1.movementD(1)
    else:
        init.cannon2.movementD(2)
