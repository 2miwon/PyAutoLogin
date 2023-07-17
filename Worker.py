from queue import Queue
import os

from SeleniumAction import *
from OutputController import *


### scheduler -> FIFO
queue = Queue()
def inQueue(a):
  queue.put(a)
  return True
def outQueue():
  return queue.get()

def Sleep():
  time.sleep(timeSleep)

def Interpreter(com, pram):
  try:  
    if com == "PAGE":
      GetPage(pram[0])
      MessageGetPage()
    elif com == "CURSOR":
      Cursor(pram[0])
    elif com == "CLICK":
      Sleep()
      MessageClick(ClickButton(pram[0]))
    elif com == "TEXT":
      text = GetText(pram[0])
      #inc = ''
      #if isVarExist('Tstack'):
      #  inc = CalculateIncrease()
      MessagePoint(text)
      RecordPoint(filelist[2], GetURLShort(), text)
    elif com == "SLEEP":
      MessageSleep(pram[0])
      time.sleep(float(pram[0]))
    elif com == "LOGIN":
      if Login(pram[0], pram[1], pram[2], pram[3]):
        RecordLogin(filelist[1])
        Sleep()
        MessageSuccessLogin()
      else:
        MessageFailureLogin()
    elif com == "CHECK":
      if CheckPage(pram[0], pram[1]):
        MessagePassCheck()
      else:
        MessageSkipChangePW()
    elif com == "START":
      if CheckAttendance(pram[0]):
        while process[0] != "END":
          if process[0] == "TEXT":
            RecordPoint(filelist[2], pram[0], point[pram[0]])
          process = outQueue()
        MessageRemoveDuplication(pram[0])
    elif com == "END":
      MessageSuccessLogout()
    elif com == "INPUT":
      if ElementInput(pram[0], pram[1]):
        pass
    elif com == "ENTER":
      if ElementEnter(pram[0]):
        document.send_keys(Keys.RETURN)       
    else:
      pass
    return True
  except TimeoutException:
    MessageTimeOut()
  except:
    pass
  finally: 
    return False

def Launcher():
  process = outQueue()
  command = process[0]
  prameter = 0
  if len(process) != 1:
    prameter = process[1]
  Interpreter(command, prameter)

def Console(inp):
  tlist = inp.split(' ')
  plist = tlist[1:]
  Interpreter(tlist[0], plist)

def txtTOqueue(file):
  f = TXT.ReadFile("process.txt")
  for line in f:
    if line == None:
      break
    inQueue(TXT.txtTOtuple(line))
  f.close()

def Processing():
  while not queue.empty():
    if not Launcher():
        continue

def ShutDown(filelist):
  driver.quit()
  for f in filelist:
    f.close()

def Booting():
  filelist.append(TXT.ReadFile("process.txt"))
  filelist.append(TXT.AddFile("log.txt"))
  if not TXT.isEmptyFile("dashboard.txt"):
    LinetoDict(TXT.ReadFile("dashboard.txt"))
  filelist.append(TXT.WriteFile("dashboard.txt"))

  txtTOqueue(filelist[0])
  MessageBoot()
  RecordBoot(filelist[1])

def CalculateIncrease(file, flo):
  for l in range(1,len(Tstack)):
    temp = Tstack[l].split(' ')
    print(float(temp[2]) - flo)
  return float(temp[2]) - flo

def isVarExist(var):
  return (var in locals()) or (var in globals())

def isVarExistIn(var, container):
  return var in container

def LinetoDict(file):
  Tstack = file.readlines()
  global stamp
  stamp = dict()
  global point
  point = dict()
  for l in Tstack:
    stamp[l.split(' ')[1]] = l.split(' ')[0]
    point[l.split(' ')[1]] = l.split(' ')[3]

def CheckAttendance(sn):
  if isVarExistIn(sn ,stamp):
    if GetNowDay() == stamp[sn]:
      return True
  return False
  