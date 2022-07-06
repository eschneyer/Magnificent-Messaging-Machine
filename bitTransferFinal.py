import RPi.GPIO as GPIO
import time
 
def InitGPIO():
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(17, GPIO.IN)
   GPIO.setup(22, GPIO.IN)
   GPIO.setup(27, GPIO.OUT)
 
def GetData():
   if GPIO.input(17):
       return 1
   else:
       return 0
 
def GetClock():
   if GPIO.input(22):
       return 1
   else:
       return 0
def SetReset(value):
   if value == 0:
       GPIO.output(27, GPIO.LOW)
   else:
       GPIO.output(27, GPIO.HIGH)
 
def GetBit():
 
   while (GetClock() != 1): # wait for clock to go up and down
       time.sleep(0.01)
   while (GetClock() != 0):
       time.sleep(0.01)
 
   return GetData()
 
def GetNum(n):
   bits = ""
   num = 0
   SetReset(0)
   for i in range (n):
       bit = GetBit()
       print(str(bit), end = "")
       bits += str(bit)
       '''if bit == 1:
           num += 2**i'''
       num = num*2 + bit
       SetReset(1)
   return num
 
def GetChar(n):
 
   return chr(n)
 
def GetString():
   endString = 0
   num = GetNum(8)
   word = ""
   while num != endString:
       word += GetChar(num)
       print(" " + word)
       num = GetNum(8)
   return word
 
def GetAnswer(userInput):
   print(userInput)
   string = GetString()
   return string
 
def GetYesNoAnswer(prompt):
   print(prompt)
   return GetNum(1)
 
def mainBitTransfer():
   InitGPIO()
   print("please input a string.")
   string = GetString()
   print(string)
   ans = 1
   while (ans != 0):
       string = GetString()
       print(string)
       ans = GetYesNoAnswer("do you want to continue?")
   return string
