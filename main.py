#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Даниил Головлев ( daniil.golovlev@yandex.ru )
Эти скрипты писались для личных нужд. Они не предназначены для использования кем либо еще.
Если к Вам попали эти скрипты - не вздумайте их использовать!!!!

Скрипты для конфигурирования серверов и рабочих станций Linux"""

from platform import dist, system

def select_script():
    """ Выбор скрипта настройки """

    os_distr = dist()

    if os_distr == "debian":
        import OS.cnfgr_debian
    elif os_distr == "centos":
        import OS.cnfgr_centos
    elif os_distr == "fedora":
        import OS.cnfgr_fedora
    elif os_distr == "ubuntu":
        import OS.cnfgr_ubuntu


if __name__ == "__main__":

    if system() != "Linux":
        print("Только для Linux")
    else:
        select_script()
