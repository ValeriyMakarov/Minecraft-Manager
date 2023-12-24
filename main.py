"""Minecraft Manager для управления содержимого папки .minecraft и его архивирования с использованием WinRAR.

Используй список имён, который можно посмотреть с помощью команды ls, для перемещения содержимого:
    mcmanager ls
    > gregtech , vanilla.
При помощи команды move и ключей, можно управлять содержимым папки:
    ---------------ключи----------------
    r = Remove        очистить папку от файлов майнкрафта
    a = remove All    очистить папку
    c = Copy to       скопировать содержимое
    s = Swap with     поменять
    p = Press to      сжать, архивировать

    1. mcmanager ps move name_from_list - архивирует содержимое папки и заменяет на содержимое name_from_list
    2. mcmanager cs move name_from_list - сохраняет содержимое папки и заменяет на содержимое name_from_list
    3. mcmanager ap move - архивирует содержимое папки и очищает её
    4. mcmanager rc move - сохраняет содержимое папки и очищает её от файлов майнкрафта
Добавить имя можно переместив файлы с помощью команды move и ключа 'c' или 'p', либо командой get из указанной папки:
    1. mcmanager p move new_name
    2. mcmanager get your_path new_name
"""
import shutil
import os
import sys
import time
import subprocess
import zipfile


r'"C:\Program Files\WinRAR\rar.exe" a C:\Users\Lenovo\Desktop\test1 C:\Users\Lenovo\Desktop\hello'
r'"C:\Program Files\Minecraft Manager"'
'''
Копирование папки с майном: mcmanager
1. Аргументы:   move    |   переместить
                    r = Remove очистить папку от файлов майнкрафта
                    a = remove All очистить папку
                    c = Copy скопировать содержимое
                    s = Swap with поменять
                    p = Press сжать, архивировать
                    path
                help    |   помощь
                ls      |   список архивов
                get     |   скопировать из указанного пути в папку, указав имя
             
    r a c p - что делать с текущей папкой
    s - обмен папок
    Press Copy взаимозаменяемы
    Remove remove All взаимозаменяемы
    Copy Swap взаимозаменяемы  
                
    mcmanager r move          |   удалить все файлы кроме лаунчера
    mcmanager a move          |   очистить всю папку
    mcmanager с move path name|   создать папку с именем и скопировать содержимое папки майнкрафта или скопировать в указанный "path"
    mcmanager s name     |   поменять папку майнкрафта с папкой по указанному name. Изначально должно содержаться в списке. Автоматически разархивирует
    mcmanager p move name     |   архивировать папку в стандартную папку или в указанный "path"
    
    mcmanager pa move path    |   сжать, скопировать файлы в указанный "path" и очистить папку
    mcmanager pr move path    |   сжать, скопировать файлы в указанный "path" и удалить файлы майнкрафта
    mcmanager ps move    |   сжать, поменять папку или архив майнкрафта с папкой по указанному "path". Автоматически разархивирует
    mcmanager ar move         |   r игнорируется и удаляется всё
    mcmanager ca move path name   |   создать папку с именем и скопировать содержимое папки майнкрафта или скопировать в указанный "path", очищается исходная папка
    mcmanager cr move path name   |   создать папку с именем и скопировать содержимое папки майнкрафта или скопировать в указанный "path", удаляются файлы майнкрафта
    mcmanager acprs move    вызывает ошибку

2. Должен иметься файл для хранения данных программы.
3. Загрузить в список имена
4. Проверка на наличие файлов
5. Убивать процесс с майнкрафтом для работы или проверить как работает команда с запущеным
6. Проверить что имя - это не путь
7. Хранить текущее имя, если его нет при свапе, запрашивать у пользователя
исходить из списка
'''
print(__doc__)
if __name__ != '__main__':
    files = sys.argv[1:]
    target = r'C:/Projects/trash/'
    print(files, target)
    if not os.path.exists(target):
        os.mkdir(target)
    for file in files:
        name = time.strftime('%Y_%m_%d_%H_%M_%S')
        res = shutil.make_archive(fr'{target}{os.sep}{name}', 'zip', root_dir=target, base_dir=file)

        command = r'Compress-Archive -Path "C:/Users/Lenovo/Desktop/Новая папка" -DestinationPath "C:/Users/Lenovo/Desktop/archive.zip"'
        subprocess.run(['powershell', '-Command', command], capture_output=True, text=True)
        print(f'Получилось создать архив {target}//{name}.zip из {file}.' if res else f'Не получилось создать архив {target}//{name}.zip из {file}.')