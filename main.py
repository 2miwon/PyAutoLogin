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

mylist = open("list.csv",'r')
mysites = []
myline = mylist.readline()
while(myline):
  newlist = myline.split(',')
  newlist[6] = newlist[6][:-1]
  mysites.append(newlist);
  myline = mylist.readline()

def loginModule(url):
  print("login:: target url: " + url[0])
  driver.get(url[0])
  print("login:: login...")
  for i in range(3, 5):
    if(url[i][0] == 'n'):
      elem = driver.find_element_by_name(url[i][2:])
    elif(url[i][0] == 't'):
      elem = driver.find_element_by_type(url[i][2:])
    elif(url[i][0] == 'i'):
      elem = driver.find_element_by_id(url[i][2:])

    if(i == 3):
      elem.send_keys(url[1])
    elif(i == 4):
      elem.send_keys(url[2])
      elem.send_keys(Keys.RETURN)
  
  print("login:: successfully login "+ driver.current_url.split('/')[2])
  print("welcome to " + driver.title)

def logoutModule(url):
  print("logout:: target url: " + url[5])
  driver.get(url[5])
  print("logout:: logout...")
  if(url[6][0] == 'n'):
    elem = driver.find_element_by_name(url[6][2:])
  elif(url[6][0] == 't'):
    elem = driver.find_element_by_type(url[6][2:])
  elif(url[6][0] == 'i'):
    elem = driver.find_element_by_id(url[6][2:])
  
  elem.click()

  print("logout:: successfully logout "+ driver.current_url.split('/')[2])

myday = 0

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