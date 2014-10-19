import shelve
import os
import fnmatch
#search for the word input by the user
def search():
    
    f=shelve.open("file_path")
    dict1={}
    s1=[]
    #Retrieves the data from file and place the data to dictionary
    for key in f:
        dict1[key]=f[key]
        
    f.close()
    cond=2
    s=set()
    #print(dict1['whole'],dict1['loaves'])
    query=input()
    s=query.split(' ')
    s1=[]
    if ("or" in s) and (cond!=1):
        s.remove("or")
        cond=0
    if "and" in s:
        s.remove("and")
        cond=1
    print(s)
    #Searches for a word in the dictionary
    for word in s:
        s2=set()
        
        if(word in dict1.keys()) and (cond==0):
            if(dict1[word] not in s1):
                s1.append(dict1[word])
               
        if(word in dict1.keys()) and (cond==1):
            if(len(s1)!=0):
                 for x in dict1[word]:
                     for y in s1:
                         if(y==x):
                             s1.append(x)
                 
            else:
                s1.append(dict1[word])
                    
                    
   
            
    
    
    return s1





        
