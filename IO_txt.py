import os

def ReadFile(filename):
  return open(filename,'r')

def WriteFile(filename):
  return open(filename,'w')

def AddFile(filename):
  return open(filename,'a')
  
def isEmptyFile(filepath):
  return os.stat(filepath).st_size == 0

### second

def ReadNWrite(filename):
  temp = ReadFile(filename)
  global Tstack
  Tstack = temp.readlines()
  return WriteFile(filename)

"""
def ReadLine(file):
  return file.readline()
"""
def txtTOtuple(line):
  sp = RemoveN(line).split(" ")
  if len(sp) == 1:
    return (sp[0],)
  else:
    return (sp[0], sp[1:])

def RemoveN(str):
  return str[:-1]
  


  

