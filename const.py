"""
@author: koka
"""
import os
from PIL import Image
WIDTH = 800
HEIGHT = 650
g = 7
v = 100
DIRT = (185, 122, 87)
SKY = (153, 217, 234)
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
back = Image.open(os.path.join(img_folder, 'back.png'))