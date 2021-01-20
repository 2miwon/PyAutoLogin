# for repl.it (online ide)

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
#hiding option
#chrome_options.headless = True
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
  print("target url :" + url[0])
  driver.get(url[0])
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
  
  print("successfully login "+ driver.current_url.split('/')[2])
  print("welcome to " + driver.title)

def logoutModule(url):
  print("target url :" + url[5])
  driver.get(url[5])
  print("logout...")
  if(url[6][0] == 'n'):
    elem = driver.find_element_by_name(url[6][2:])
  elif(url[6][0] == 't'):
    elem = driver.find_element_by_type(url[6][2:])
  elif(url[6][0] == 'i'):
    elem = driver.find_element_by_id(url[6][2:])
  
  elem.click()

  print("successfully logout "+ driver.current_url.split('/')[2])

for url in mysites:
  loginModule(url)
  logoutModule(url)
  



