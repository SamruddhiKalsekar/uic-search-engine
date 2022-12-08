
from remove_stopwords import remove_stopwords
from nltk.stem import PorterStemmer

def stem(dictionary,path):
    dictionary = remove_stopwords(dictionary, path)           #stopwords removal
    ps = PorterStemmer()                                      #defining stemmer  
    for key, value in dictionary.items():                     #iterating through dictionary to stem each token
        post_stemming = [ps.stem(word) for word in value]
        dictionary.update({key:post_stemming})                #updating dictionary value with stemmed token
    for k, v in dictionary.items():
        for token in v:
            if len(token)<=2 :                                #removing words with one or two characters in length
                v.remove(token)
    dictionary = remove_stopwords(dictionary, path)
    return dictionary                                         #returning processed dictionary



