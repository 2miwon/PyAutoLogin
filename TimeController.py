import time

### time controller
def ConvertTOLocaltime(rawtime):
  return time.localtime(rawtime)

def ConvertUTCtoKst(utc):
  kst = utc + 60*60*9
  return kst

def twoD0(p) :
  return '{:0>2}'.format(p)

def GetNowTime():
  return "{0}/{1}/{2} {3}:{4}".format(
    KR.tm_year, 
    twoD0(KR.tm_mon), 
    twoD0(KR.tm_mday),
    twoD0(KR.tm_hour),
    twoD0(KR.tm_min)
    )

def GetNowDay():
  return "{0}/{1}/{2}".format(
    KR.tm_year,
    twoD0(KR.tm_mon), 
    twoD0(KR.tm_mday)
    )

timeLine = ConvertUTCtoKst(time.time())
KR = ConvertTOLocaltime(timeLine)
  
""""      
      start = time.time()
      end = time.time()
      timestamp = end-start
      #print("It took {0}second to access {1}".format('.1f'.format(timestamp),(SiteDatabase[0].URL_Login).split('/')[2]))
"""