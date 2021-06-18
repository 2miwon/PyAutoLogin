# for repl.it (online ide)

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
# speeding option
chrome_options.headless = True
chrome_options.add_argument("disable-gpu")
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# in repl.it
driver = webdriver.Chrome(options=chrome_options)


### setting
class Setting:
  def __init__(self):
    self.SiteList = "list.csv"
  
  def getSiteList(self):
    return self.SiteList
  def setSiteList(self, i):
    self.SiteList = i

BasicSet = Setting()

### interaction with HTML
def ElementFinder(tag):
  return tag[2:]

def ElementChecker(targetEle):
  if(targetEle[0] == 'n'): #name
    return driver.find_element_by_name(ElementFinder(targetEle))
  elif(targetEle[0] == 't'): #type
    return driver.find_element_by_type(ElementFinder(targetEle))
  elif(targetEle[0] == 'i'): #id
    return driver.find_element_by_id(ElementFinder(targetEle))

def ElementInputID(site):
  target = ElementChecker(site.E_ID)
  target.send_keys(site.ID)
  return True

def ElementInputPW(site):
  target = ElementChecker(site.E_PW)
  target.send_keys(site.PW)
  Enter(target)
  return True

def LogoutButton(site):
  target = ElementChecker(site.E_Logout)
  Click(target)
  return True

def Enter(target):
  target.send_keys(Keys.RETURN)

def Click(target):
  target.click()

### interaction with database(csv)
SiteDatabase = []

def ReadCSV(setting):
  return open(setting.getSiteList(),'r')

def ReadLineToList(line, spl):
  rawlist = line.split(spl)
  ConvertData(rawlist)

def ConvertData(rawlist):
  site = Site(rawlist[0], rawlist[1], rawlist[2], rawlist[3], rawlist[4], rawlist[5],rawlist[6][:-1])
  SiteDatabase.append(site)

### site information

class Site:
  def __init__(self, URL_Login, ID, PW, E_ID, E_PW, URL_Logout, E_Logout):
    self.URL_Login = URL_Login
    self.ID = ID
    self.PW = PW
    self.E_ID = E_ID
    self.E_PW = E_PW
    self.URL_Logout = URL_Logout
    self.E_Logout = E_Logout
  
  def MessageLoginURL(self):
    print("login :: target url: " + self.URL_Login)
  
  def MessageSuccessLogin(self):
    print("login :: successfully login "+ driver.current_url.split('/')[2])
    print("welcome to " + driver.title)

  def MessageFailureLogin(self):
    print("login :: error :: fail login")

  def MessageLogoutURL(self):
    print("logout :: target url: " + self.URL_Logout)
  
  def MessageSuccessLogout(self):
    print("logout:: successfully logout "+ driver.current_url.split('/')[2])

  def MessageFailureLogout(self):
    print("logout :: error :: fail logout")

  def Login(self):
    driver.get(self.URL_Login)
    print("login :: login...")
    if(ElementInputID(self) and ElementInputPW(self)): 
      self.MessageSuccessLogin()
    else:
      self.MessageFailureLogin()
      
  def Logout(self):
    driver.get(self.URL_Logout)
    print("logout :: logout...")
    if(LogoutButton(self)):
      self.MessageSuccessLogout()
    else:
      self.MessageFailureLogout()


### time controller



### log



### Module
def loginModule(site):
  site.MessageLoginURL()
  site.Login()
  
def logoutModule(site):
  site.MessageLogoutURL()
  site.Logout()

def ReadCSVModule():
  file = ReadCSV(BasicSet)
  line = file.readline()
  while(line):
    ReadLineToList(line, ',')
    line = file.readline()
  
myday = 0



### main
ReadCSVModule()
loginModule(SiteDatabase[0])
logoutModule(SiteDatabase[0])

"""
while(True):
  mytime = time.time()
  mytime += 60*60*9
  tm = time.localtime(mytime)
  if(myday == 0):
    myday = tm.tm_min
    print("boot:: time initializing... boot time: {0}/{1}/{2} {3}:{4}".format(tm.tm_year, tm.tm_mon, tm.tm_mday,'{:0>2}'.format(tm.tm_hour),'{:0>2}'.format(tm.tm_min)))
    continue
  else:
    if(myday != tm.tm_min):
      myday = tm.tm_min
      for url in mysites:
        start = time.time()
        loginModule(url)
        logoutModule(url)
        end = time.time()
        timestamp = end-start
        print("It took {0}second to access {1}".format('.1f'.format(timestamp),url[0].split('/')[2]))
  print("check... now time: {0}/{1}/{2} {3}:{4}".format(tm.tm_year, tm.tm_mon, tm.tm_mday,'{:0>2}'.format(tm.tm_hour),'{:0>2}'.format(tm.tm_min)))
  time.sleep(60*10)
    
  



#90일비밀번호기능
#로그인기록 남기기"""