# Работа с архиватором ZIP

import os
from zipfile import ZipFile


# Архивирование папок с файлами и вложенными папками в ZIP

def zip(path, zpath):
    zfile = ZipFile(zpath, "w")
    if os.path.isfile(path):
        zfile.write(path)
    else:
        for root, dirs, files in os.walk(path):
            for file in files:
                zfile.write(root + "/" + file)

    zfile.close()


# Разархивирование папок с файлами и вложенными папками в ZIP

def unzip(path, zpath):
    zfile = ZipFile(zpath, "r")
    for name in zfile.namelist():
        dir, file = os.path.split(name)
        if not os.path.exists(path + "/" + dir):
            os.mkdir(path + "/" + dir)
        if file:
            handler = open(path + "/" + name, "wb")
            handler.write(zfile.read(name))
            handler.close()
    zfile.close()


zip("images", "my.zip")
unzip("abc", "my.zip")
