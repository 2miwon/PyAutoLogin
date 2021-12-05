#from main import Site

#def ReadCSV(setting):
#  return open(setting.getSiteList(),'r')

def ReadFile(filename):
  return open(filename,'r')

def ReadLineToList(line, spl):
  return line.split(spl)
  #return ConvertData(rawlist)

"""
def ConvertData(rawlist):
  site = Site(rawlist[0], rawlist[1], rawlist[2], rawlist[3], rawlist[4], rawlist[5],rawlist[6][:-1])
  return site
"""

def ReadCSVModule():
  #file = ReadCSV(BasicSet)
  file = CSV.Read("list.csv")
  line = file.readline()
  while(line):
    SiteDatabase.append(Site(CSV.ReadLineToList(line, ',')))
    line = file.readline()