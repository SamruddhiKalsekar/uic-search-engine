import os, pickle, operator, math, math, copy
from collections import Counter
# from tf_idf import calc_tf_idf, page_length
from preprocess import preprocess
# from cosine_sim import cos_sim
from collections import defaultdict


stopwords_path =r"/Users/samruddhi/Desktop/search-engine/uic-search-engine/stopwords.txt"  
freq = {}
crawlNum = 3500
b = {}
a = {}



def calc_idf( n, dictionary):
    idf = defaultdict(dict)
    # df = defaultdict(dict)
    # for key in dictionary.keys():
    #     df[key] = len(dictionary[key].keys())
    #     idf[key] = math.log(n/df[key], 2)    
    return idf
    idf = {}

    for key in dictionary.keys():
        df = len(dictionary[key].keys())
        idf[key] = math.log2(n/df)
    return idf

def calc_tfidf(data, token):
    # tf_idf = copy.deepcopy(inverted_index)
    # key = frozenset(data.items())
    inverted_index[token][data] = inverted_index[token][data] * idf[token]
    return inverted_index[token][data]

def tf_idf( n, dictionary):
    freq_dict = defaultdict(dict)
    idf = defaultdict(dict)
    for k , v in dictionary.items():
        for k_ , v_ in v.items():
            freq_dict[k_][k] = v_*math.log2(n/len(v))      #calculating tf_idf using formula
            idf[k] = math.log2(n/len(v))
    return freq_dict, idf
    
    
def calc_tfidf(inverted_index):
    tf_idf = copy.deepcopy(inverted_index)
    
    for token in tf_idf:
        for page in tf_idf[token]:
            tf = tf_idf[token][page] / freq[page]
            tf_idf[token][page] = tf * result_idf[token]
    
    return tf_idf   
def doc_length(data, tokens):
    hashmap = []
    length = 0
    for token in tokens:
        if token not in hashmap:
            # print(a[1])
            length += a[data][token] ** 2
            hashmap.append(token)
    return math.sqrt(length)

    
def page_length(tokens):
    doc_l = {}
    for i in range(crawlNum+1):
        doc_l[str(i)] = doc_length(i, tokens[str(i)])
    return doc_l


def cosine_simi(query, doc_lens):
    similarity_scores = {}
    query_len = 0
    query_weights = {}
    dict_len = len(a)
    
    query_dict = Counter(query)
    
    
    for token in query_dict.keys():
        token_tf = query_dict[token] / query_dict.most_common(1)[0][1]
        query_weights[token] = token_tf * b.get(token,0)
        query_len += query_weights[token] ** 2
    
    query_len = math.sqrt(query_len)
    
    for token in query:
        token_weight = query_weights.get(token)
  
        if token_weight:
            for i in range(1, dict_len):
                for page in a[i].keys():
                    if(token == page):
                        similarity_scores[i] = similarity_scores.get(i,0) + (a[i][token] * token_weight)

    for page in similarity_scores:        
        similarity_scores[page] = similarity_scores[page] / (doc_lens[str(page)] * query_len)  
    return similarity_scores

def print_output(webpages,n):
    for i in range(n, n+10):
        try:
            url_no = int(webpages[i][0])
            
        except Exception as e: 
            print("\nNo more results found !!")
            break
            
        if links.get(url_no, None):
            print(i+1,links.get(url_no))



pickle_folder = "./PickleFiles/"
os.makedirs(pickle_folder, exist_ok=True)

with open(pickle_folder +'inverted_index.pickle', 'rb') as f:
    inverted_index=pickle.load(f)

with open(pickle_folder +'tokens.pickle', 'rb') as f:
    tokens=pickle.load(f)

with open(pickle_folder +'url.pickle', 'rb') as f:
    links=pickle.load(f)       


a , b = tf_idf(crawlNum, inverted_index)
page_lengths = page_length(tokens)


query = str(input("Enter search query : "))
query_processed = preprocess(query, stopwords_path)

similarityIndex = cosine_simi(query_processed, page_lengths)
print(similarityIndex)
fetched = sorted(similarityIndex.items(), key=operator.itemgetter(1), reverse=True)
count = 0
flag = True

while flag or (iteration == 'yes' or iteration == 'y' or iteration == 'Yes' or iteration == 'Y'):
    flag = False
    print_output(fetched,count)
    count += 10
    iteration = str(input("View more? Yes/yes/Y/y: ")) 
