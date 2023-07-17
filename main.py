# for repl.it (online ide)

from Worker import *
#from pynput import keyboard
from SeleniumAction import *
import json
from OutputController import *

with open('account.json') as f:
    account = json.load(f)


#import pymysql as mysql
#import sqlite3 as sql

#DB.MakeTable("test","x text")
#DB.ReadTable("test")

### main
"""
def on_press(key):
  if key == keyboard.Key.esc:
    exit()
  elif key == 'r':
    print('sex')
    RMode()
  elif key == 'c':
    CMode()
  elif key == 'l':
    ClearLog()

def on_release(key):
  if key == Key.esc:
    exit()
  elif key == 'r':
    RMode()
  elif key == 'c':
    CMode()
  elif key == 'l':
    ClearLog()

with keyboard.Listener(
    on_press=on_press,
    on_release=on_release) as listener:
    listener.join()
"""


def RMode():
  Booting()
  Processing()
  ShutDown(filelist)


def CMode():
  Booting()
  while True:
    command = input("in :: ")
    if command == '':
      break
    else:
      Console(command)
  ShutDown(filelist)


def ClearLog():
  log = open("log.txt", 'w')
  log.close()


def DebugMode():
  pass


print("""
    Welcome to MyViser!! last update 2021-12-12 ver 1.10 \n
    R: Routine Mode 
    C: Console Mode 
    L: Clear Log File 
    E: Exit Program
    """)
com = input()

if com == 'r' or com == 'R':
  RMode()
elif com == 'c' or com == 'C':
  CMode()
elif com == 'L' or com == 'l':
  ClearLog()
elif com == 'e' or com == 'E':
  exit()