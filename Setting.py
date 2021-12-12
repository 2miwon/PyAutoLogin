
### selenium Setting

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

### pyautogui


### speeding option
chrome_options = Options()
## gui option
#chrome_options.headless = True
#chrome_options.add_argument("disable-gpu")
#chrome_options.add_argument("disable-infobars")
#chrome_options.add_argument("--disable-extensions")
##
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
# in repl.it
driver = webdriver.Chrome(options=chrome_options)



## WebAction.py
timeoutInSeconds = 15
timeSleep = 0.5


## INIT
global filelist
filelist = list()


### setting
## 지역별/타겟로그파일/몇일에한번 로그인바꾸라하는지
"""class Setting:
  def __init__(self):
    self.SiteList = "list.csv"
  
  def getSiteList(self):
    return self.SiteList
  def setSiteList(self, i):
    self.SiteList = i

BasicSet = Setting()"""