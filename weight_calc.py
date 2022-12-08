import math

def weight_calc(dictionary):
    weight_dict = {}
    for key in dictionary.keys():
        w = 0
        for v in dictionary[key].values(): #calculating weight using formula
            sq = pow(v, 2)                 #squareroot of sum of squares of tf_idf values of tokens in each doc/query
            w += sq
            res = math.sqrt(w)
            weight_dict.update({key:res})  
    return weight_dict
    

