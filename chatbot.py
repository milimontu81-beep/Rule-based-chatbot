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

#for chatbot responses
print(f"Hello {name} I am your chatbot,ask me something ")
#creating dictionary storing information for response 
responses={"hi":"Hello "+name,"how are you":"I am fine","who are you":"I am your chatbot","who build you":"A developer name Montu mili build me","what is python":"python is a programming language","thankyou":"welcome,glad to hear that","do you have emotion":"No i don't have emotions"}
elif 17<=presenttime<20:
 print("Good evening",name) 
else:
 print("Good night",name)
 
#creating a function for answering the question
def ask(userquestion):
   if userquestion.lower() in responses:
     print("chatbot response :",responses[userquestion])
   else: 
     print("sorry,I could not able to answer yet,i will learn it soon")

#for asking question again and again 
while True:
   #for asking question 
   userquestion=input("ask me something:")
   if userquestion.lower()=="bye":
     print("chatbot response:thanks for using me")
   break
   #calling function 
   ask(userquestion) 
 
