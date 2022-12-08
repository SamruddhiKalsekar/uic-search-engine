

def remove_stopwords(dictionary, path):
    stopwords = list(open(path))                               #reading stopwords from path
    stop_words = []
    for i in stopwords:
        i = i.strip()
        stop_words.append(str(i))
    for k, v in dictionary.items():                            #iterating through dictionary of tokens
        tokens_without_stopwords = [word for word in dictionary[k] if not word.lower() in stop_words]
        dictionary.update({k:tokens_without_stopwords})        #removal of stopwords and updating dictionary
    return dictionary                                          #return processed dictionary



