#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Даниил Головлев ( daniil.golovlev@yandex.ru )
Эти скрипты писались для личных нужд. Они не предназначены для использования кем либо еще.
Если к Вам попали эти скрипты - не вздумайте их использовать, это может привести к потере важной информации
и/или неработоспособности системы/программ!!!!

These scripts were designed for personal use. They are not intended to be used by anyone else.
If these scripts come to you - do not try to use them, this may lead to the loss of important information
and / or inoperability of the system / programs !!!!
Sorry for my english =)

Скрипты для конфигурирования серверов и рабочих станций Linux"""

from platform import dist


os_distr = dist()

supported_operating_systems = ("debian", "centos", "ubuntu", "fedora")


def select_script():
    """ Выбор скрипта настройки """

    if os_distr[0] == "debian":
        import OS.cnfgr_debian
    elif os_distr[0] == "centos":
        import OS.cnfgr_centos
    elif os_distr[0] == "fedora":
        import OS.cnfgr_fedora
    elif os_distr[0] == 'ubuntu':
        import OS.cnfgr_ubuntu


if __name__ == "__main__":
    if os_distr[0] not in supported_operating_systems:
        print("Эта ОС или дистрибьютив не поддерживается")
    else:
        select_script()
