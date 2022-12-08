import re
import string

def preprocess(path):
    key_count = 1                                                 #queryid 
    query_dict = {}                           
    pattern = "[" + re.escape(string.punctuation) + "]" 
    queries = list(open(path))                                    #reading queries
    query = []
    for q in queries:                     
        query.append(q.strip())
    for i in query:
        punctuation_removal = re.sub(pattern, "", str(i))         #punctuation removal
        remove_num = re.sub(r'[~^0-9]', '', punctuation_removal)  #number removal
        whitespace_removal = remove_num.split()                   #split whitespaces
        query_dict.update({key_count:whitespace_removal})         #update dict{queryID:preprocessed query}
        key_count += 1                                            #increasing count for every iteration
    return query_dict
            

