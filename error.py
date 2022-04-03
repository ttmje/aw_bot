import pyautogui as pg
import time
import numpy as np
from mss import mss
import datetime


def errorcloser():
    pg.FAILSAFE = False
    time.sleep(0.2)
    l1 = 1418
    t1 = 442

    monitor1 = {
            "left": l1, # координаты красного пикселя
            "top": t1,
            "width": 200, # размер
            "height": 100,
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

    def find_color1(our_color1, monitor1={}):

        # проба цвета с координат
        m = mss()

        # получаем пиксель с монитора
        img = m.grab(monitor1)

        # преобразуем пиксель в матрицу
        img_arr = np.array(img)
        # поиск цвета (b, g, r alpha)
        our_map1 = (our_color1[2],our_color1[1],our_color1[0],255)
        indexes = np.where(np.all(img_arr == our_map1, axis=-1))
        our_crd = np.transpose(indexes)
        return our_crd

    our_color = [255,0,0]   # красный цвет с надписи error
    our_color1 = [217,3,7] #тоже красный, но другой
    while True:
        time1 = time.time()
        result = find_color(our_color, monitor1)
        time2 = time.time()
        if result.__len__():
            x = result[0][1]+monitor1.get("left")
            y = result[0][0]+monitor1.get("top")
            print('Нашел ошибку:', datetime.datetime.now())
            pg.moveTo(x+240,y-30) # перемещение мыши по координатам где крестик закрыть окно ошибки
            pg.click(x+240,y-30, interval=0.2)  # клик
            pg.moveTo(x, y)
            print('Закрыл ошибку:', datetime.datetime.now())
        else:
            time.sleep(1)

