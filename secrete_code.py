import secrets
import string
import os 
import time
def inputstring():
   while True:
     str = input("Enter the string:")
     if(len(str)>0): 
        return str
     else:
        print("please enter a string of atleast one character ")
   
def codingtext():
   """This function takes a string as input and returns a string with the first letter of each word"""
   str=inputstring()
   if(len(str)<3):
      return "".join(reversed(str))
   else:
      front=''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(5))
      ending=''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(5))
      return(front+str[3:]+ending+str[0:3])

def decodingtext():
   """This function takes a string as input and returns a string with the first letter of each word"""
   str=inputstring()
   while True:
     if(len(str)<3):
        return "".join(reversed(str))
   
     elif(len(str)>12):
          length=len(str)
          return(str[length-3:]+str[5:length-8])
     else:
        print("you are entering wrong key \nplease enter a key of size either 2 or more than 13.")
        str=inputstring()
while True:
  os.system('cls' if os.name == 'nt' else 'clear')
  str=input("what do you want to do?\npress\n1. for encryption\n2. for decryption\n3. for exit\n")
  if(str=="1"):
     print(codingtext())
     time.sleep(5)
  elif(str=="2"):
     print(decodingtext())
     time.sleep(5)
  elif(str=="3"):
     print("thank you for using this program")
     os._exit(0)
  else:
     print("please enter a valid input either 1 or 2")