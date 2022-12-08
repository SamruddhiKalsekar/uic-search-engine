
from collections import defaultdict
import math

def tf_idf( n, dictionary):
    freq_dict = defaultdict(dict)
    idf = defaultdict(dict)
    for k , v in dictionary.items():
        for k_ , v_ in v.items():
            freq_dict[k_][k] = v_*math.log2(n/len(v))      #calculating tf_idf using formula
            idf[k] = math.log2(n/len(v))
    return freq_dict, idf
    
    

