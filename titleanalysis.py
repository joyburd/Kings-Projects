#Script 2
#fetches headline of an article and
#searches these against current headlines


#STEP 1:importing necessary modules


#url grabbing
import urllib

#access to searchable web crawl
#info on Webhoseio here: https://webhose.io
#other necessary info provided in zip file under webhosio-python-master file
#the most pertinent information is that webhoseio produces a news crawl limited to the last three days
#ideally a user would be warned about this limit, or a service could be used that doesn't impose it
#the implications of this limit are that only headlines that are relatively recent can be checked with any kind of validity
import webhoseio


#STEP 2: grabbing article headline
#suggested article: https://now8news.com/united-airlines-flight-attendant-slaps-crying-baby/
#I should provide a warning that this particular article will be far out of date by the time
#anyone but me sees it, so the results returned may be kind of odd
#I picked this one in particular because it preys on a story that I think will continue
#to unfold in the news for awhile, so the results should at the very least be interesting

#loop
#continues until an article is provided or the user enters "stop"
x=''
while x!='stop':
    url=raw_input("Please enter the URL of an article. If you'd like to stop entering articles, please enter 'stop': ")
    #TO DO: INVALID INPUT
    if url=='stop':
        x='stop'
    else:
        full=urllib.urlopen(url).read()

        #splits text by line
        text=full.split('\n')
        #sorts through looking for title
        for line in text:
            
            #looking for line containing title
            if '<title>' in line:

                #splits line by carrot to seperate the headline from style tags
                line=line.split(">")
                
                #splits headline and source based on the dash between them
                headline=line[1].split('-')
                
                #this worked for most of the fake news articles I tried as their markup tends to be a bit simplistic
                #it got complicated for some bigger news organizations like NPR though
                #so I built in a confirmation just in case, so the user can paste in their headline if all else fails

                c_headline=raw_input("Is this your headline? " + headline[0] + "\nPlease enter y for yes or n for no: ")

                if c_headline=='y':
                    headline[0]=headline[0]
                else:
                    headline[0]= raw_input("I'm sorry. Please copy and paste the headline directly from the article: ")
                    #other ways of doing this include allowing the user to enter exactly what's extraneous on the headline
                    #and setting that to a variable and putting in a split function to remove it directly
                    #but I don't have all the time in the world here guys

             
                #STEP 3
                #splits headline into terms and searches news crawl for them
                #TO DO: split these into functions probably

                #splits through headline by spaces
                headline=headline[0].split(" ")

                #my verification process for these articles is to search how many results the entire headline gets
                #and match that against the results individual words get
                #the hope is that by narrowing the results to news, it will compare what's being reported by news organizations to this article
               
                #searching full string
                search=""

                for word in headline:
                    if word!="":
                        search+=word+" "
                    else:
                        search=search
                    

                search='"'+search+'"'+' langugage:(english) (site_type:news)'



                print search

                #first it's going to search the whole title
                webhoseio.config(token="282a28d3-227f-45f4-bb33-284c5b0dcb61")
                output = webhoseio.query("filterWebData", {"q":search})

 
                full_results=output['totalResults']

                results=[]
                #searching single words
                #for word in headline:
                for word in headline:
                    if word!="":
                        search=word

                        search=search+" language:(english) (site_type:news)"
                        print search

                
                        webhoseio.config(token="282a28d3-227f-45f4-bb33-284c5b0dcb61")
                        output = webhoseio.query("filterWebData", {"q":search})

 
                        results.append(output['totalResults'])

                print results

                #searching for pairs
                #i decided only to search in singles or pairs to get more coherent results


                pairs_results=[]
                pairs=[]
                
                for word in headline:
                    #ergo, if it isn't the first word

                    if headline.index(word)==0:
                        pair=word+" "+headline[1]

                        pairs.append(pair)

                        search=pair

                        search=search+" language:(english) (site_type:news)"
                        print "Searching for term: "+pair

                
                        webhoseio.config(token="282a28d3-227f-45f4-bb33-284c5b0dcb61")
                        output = webhoseio.query("filterWebData", {"q":search})

 
                        pairs_results.append(output['totalResults'])
                    elif headline.index(word)!=0 and headline.index(word)!=headline.index(headline[-1]):
                        
                        pair=word+" "+headline[(headline.index(word)+1)]


                        pairs.append(pair)
                        
                        search=pair

                        search=search+" language:(english) (site_type:news)"
                        print "Searching for term: "+pair

                
                        webhoseio.config(token="282a28d3-227f-45f4-bb33-284c5b0dcb61")
                        output = webhoseio.query("filterWebData", {"q":search})

 
                        pairs_results.append(output['totalResults'])


        #STEP 4: PRINTOUT
        #this printout is pretty simplistic since I realized the results really implied
        #much less than I'd hoped.
        print "The headline returned " +str(full_results)+" for a complete match."
        print "The following terms resulted in more than "+str(full_results)+" :"

        print headline
        print results
        print pairs
        print pairs_results

        
        
        
