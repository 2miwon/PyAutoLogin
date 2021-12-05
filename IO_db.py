import sqlite3 as sql
print("sqlite3 library version : " + sql.version)
print("SQLite DB Engine version : " + sql.sqlite_version)

# C_ : Command

#tag
tag_maketable = "DB :: Making Table :: "

### interaction with DB
SiteDB = sql.connect("data.db")
cursor = SiteDB.cursor()

def init():
  cursor.execute("CREATE TABLE TableList (TableName text)") # make TableList
  MakeTable("SiteInfo", "(Name text, ID text, PW text, E_ID text, E_PW text, URL_login text, URL_logout text)")
  #MakeTable("ActionTable", "Action text",)
  
  #MakeTable("TimeTable")
  # MakeTable("SiteRecord") // 현적립금 / 총로그인횟수 / last logined 시간

def MakeTable(name, text):
  cursor.execute("CREATE TABLE " + name + text)
  cursor.execute("INSERT INTO TableList VALUE " + name)

def InputColumn():
  text = " ("
  count = 0
  command = input(tag_maketable + "input [ name type ] or input none to exit (default type = text): ")
  while command != "":
    text += command
    text += ", "
    command = input(tag_maketable + "input [ name type ] or input none to exit (default type = text): ")
    count += 1
  text = text[:-2]
  text += ")"
  print(tag_maketable + "successfully input " + count + " column")
  return text

def InsertData(table, myds):
  cursor.executemany("INSERT INTO " + table1(id, name, birthday) + "VALUES(?,?,?)", myds)

# Table Info visualization

def ReadALL():
  DBfile = sql.connect("data.db")
  cursor = DBfile.cursor
  
  #tlist = ReadTable(Table)
  cursor.execute("SELECT * FROM *")
  
  ReadTable()

def ReadTable(tablename):
  cursor.execute("SELECT * FROM " + tablename)
  return cursor.fetchall()

def PrintTable(list_table):
  for row in list_table:
    print(row)
    #for i in row:
      #print()


#PrintTable(table)
