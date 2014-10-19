import searcher
import data_load
import indexer
#the functions will be called here in order to perform search_engine operations

s=data_load.file_traverse()
indexer.preprocess(s)
print("Please enter the word")
s1=searcher.search()

print(s1)

#Output1

#Please enter the word
#whole and loaves
#['whole', 'loaves']
#[['fortune1\\fortune1\\fortune2\\fortune2.txt']]

#Output2

#Please enter the word
#war or trapped
#['war', 'trapped']
#[['fortune1\\fortune1\\fortune2\\fortune2.txt'], ['fortune1\\fortune1\\fortune2\\fortune3\\fortune4\\fortune5\\fortune6\\fortune7\\fortune8\\fortune9\\fortune10\\fortune11\\fortune11.txt']]
