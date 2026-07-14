#wellcome massage 
print("welcome to rule based chatbot ")

#for greeting the user according to the time 
import datetime 
import time
presenttime=time.localtime().tm_hour
#for user name
name=input("Enter your name:")
#putting condition for greeting
if 1<=presenttime<12:
 print("Good morning",name)
elif 12<=presenttime<17:
 print("Good afternoon",name)
elif 17<=presenttime<20:
 print("Good evening",name) 
else:
 print("Good night",name) 
