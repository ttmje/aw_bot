import Bot, selector, Capcha_deny, Crutch, error, loginer
from threading import Thread
from datetime import datetime

now = datetime.now().strftime("%d/%m/%y %I:%M:%S")
print("Начало работы бота: ", now)

if __name__ == '__main__':
    captcha_deny1 = Thread(target=Capcha_deny.captcha_deny, args=())
    captcha_deny1.start()

    crutch1 = Thread(target=Crutch.crutch, args=())
    crutch1.start()

    login = Thread(target=loginer.loginerfunc, args=())
    login.start()

    error_closer = Thread(target=error.errorcloser, args=())
    error_closer.start()

    bot = Thread(target=Bot.botmain, args=[Bot.ts1])
    bot.start()

    selector = Thread(target=selector.group1(selector.st1, selector.sleep))
    selector.start()









