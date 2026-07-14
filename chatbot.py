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

#for chatbot responses
print(f"Hello {name} I am your chatbot,ask me something ")
#creating dictionary storing information for response 
responses={"hi":"Hello "+name,"how are you":"I am fine","who are you":"I am your chatbot","who build you":"A developer name Montu mili build me","what is python":"python is a programming language","thankyou":"welcome,glad to hear that","do you have emotion":"No i don't have emotions"}
elif 17<=presenttime<20:
 print("Good evening",name) 
else:
 print("Good night",name) 
