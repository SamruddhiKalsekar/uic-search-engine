import os
import re 
import string
from stem import stem
from preprocess import preprocess
from tokenizer import tokenizer
from inverted_index import inverted_index
from tf_idf import tf_idf
from weight_calc import weight_calc


crawledData_path =r"/Users/samruddhi/Desktop/search-engine/uic-search-engine/CrawledData"
stopwords_path =r"/Users/samruddhi/Desktop/search-engine/uic-search-engine/stopwords.txt"  


# processing for queries
queries = preprocess(folder_path2)
queries_stemmed = stem(queries,stopwords_path)
queries_inv_index = inverted_index(queries_stemmed)
qn = len(queries)
queries_tfidf, idf = tf_idf(qn ,queries_inv_index )
queries_weights = weight_calc(queries_tfidf)