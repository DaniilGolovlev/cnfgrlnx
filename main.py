#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Даниил Головлев ( daniil.golovlev@yandex.ru )
Эти скрипты писались для личных нужд. Они не предназначены для использования кем либо еще.
Если к Вам попали эти скрипты - не вздумайте их использовать!!!!

Скрипты для конфигурирования серверов и рабочих станций Linux"""

import platform


def system_information():
    """ Сбор основной информации о системе """
    print("Сбор информации о системе...")

    os_distr = platform.dist()
    os_arch = platform.architecture()

    print("ОС:", os_distr[0], os_distr[1], "\n" + "Архитектура:", os_arch[0])


if __name__ == "__main__":
    if platform.system() != "Linux":
        print("Только для Linux")
    else:
        system_information()
