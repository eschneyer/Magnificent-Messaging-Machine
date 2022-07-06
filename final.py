from tq import *
from download import *
from tweet import *
from bitTransferFinal import *
 
GPIO.setwarnings(False)
InitGPIO()
 
run = True
theUserName = ""
theUserMessage = ""
theActualURL = ""
theActualFile = ""
 
while run == True:
   theUserName = GetAnswer("Please input your name: ")
   if theUserName == "":
       exit("Invalid input: the name is blank")
   theUserMessage = GetAnswer("Please type a message that you would like to share: ")
   if theUserMessage == "":
       exit("Invalid input: the message is blank")
 
   theActualURL = mainTQ()
   theActualFile = mainDownload(theActualURL)
   mainTweet(theUserMessage,theUserName,theActualFile)
 
   repeat = GetYesNoAnswer("Would you like to send another message? ")
 
   if repeat != 1:
       run = False
