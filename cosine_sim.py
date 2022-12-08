
def cosine_sim(queries_tfidf, idf, inv_index_output, weights, queries_weights):
    cos_sim = {}
    for queryid, tf in queries_tfidf.items():                             #iterating over tf_idf calculated against 10 queries
        cos_sim[queryid] = {}
        for word, freq in tf.items():
            if word in inv_index_output:
                for doc_id, doc_tf in inv_index_output[word].items():
                    weight_document = doc_tf * idf[word]                  #multiplication of weights in the nominator and vectors in denominator
                    weight_query = freq * idf[word]
                    try:
                        cos_sim[queryid][doc_id] += (weight_document * weight_query) /(weights[doc_id]*queries_weights[queryid])
                    except:
                        cos_sim[queryid][doc_id] = (weight_document * weight_query) / (weights[doc_id]*queries_weights[queryid])
        cos_sim[queryid] = dict(sorted(cos_sim[queryid].items(), key=lambda item: item[1], reverse=True)) #sorting based on cosine similarity value
    return cos_sim

