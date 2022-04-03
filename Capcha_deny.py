import pyautogui as pg
import time
import numpy as np
from mss import mss
import datetime
import keyboard

def captcha_deny():
    time.sleep(0.2)

    l1 = 192 #input("Введите место пикселя NO x: ")
    #try:
        #l1 = int(l1)
        #print("Введенная координата Х ", l1)
    #except ValueError:
        #l1 = 800
        #print("Ставлю по умолчанию:", l1)

    t1 = 585 #input("Введите место пикселя NO y: ")
    #try:
        #t1 = int(t1)
        #print("Введенная координата У : ", t1)
    #except ValueError:
        #t1 = 300
        #print("Ставлю по умолчанию:", t1)

    monitor1 = {
            "left": l1, # координаты белого пикселя
            "top": t1,
            "width": 5, # размер
            "height": 5,
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

    our_color = [255,255,255]   # белый цвет с надписи нет слота

    while True:
        time1 = time.time()
        result = find_color(our_color, monitor1)
        time2 = time.time()
        if result.__len__():
            x = result[0][1]+monitor1.get("left")
            y = result[0][0]+monitor1.get("top")
            print('Нашел ошибку:', datetime.datetime.now())
            pg.moveTo(297,783) # перемещение мыши по координатам кнопки Денай
            pg.click(297,783, interval=0.2)  # клик
            pg.moveTo(297+100, 783+100)
            time.sleep(1)
            print('Закрыл ошибку:', datetime.datetime.now())
        else:
            time.sleep(1)