import time
from datetime import datetime
import keyboard
# задаем время сна на окне
sleep = input("Введите ВРЕМЯ переключения столов (по умолчанию 16): ")
try:
    sleep = int(sleep)
    print("Время переключения: ", sleep)
except ValueError:
    sleep = 16
    print("Ставлю колличество по умолчанию:", sleep)

# задать количество столов
st1 = input("Введите колличество столов, кратно 4 (по умолчанию 24): ")
try:
    st1 = int(st1)
    print("Колличество столов: ", st1)
except ValueError:
    st1 = 24
    print("Ставлю колличество по умолчанию:", st1)

st0 = st1
#кнопки
next = "Ctrl + windows + right"
prev = "Ctrl + windows + left"
a = int(st1/4)

def group1(st1, sleep):
    while True:
        for i in range(a):
            for i in range(3):
                time.sleep(sleep)
                st1 = st1 - (st1 - 3)
                while st1 > 0:
                    keyboard.press_and_release(next)
                    print("Переключил на следующий стол в группе: ", datetime.now().strftime("%d/%m/%y %I:%M:%S"))
                    time.sleep(sleep)
                    st1 -= 1
                else:
                    for i in range(3):
                        keyboard.press_and_release(prev)
                print("Вернулся на первый стол в группе: ", datetime.now().strftime("%d/%m/%y %I:%M:%S"))
            else:
                for i in range(4):
                     keyboard.press_and_release(next)
                print("Переключил на первый стол в новой группе: ", datetime.now().strftime("%d/%m/%y %I:%M:%S"))
        else:
            for i in range(11):
                keyboard.press_and_release(prev)
            print("ЗАКОНЧИЛ ЦИКЛ И ВЕРНУЛСЯ НА САМОЕ ПЕРВОЕ ОКНО")


