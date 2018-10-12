#!/bim/env python3
"""""
Даниил Головлев ( daniil.golovlev@yandex.ru )

Эти скрипты писались для личных нужд. Они не предназначены для использования кем либо еще.
Если к Вам попали эти скрипты - не вздумайте их использовать!!!! """

"""
Скрипты для конфигурирования серверов и рабочих станций Linux"""

import platform

def SystemInformation():
    """ Сбор основной информации о системе """
    print("Сбор информации о системе...")

    OS = platform.dist()
    ARCH = platform.architecture()

    print("ОС:", OS[0], OS[1], "\n"+"Архитектура:", ARCH[0])

if __name__ == "__main__" :
    if platform.system() != "Linux":
        print("Только для Linux")
    else:        
        SystemInformation()
