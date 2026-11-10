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

time.sleep(0)
print(result.stdout)

disk_names = [disk.device for disk in psutil.disk_partitions(all=True)]
disks_text = ", ".join(disk_names)

print("напиши C чтоб на ссд для системи или D чтоб установить на сторонний",)

quess = input("Выбери").strip().upper()


disk_names = [disk.device for disk in psutil.disk_partitions(all=True)]
if quess == disk_names:
    print("Ви устанавливаете на системный диск", disk_names)
else:
    disk = quess + ":\\"

if quess + ":\\" not in disk_names:
    print("ми не смогли найти такой диск на вашем устройстве")
    sys.exit()

print("Вы устанавливаете на диск", disk)

print("Вставь код игры сюда.")
print("После вставки напиши END на новой строке.")

lines = []

while True:
    line = input()
    if line == "END":
        break
    lines.append(line)

game_code = "\n".join(lines)

install_folder = os.path.join(disk, "snake")
os.makedirs(install_folder, exist_ok=True)

new_path = os.path.join(install_folder, "game.py")

with open(new_path, "w", encoding="utf-8") as f:
    f.write(game_code)

print("Установка завершена! Игра сохранена!")
print("Файл:", new_path)
print("Размер файла:", os.path.getsize(new_path), "байт")
