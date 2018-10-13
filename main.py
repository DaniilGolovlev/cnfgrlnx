""" Даниил Головлев ( daniil.golovlev@yandex.ru )
Эти скрипты писались для личных нужд. Они не предназначены для использования кем либо еще.
Если к Вам попали эти скрипты - не вздумайте их использовать!!!!

Скрипты для конфигурирования серверов и рабочих станций Linux"""

import platform


def systemInformation():
    """ Сбор основной информации о системе """
    print("Сбор информации о системе...")

    OSDistr = platform.dist()
    ArchOS = platform.architecture()

    print("ОС:", OSDistr[0], OSDistr[1], "\n" + "Архитектура:", ArchOS[0])


if __name__ == "__main__":
    if platform.system() != "Linux":
        print("Только для Linux")
    else:
        systemInformation()
