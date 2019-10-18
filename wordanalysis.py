#Script 4
#Word Comparison: grabs the text of an article and stores a word analysis in an external text file
#the more added, the more information in the text file
#We're on script 4 now and I should probably mention that I absolutely should be
#splitting these into functions. But they're all so small in the first place. Sorry.


#STEP 1:importing necessary modules


#url grabbing
import urllib

#operating system for checking
import os.path

#for importing large blocks of text
import sys

#these are all for manipulating a string
import string
import re

import collections


#Step 2: Create or open file
#I felt this was necessary since otherwise the program would just have to run forever
#in order to compile results

#name of file to be created
#added the random number because i'm not out here tryng to rewrite anybody's files. just in case.
name="All_Words_58.txt"


#checks to see whether it exists already and to read in contents
#this is so past word checks don't get deleted
#(there is an argument to be made that you can't delete the word content of an article you've already read in
#which is something to look into in the future because it could definitely be done)
if os.path.isfile(name):

    #check to delete
    print "File exists, reading in"

    x=open(name,"r")

    if x.mode=="r":

        full_file=x.read()

        x.close()

    words={}
    sources=[]

    #sorting file into usable formats
    n=full_file.split("\n")


    s=n.index("Sources Used:")

    for line in n:
        if n.index(line)>1 and n.index(line)<s:

            line=line.replace(" ","")
            
            
            line=line.split(":")

            words[line[0]]=int(line[1])

        elif n.index(line)==(s+1):

            sources.append(line)

   
    #generating new content

    y=0

    #count
    articles=0
    
    while y!=1:

        
        #example url: http://www.snopes.com/denzel-washington-death-hoax/
        #even though this script doesn't read urls, I am going to use them as an organizational element
        #gets words to base counts on
        url=raw_input("Please input the a URL of your confirmed fake text. To stop entering, enter 'stop': ")
        
        

        if url=="stop":

            y=1
            #while loop ends
            
        else:

            #originally this was going to do what Script 3 did and pull the main text of an article out using the <p> tag
            #however, I wanted to provide a tool that would analyze the language of fake news stories as a whole
            #an a big component of them is they often get shared via facebook exclusively as posts.
            #so instead I opted to have this one just take in text pasted by the user.

            print("Please input the text of your article below. Press Ctrl+D when you're done entering text for ONE article. But if you arne't on Windows or Mac.... abandon hope.")
            
            
            text=sys.stdin.read()

            #stripping punctuation
            text=text.translate(string.maketrans("",""), string.punctuation)
            #this causes a lot of nasty problems with things like times and ages
            #but for the moment i'm just going to relegate anything with numbers in it to second class citizen status
            #which is to say they have no rights and i'm ignoring them on a structural level
            
            #i'm a big believer in resuing variables but the strip, split, and replace modules don't seem to be
            #so what follows is a jungle of slightly different variables

            #replaces doubled new lines with spaces
            textn=text.replace("\n\n"," ")

            #gets rid of the new line that happens with input
            textm=textn.replace("\n","")

            #splits based on spaces
            textl=textm.split(" ")

            #adding to source list
            sources.append(url)

            
            
            for word in textl:
                if word in words:
                    #adds to value
                    words[word]+=1
                else:
                    words[word]=1

            

            #adding to count
            articles+=1

            print("You've entered "+str(articles)+" articles.")

    #left this in for testing purposes
    #this will now create a new file added info
    #name_n=name.strip(".txt")
    #name_f=name_n+"_appended"+".txt"
    #print name
    #creates a messy file structure but i felt this was a better alternative than fully deleting the original file

    #writes over original file
    x=open(name,"w")

    #Title
    x.write("Word Frequencies\n\n")

    for k,v in words.items():

        x.write (k+": "+str(v)+"\n")
        #print words.values()

    x.write("\n\nSources Used:\n")
    for entry in sources:
        x.write(entry+"\n")

    
    
    x.close()
    
    
#if it doesn't exist
#creates the file as if brand new
else:
    #opens/creates file
    x=open(name,"w+")

    #Title
    x.write("Word Frequencies\n\n")

    #priming while loop variable
    y=0

    #setting up dictionary
    words={}

    #count
    articles=0

    while y!=1:

        
        
        #example url: http://www.snopes.com/denzel-washington-death-hoax/
        #even though this script doesn't read urls, I am going to use them as an organizational element
        #gets words to base counts on
        url=raw_input("Please input the a URL of your confirmed fake text. To stop entering, enter 'stop': ")
        
        

        if url=="stop":

            
            
            y=1
            #while loop ends
        else:

            #originally this was going to do what Script 3 did and pull the main text of an article out using the <p> tag
            #however, I wanted to provide a tool that would analyze the language of fake news stories as a whole
            #an a big component of them is they often get shared via facebook exclusively as posts.
            #so instead I opted to have this one just take in text pasted by the user.

            print("Please input the text of your article below. Press Ctrl+D when you're done entering text for ONE article. But if you arne't on Windows or Mac.... abandon hope.")
            
            
            text=sys.stdin.read()

            #stripping punctuation
            text=text.translate(string.maketrans("",""), string.punctuation)
            #this causes a lot of nasty problems with things like times and ages
            #but for the moment i'm just going to relegate anything with numbers in it to second class citizen status
            #which is to say they have no rights and i'm ignoring them on a structural level
            
            #i'm a big believer in resuing variables but the strip, split, and replace modules don't seem to be
            #so what follows is a jungle of slightly different variables

            #replaces doubled new lines with spaces
            textn=text.replace("\n\n"," ")

            #gets rid of the new line that happens with input
            textm=textn.replace("\n","")

            #splits based on spaces
            textl=textm.split(" ")

            #set for sources
            sources=[]

            sources.append(url)

            
            #set for texts
            texts=[]

            texts.append(text)
            
            for word in textl:
                if word in words:
                    #adds to value
                    words[word]+=1
                else:
                    words[word]=1

           
                    
            

            #adding to count
            articles+=1

            print("You've entered "+str(articles)+" articles.")

            
    
    
    for k,v in words.items():

        x.write (k+": "+str(v)+"\n")
        #print words.values()

    x.write("\n\nSources Used:\n")
    for entry in sources:
        x.write(entry+"\n")

    x.close()

    


