
def inverted_index(dictionary):
    vocab = [item for i in dictionary.values() for item in i]      #all tokens in cranfieldDocs
    total_vocab = list(set(vocab))                                 #unique tokens 
    inv_index = {}                                                 #dictionary: {token:[docid,wordfrequency]}
    for word in total_vocab:                                       
        for k, v in dictionary.items():
            if word in v:                                          #if token from total_vocab exists in a doc
                wordfreq = v.count(word)                           #count the frequency it appears in the doc
                inv_index.setdefault(word, {}).update({int(k): wordfreq}) 
    return inv_index                                               #update dictionary{token:{docid : wordfreq}}
            

