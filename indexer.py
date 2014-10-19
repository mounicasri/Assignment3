import shelve
import data_load
#Preprocess the data
def preprocess(s):
    dict2={}
    data=s.split()
    for word in data:
        s1=[]
        for key,value in dict1.items():
            if word in value:
                s1.append(key)
        dict2[word]=s1
        f[word]=s1
    f=shelve.open("file_path")
    dict1={}
    for key in f:
        dict1[key]=f[key]
        
    f.close()
    return





