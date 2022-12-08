import os
import re 
import string
import pickle
from stem import stem
from preprocess import preprocess
from tokenizer import tokenizer
from inverted_index import inverted_index
from tf_idf import tf_idf
from weight_calc import weight_calc


crawledData_path =r"/Users/samruddhi/Desktop/search-engine/uic-search-engine/CrawledData"
queries_path = r"/Users/samruddhi/Desktop/search-engine/uic-search-engine/queries.txt"
stopwords_path =r"/Users/samruddhi/Desktop/search-engine/uic-search-engine/stopwords.txt"  

# processing for crawled documents
tokenized_dict = tokenizer(crawledData_path)
n = len(tokenized_dict)
stemmed_output = stem(tokenized_dict,stopwords_path)                         #passing dictionary{DocNO:[pre-preprocessed tokens]}
inv_index_output = inverted_index(stemmed_output)
tf_idf_output, idf = tf_idf(n , inv_index_output)
weights = weight_calc(tf_idf_output)


# processing for queries
queries = preprocess(queries_path)
queries_stemmed = stem(queries,stopwords_path)
queries_inv_index = inverted_index(queries_stemmed)
qn = len(queries)
queries_tfidf, idf = tf_idf(qn ,queries_inv_index )
queries_weights = weight_calc(queries_tfidf)

pickleData = "./PickleFiles/"
os.makedirs(pickleData, exist_ok=True)
with open(pickleData + 'inverted_index.pickle', 'wb') as f:
    pickle.dump(inv_index_output ,f)
    
with open(pickleData + 'tokens.pickle', 'wb') as f:
    pickle.dump(stemmed_output,f)

