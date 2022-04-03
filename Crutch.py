import pyautogui as pg
import time
import numpy as np
from mss import mss
import datetime
import keyboard


def crutch():
    time.sleep(0.2)

    CX = 1791
    CY = 341

    monitor1 = {
            "left": CX, # координаты синего пикселя Х
            "top": CY,
            "width": 1, # размер
            "height": 1,
    }

    def find_color(our_color, monitor1={}):

        # проба цвета с координат
        m = mss()


        # получаем пиксель с монитора
        img = m.grab(monitor1)

        # преобразуем пиксель в матрицу
        img_arr = np.array(img)

        # поиск цвета (b, g, r alpha)
        our_map = (our_color[2],our_color[1],our_color[0],255)
        indexes = np.where(np.all(img_arr == our_map, axis=-1))
        our_crd = np.transpose(indexes)
        return our_crd

    our_color = [41,125,231]   # синий цвет с надписи Х

    while True:
        time1 = time.time()
        result = find_color(our_color, monitor1)
        time2 = time.time()
        if result.__len__():
            x = result[0][1]+monitor1.get("left")
            y = result[0][0]+monitor1.get("top")
            print('Нашел ошибку:', datetime.datetime.now())
            pg.moveTo(x,y) # перемещение мыши по координатам где крестик закрыть окно ошибки
            pg.click(x,y, interval=0.2)  # клик
            pg.moveTo(x+100, y+100)
            print('Закрыл ошибку:', datetime.datetime.now())
        else:
            time.sleep(1)