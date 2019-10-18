#Script 3: Sources
#This script will strip the html markup of an article searching for linked sources

#Suggested URL: http://www.npr.org/sections/thetwo-way/2017/04/25/525568470/lawmakers-say-it-appears-michael-flynn-acted-illegally-in-taking-russian-payment
#I picked one from a reputable source this time because one of their links sources is twitter
#and i wanted to point out that source verification isn't always as black and white as a domain name

#STEP 1:importing necessary modules


#url grabbing
import urllib

#loop
#continues until an article is provided or the user enters "stop"
x=''

while x!='stop':
    
        url=raw_input("Please enter the URL of an article. If you'd like to stop entering articles, please enter 'stop': ")
        #TO DO: INVALID INPUT
        if url=='stop':
            x='stop'
        elif "http://" in url or "https://" in url:
            

            full=urllib.urlopen(url).read()

            
            #splits based on line
            full=full.split("\n")

            #empty variable for main text of article
            main=""

            #adds main text to main variable by looking for <p> tags
            for bit in full:
                if "<p>" in bit:
                    main+=bit

            #splits based on <p> tags, basically into paragraphs
            main=main.split("<p>")

            #empty list for sources
            sources=[]

            #sorting through to look for <a href> tags
            for bit in main:
                if "href" in bit:

                    #splits based on href
                    bit=bit.split("href")
                    #so bit is now a the of contents

                    #sorting through splits
                    for object in bit:
                        if bit.index(object)>0:

                            #sources now a list of the text, seperated by sources markup
                            sources.append(object)


            #print sources

            #count variable
            c=0
            #sorting through each item in sources list, to strip out website domain of source
            for bit in sources:

                

                #split based on slashes
                bit=bit.split("/")

                #print bit
                
                i=0
                for x in bit:
                    
                    
                    if i==2:
                        sources[c]=x

                    i+=1

                c+=1

            print "Sources cited in this article include: "
            for cite in sources:
                print cite
                #this is a bit faulty because help.npr is still coming through from the surrounding html
                #also if you enter pretty much any other article this whole thing breaks
            
            
                    
        
        else:
            print "Sorry that doesn't appear to be a URL."
            
        
        
    
