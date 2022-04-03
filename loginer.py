import pyautogui as pg
import time
import numpy as np
from mss import mss
import datetime
import keyboard

def loginerfunc():
    time.sleep(1)

    l3 = 1420  # координаты кнопки логин
    t3 = 900
    l4 = 1689 # координаты кнопки майн
    t4 = 441



    monitor3 = {
            "left": l3, # координаты кнопки логин
            "top": t3,
            "width": 1, # размер
            "height": 1,
    }

    monitor4 = {
            "left": l4, # координаты кнопки Mining Hub
            "top": t4,
            "width": 1, # размер
            "height": 1,
    }


    def find_color3(our_color3, monitor3={}):

        # проба цвета с координат
        m3 = mss()


        # получаем пиксель с монитора
        img3 = m3.grab(monitor3)

        # преобразуем пиксель в матрицу
        img_arr3 = np.array(img3)

        # поиск цвета (b, g, r alpha)
        our_map3 = (our_color3[2],our_color3[1],our_color3[0],255)
        indexes3 = np.where(np.all(img_arr3 == our_map3, axis=-1))
        our_crd3 = np.transpose(indexes3)
        return our_crd3

    def find_color4(our_color4, monitor4={}):

        # проба цвета с координат
        m4 = mss()


        # получаем пиксель с монитора
        img4 = m4.grab(monitor4)

        # преобразуем пиксель в матрицу
        img_arr4 = np.array(img4)

        # поиск цвета (b, g, r alpha)
        our_map4 = (our_color4[2],our_color4[1],our_color4[0],255)
        indexes4 = np.where(np.all(img_arr4 == our_map4, axis=-1))
        our_crd4 = np.transpose(indexes4)
        return our_crd4

    our_color3 = [0,60,112]     # синий цвет с кнопки
    our_color4 = [0,60,112]

    while True:

        time1 = time.time()
        result = find_color3(our_color3, monitor3)
        time2 = time.time()
        if result.__len__():
            x = result[0][1] + monitor3.get("left")
            y = result[0][0] + monitor3.get("top")
            pg.moveTo(x, y)  # перемещение мыши по координатам где найден цвет
            pg.click(x, y, interval=0.2)  # клик
            pg.moveTo(x+150, y+150)
            print('Нажал кнопку Login:', datetime.datetime.now())
        else:
            time1 = time.time()
            result = find_color4(our_color4, monitor4)
            time2 = time.time()
            if result.__len__():
                x = result[0][1] + monitor4.get("left")
                y = result[0][0] + monitor4.get("top")
                pg.moveTo(x, y)  # перемещение мыши по координатам где найден цвет
                pg.click(x, y, interval=0.2)  # клик
                pg.moveTo(x + 150, y + 150)
                print('Нажал кнопку Mine в меню игры:', datetime.datetime.now())
            else:
                time.sleep(1)






