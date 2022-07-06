import mysql.connector as mdb
from bitTransferFinal import *
 
#Opens the data and returns the handler
def OpenDatabase():
   mydb = mdb.connect(
       host ="mmss-math-int.lsa.umich.edu",
       user ="mmssmath_read",
       password="pw72gdy0@",
       database = "mmssmath_int",
       port = "3306"
       )
   return mydb
 
#closes when we are done
def CloseDatabase(handle):
   handle.close()
 
#runs the game
def TwentyQuestions(handle):
 
   run = True
 
   mycursor = handle.cursor(dictionary=True)
   mycursor.execute("SELECT * FROM twentyquestions where id = 1")
   myresult = mycursor.fetchone()
 
 
   currQuestion = myresult["content"]
 
   while (run == True):
       currYesNode =myresult["yesnode"]
       currNoNode = myresult["nonode"]
       currURL = myresult["url"]
 
       if currYesNode == None or currNoNode == None:
           return currURL
           run = False
           break
 
       currAnswer = GetYesNoAnswer(currQuestion+" ")
 
       if currAnswer == 1:
           mycursor.execute("SELECT * FROM twentyquestions where id = "+str(currYesNode))
           myresult = mycursor.fetchone()
           currQuestion = myresult["content"]
 
       else:
           mycursor.execute("SELECT * FROM twentyquestions where id = "+str(currNoNode))
           myresult = mycursor.fetchone()
           currQuestion = myresult["content"]
 
def mainTQ():
   twentyQHandle = OpenDatabase()
   theURL = TwentyQuestions(twentyQHandle)
   CloseDatabase(twentyQHandle)
   return theURL
