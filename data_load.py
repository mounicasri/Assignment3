import os
import fnmatch
import shelve

#Traverse the files and save their path and content in to "file_path"
def file_traverse():
    data=set()
    data_list=[]
    dict1={}
    dict2={}
       start_dir="fortune1"
    #walks through all the directories in the given structure
    for dirpath,dirs,files in os.walk(start_dir):
        for single_file in files:
            #Finds all the text files
            if(fnmatch.fnmatch(single_file,"*txt")):
                x=open(os.path.normpath(os.path.join(dirpath, single_file)))
                
                str1=x.read()
                data_list.append(str1)
                dict1[os.path.normpath(os.path.join(dirpath, single_file))]=str1+"\n Last time when the file is modified"+str(os.path.getmtime(os.path.normpath(os.path.join(dirpath, single_file))))+"\n Size of the file "+str(os.path.getsize(os.path.normpath(os.path.join(dirpath, single_file))))
                              
    s=''.join(data_list)
   
##    data=s.split()
##    for word in data:
##        s1=[]
##        for key,value in dict1.items():
##            if word in value:
##                s1.append(key)
##        dict2[word]=s1
##        f[word]=s1
   
        
    return s;
    #f.close()

                                      
    



    


