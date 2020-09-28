"""
@author: koka
"""
import tkinter as tk
import const
from PIL import ImageTk, Image
import os
import classTank
import classCannon
import classBall
import fin

# Инициализация главного окна, размеры
root = tk.Tk()
root.title("TANKS")
w = root.winfo_screenwidth() // 2 - 400
h = root.winfo_screenheight() // 2 - 325
root.geometry('800x650+{}+{}'.format(w, h))

# подгрузка фото
background_image = ImageTk.PhotoImage(const.back)
tank1_img = ImageTk.PhotoImage(Image.open(os.path.join(const.img_folder, 'tank1-nocannon.png')))
tank2_img = ImageTk.PhotoImage(Image.open(os.path.join(const.img_folder, 'tank2-nocannon.png')))
cannon1_img = ImageTk.PhotoImage(Image.open(os.path.join(const.img_folder, 'tank1-cannon.png')))
cannon2_img = ImageTk.PhotoImage(Image.open(os.path.join(const.img_folder, 'tank2-cannon.png')))
ball_img = ImageTk.PhotoImage(Image.open(os.path.join(const.img_folder, 'ball.png')))

# Инициализация канвасов и отрисовка старта
canvas_start = tk.Canvas(root, width = const.WIDTH, height = const.HEIGHT, bg = "#80dfff", highlightthickness = 0)
canvas_game = tk.Canvas(root, width = const.WIDTH, height = const.HEIGHT, bg = "white" , highlightthickness = 0)
canvas_finish = tk.Canvas(root, width = const.WIDTH, height = const.HEIGHT, bg = "#80dfff")
canvas_start.pack()

# отрисовка изображений на канвас_гейм (включиться после дестроя канвас_старт)
background_image_object = canvas_game.create_image(0, 0, image = background_image, anchor = tk.NW)

# инициализация элементов на канвас_гейм
s1 = canvas_game.create_text(50, 50, text="3", justify = tk.LEFT,\
                       font = ("Times", "24", "bold italic"), fill = '#FF0000')
s2 = canvas_game.create_text(750, 50, text="3", justify = tk.LEFT,\
                       font = ("Times", "24", "bold italic"), fill = '#FF0000')

# создание объектов класса 
tank1 = classTank.Tank(tank1_img, 80, 100)
tank2 = classTank.Tank(tank2_img, 700, 100)
cannon1 = classCannon.Cannon(cannon1_img, 80, 86)
cannon2 = classCannon.Cannon(cannon2_img, 700, 86)
ball = classBall.Ball(ball_img, 0, 0)

# инициализация доп кнопок и элементов на канвас_старт
button_start = tk.Button(canvas_start, text = 'START', width = 14, height = 4,\
                         bg = '#ff8080', fg = 'white', command = fin.start)
canvas_start.create_text(150, 20, text="Клавиши вверх-вниз, влево-вправо и пробел", justify = tk.LEFT,\
                       font = ("Times", "12", "italic"), fill = '#0000ff')

# инициализация доп кнопок и элементов на канвас_финиш
button_finish = tk.Button(canvas_finish, text = 'PLAY AGAIN', width = 14,\
                height = 4, bg = '#ff8080', fg = 'white', command = fin.play_again)
   
# отрисовка на старт и финиш канвасах объектов типо текста и кнопок  
button_start.pack()
button_start.place(x = 360, y = 280)  
#button_finish.pack()
#button_finish.place(x = 360, y = 400)

# переменные для смены хода (вынести в конст)
tank = tank1
cannon = cannon1
