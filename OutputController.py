from SeleniumSetting import *
from TimeController import *
import time
import IO_txt as TXT

def GetURLShort():
  return driver.current_url.split('/')[2]
def GetURLFull():
  return driver.current_url

# Console Control
def MessageGetPage():
  print("page :: target url: " + GetURLShort())
def MessageSuccessLogin():
  print("login :: successfully login "+ GetURLShort())
  print("welcome to " + driver.title)
def MessageFailureLogin():
  print("error :: fail login")
def MessageClick(text):
  print("action :: click", text)
def MessageSuccessLogout():
  print("logout :: successfully logout "+ GetURLShort())
def MessageFailureLogout():
  print("error :: fail logout")
def MessagePassCheck():
  print("check :: pass checking")
def MessageSkipChangePW():
  print("check :: invalid url... skip change pw")
def MessagePoint(po):
  print("text :: your point =", po)
def MessageTimeOut():
  print("error :: time out")
def MessageNowTime():
  print("check :: now time: " + GetNowTime())
def MessageBoot():
  print("boot :: time initializing... boot time: " + GetNowTime())
def MessageRemoveDuplication(URL):
  print("Process :: " + URL + " already accessed today")
def MessageSleep(t):
  print("System :: sleep " + t + " seconds")
# Log Control
def OutputEnter(file):
  file.write("\n")

def RecordBoot(file):
  file.write("Boot : " + GetNowTime())
  OutputEnter(file)
def RecordLogin(file):
  file.write("Login : " + GetURLShort() + " / " + GetNowTime())
  OutputEnter(file)
def RecordLogout(file):
  file.write("Logout : " + GetURLShort() + " / " + GetNowTime())
  OutputEnter(file)
def RecordPoint(file, URL, p):
  file.write("{0} {1} = {2} ".format(
    GetNowDay(),
    URL,
    p
  ))
  #if (inc):
  #  file.write("({:+d})".format(inc))
  OutputEnter(file)
def RecordStamp(file):
  file.write(GetNowDay())
  OutputEnter(file)
# Stamp Control
def Stamp(file):
  pass
