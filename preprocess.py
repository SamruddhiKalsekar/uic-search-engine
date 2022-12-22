import re
import string
from nltk.stem import PorterStemmer


def preprocess(query,path):
    query = query.lower()
    pattern = "[" + re.escape(string.punctuation) + "]" 
    punctuation_removal = re.sub(pattern, "", query)         #punctuation removal
    remove_num = re.sub(r'[~^0-9]', '', punctuation_removal)  #number removal
    whitespace_removal = remove_num.split()  
    stopwords = list(open(path))                               #reading stopwords from path
    stop_words = []
    for i in stopwords:
        i = i.strip()
        stop_words.append(str(i)) 
    tokens_without_stopwords = [word for word in whitespace_removal if not word.lower() in stop_words]
    ps = PorterStemmer() 
    token_stemmed = [ps.stem(word) for word in tokens_without_stopwords if len(ps.stem(word))>2 ]
    unique = set(token_stemmed)  
                                             
    return unique
            

