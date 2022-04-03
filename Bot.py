import pyautogui as pg
import time
import numpy as np
from mss import mss
import datetime

def botmain(ts1):
    l1 = 1397
    t1 = 775
    l2 = 1315
    t2 = 630
    l3 = 215
    t3 = 600
    l4 = 1145
    t4 = 740

    monitor1 = {
            "left": l1, # координаты кнопки Майн
            "top": t1,
            "width": 1, # размер
            "height": 1,
    }

    monitor2 = {
            "left": l2, # координаты кнопки Клэйм
            "top": t2,
            "width": 1, # размер
            "height": 1,
    }

    monitor3 = {
            "left": l3, # координаты кнопки Апрув
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

    monitor5 = {
            "left": l3, # координаты кнопки Апрув в сером цвете
            "top": t3,
            "width": 1, # размер
            "height": 1,
    }

    # поиск цвета на экране
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

    def find_color2(our_color2, monitor2={}):

        # проба цвета с координат
        m2 = mss()


        # получаем пиксель с монитора
        img2 = m2.grab(monitor2)

        # преобразуем пиксель в матрицу
        img_arr2 = np.array(img2)

        # поиск цвета (b, g, r alpha)
        our_map2 = (our_color2[2],our_color2[1],our_color2[0],255)
        indexes2 = np.where(np.all(img_arr2 == our_map2, axis=-1))
        our_crd2 = np.transpose(indexes2)
        return our_crd2

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

    def find_color5(our_color5, monitor5={}):

        # проба цвета с координат
        m5 = mss()


        # получаем пиксель с монитора
        img5 = m5.grab(monitor5)

        # преобразуем пиксель в матрицу
        img_arr5 = np.array(img5)

        # поиск цвета (b, g, r alpha)
        our_map5 = (our_color5[2],our_color5[1],our_color5[0],255)
        indexes5 = np.where(np.all(img_arr5 == our_map5, axis=-1))
        our_crd5 = np.transpose(indexes5)
        return our_crd5

    # искомый цвет
    our_color = [0,60,112]
    our_color2 = [0,60,112]
    our_color3 = [255,119,74]
    our_color4 = [0,60,112]
    our_color5 = [209,101,67]

    while True: # начинается с обработки кнопки Майн
        time1 = time.time()
        result = find_color(our_color, monitor1)
        time2 = time.time()
        if result.__len__():
            x = result[0][1]+monitor1.get("left")
            y = result[0][0]+monitor1.get("top")
            pg.moveTo(x,y) # перемещение мыши по координатам где найден цвет
            pg.click(x, y, interval=0.2)  # клик
            pg.moveTo(x+150, y+150)
            print('Нажал кнопку Майн:', datetime.datetime.now())
        else: # отсюда обработка кнопки Клэйм
            time.sleep(0.1)

            time.sleep(0.1)

            time1 = time.time()
            result = find_color2(our_color2, monitor2)
            time2 = time.time()
            if result.__len__():
                x = result[0][1] + monitor2.get("left")
                y = result[0][0] + monitor2.get("top")
                time.sleep(0.1)
                pg.moveTo(x, y)  # перемещение мыши по координатам где найден цвет
                pg.click(x, y, interval=0.2)  # клик
                pg.moveTo(x+150, y+150)
                time.sleep(0.1)     # защита от двойного нажатия
                print('Нажал кнопку Клэйм:', datetime.datetime.now())
            else: # отсюда обработка кнопки Апрув
                time.sleep(0.1)

                time1 = time.time()
                result = find_color3(our_color3, monitor3)
                time2 = time.time()
                if result.__len__():
                    x = result[0][1] + monitor3.get("left")
                    y = result[0][0] + monitor3.get("top")
                    time.sleep(0.1)
                    pg.moveTo(x, y)  # перемещение мыши по координатам где найден цвет
                    pg.click(x, y, interval=0.2)  # клик


                    print('Нажал кнопку Апрув:', datetime.datetime.now())

                else: # отсюда обработка зависнувшей кнопки Апрув
                    time.sleep(0.1)

                    time1 = time.time()
                    result = find_color5(our_color5, monitor5)
                    time2 = time.time()

                    if result.__len__():
                        time.sleep(ts1)
                        pg.moveTo(x, y)
                        x = result[0][1] + monitor5.get("left")
                        y = result[0][0] + monitor5.get("top")
                        time.sleep(1)
                        pg.moveTo(x+73, y+72)  # перемещение мыши по координатам где найден цвет
                        pg.click(x+73, y+72, interval=0.2)  # клик
                        pg.moveTo(x+150, y+150)
                        print('Нажал кнопку Deny:', datetime.datetime.now())

                    else: # отсюда обработка кнопки Майнинг хаб
                        time.sleep(0.2)

                        time1 = time.time()
                        result = find_color4(our_color4, monitor4)
                        time2 = time.time()
                        if result.__len__():
                            x = result[0][1] + monitor4.get("left")
                            y = result[0][0] + monitor4.get("top")
                            pg.moveTo(x, y)  # перемещение мыши по координатам где найден цвет
                            pg.click(x, y, interval=0.2)  # клик
                            pg.moveTo(x+150, y+150)
                            print('Нажал кнопку Майнинг хаб:', datetime.datetime.now())
                        else:
                            time.sleep(0.1)
