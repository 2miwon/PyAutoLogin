from Setting import *
from selenium.webdriver.common.keys import Keys

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
  elif(targetEle[0] == 'c'): #class
    return driver.find_element_by_class(ElementFinder(targetEle))
  elif(targetEle[0] == 'x'): #xpath
    return GetElement(ElementFinder(targetEle))

## x-path only
def GetElement(target):
  return WebDriverWait(driver, timeoutInSeconds).until(
    EC.presence_of_element_located((By.XPATH, target)))


## Waiting until load webpage



# primary Action
def InputText(text, target):
  target.send_keys(text)

def Enter(target):
  target.send_keys(Keys.RETURN)

def Click(target):
  target.click()

def GetPage(url):
  driver.get(url)

def GetPageName():
  return driver.current_url.split('/')[2]

def Cursor(target):
  driver.move_to_element(target)

# secondary Action
def ElementInput(E, content):
  target = ElementChecker(E)
  InputText(content, target)
  return True

def ElementEnter(E):
  target = ElementChecker(E)
  Enter(target)
  return True

def ClickButton(xpath):
  target = GetElement(xpath)
  Click(target)
  return target.text

def GetText(xpath):
  target = GetElement(xpath)
  return target.text

# module
def Login(e_ID, ID, e_PW, PW):
  if (ElementInput(e_ID, ID) and ElementInput(e_PW, PW)):
    ElementEnter(e_PW)
    return True
  else:
    return False

def SkipChange(e_skip): 
  try:
     ElementEnter(e_skip)
  except:
    print("error")
 
def CheckPage(realname, e):
  if GetPageName() != realname:
    SkipChange(e)
    return False
  return True




