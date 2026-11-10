import time
import random
import os
import psutil
import subprocess
import shutil
import sys
import tkinter as tk

print("вибери куда установить")

cmd = 'powershell "Get-PhysicalDisk | Select-Object FriendlyName, MediaType, OperationalStatus, Size | Format-Table -AutoSize"'
result = subprocess.run(cmd, capture_output=True, text=True, shell=True)

time.sleep(1)
print(result.stdout)

disk_names = [disk.device for disk in psutil.disk_partitions(all=True)]
disks_text = ", ".join(disk_names)

print("напиши C чтоб на ссд для системи или D чтоб установить на сторонний", disk_names)

quess = input("Выбери C или D: ").strip().upper()

if quess == "C":
    disk = "C:\\"
    print("Ви устанавливаете на системный диск", disk)

elif quess == "D":
    disk = "D:\\"
    print("ви установили сторонний диск", disk)

else:
    print("Неверный выбор диска!")
    sys.exit()

if disk not in disk_names:
    print("Такого диска нет!")
    sys.exit()

print("Вставь код игры сюда.")
print("После вставки напиши END на новой строке.")

lines = []

while True:
    line = input()
    if line == "END":
        break
    lines.append(line)

game_code = "\n".join(lines)

install_folder = os.path.join(disk, "Snake")
os.makedirs(install_folder, exist_ok=True)

new_path = os.path.join(install_folder, "game.py")

with open(new_path, "w", encoding="utf-8") as f:
    f.write(game_code)

print("Установка завершена! Игра сохранена!")
print("Файл:", new_path)
print("Размер файла:", os.path.getsize(new_path), "байт")
