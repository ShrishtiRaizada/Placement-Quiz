
print("Welcome to the Placement Quiz")

name=input("Enter your name " )

print("Hello "+name)

reply=input("Do you want to play this quiz? " )

if reply.lower() != "yes":
    quit()

print("Okay let's play ")    

score=0

#1
ans=input("What is the language used by most of the DBMSs for helping their users to access data? " )
if ans.lower()=="query language":
    print("Congratulations its correct")
    score+=1
else:
    print("Sorry its incorrect")  

#2
ans=input("In SQL, which command is used to make permanent changes made by statements issue since the beginning of a transaction? " )
if ans.lower()=="commit":
    print("Congratulations its correct")
    score+=1
else:
    print("Sorry its incorrect") 

#3
ans=input("The part of machine level instruction, which tells the central processor what has to be done, is " )
if ans.lower()=="operation code":
    print("Congratulations its correct")
    score+=1
else:
    print("Sorry its incorrect")  

#4
ans=input("While running DOS on a PC, which command would be used to duplicate the entire diskette? " )
if ans.lower()=="diskcopy":
    print("Congratulations its correct")
    score+=1
else:
    print("Sorry its incorrect")  

#5
ans=input("A function that returns no values to the program is called? " )
if ans.lower()=="void":
    print("Congratulations its correct")
    score+=1
else:
    print("Sorry its incorrect")  

#6
ans=input("What does C++ append to the end of a string literal constant? " )
if ans.lower()=="null character":
    print("Congratulations its correct")
    score+=1
else:
    print("Sorry its incorrect")  

#7
ans=input("Which of the condition is used to transmit two packets over a medium at the same time? " )
if ans.lower()=="collision":
    print("Congratulations its correct")
    score+=1
else:
    print("Sorry its incorrect")  
  
#8
ans=input("A distributed network configuration in which all data/information pass through a central computer is " )
if ans.lower()=="star network":
    print("Congratulations its correct")
    score+=1
else:
    print("Sorry its incorrect")  

#9
ans=input("What is the term used for describing the judgmental or commonsense part of problem solving? " )
if ans.lower()=="heuristic":
    print("Congratulations its correct")
    score+=1
else:
    print("Sorry its incorrect")  

#10
ans=input("In LISP, the function evaluates both <variable> and <object> is " )
if ans.lower()=="set":
    print("Congratulations its correct")
    score+=1
else:
    print("Sorry its incorrect")  
   

print("Thankyou for attempting the quiz")

print("Your total score is "+ str(score))
   
 
  



