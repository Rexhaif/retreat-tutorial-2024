import math

def compute_tf(document):
    tf_dict = {}
    doc_len = len(document)
    for word in document:
        if word not in tf_dict:
            tf_dict[word] = 1
        else:
            tf_dict[word] += 1

    for word in tf_dict:
        tf_dict[word] = tf_dict[word] / doc_len
    return tf_dict

def compute_idf(documents):
    N = len(documents)
    idf_dict = {}
    all_words = set(word for document in documents for word in document)

    for word in all_words:
        idf_dict[word] = 0
        for document in documents:
            if word in document and document[word] > 0:
                idf_dict[word] += 1

    for word in idf_dict:
        idf_dict[word] = math.log(float(idf_dict[word]) / N)
    return idf_dict

def compute_tfidf(tf, idf):
    tfidf = {}
    for word, val in tf.items():
        tfidf[word] = val * idf[word]
    return tfidf

doc_a = "the cat sat on my face"
doc_b = "the dog sat on my bed"

# Preprocess documents
doc_a_words = doc_a.split()
doc_b_words = doc_b.split()

# Compute TF for each document
tf_a = compute_tf(doc_a_words)
tf_b = compute_tf(doc_b_words)

# Compute IDF
idf = compute_idf([tf_a, tf_b])

# Compute TF-IDF
tfidf_a = compute_tfidf(tf_a, idf)
tfidf_b = compute_tfidf(tf_b, idf)
print(f"TF-IDF for Document A: {tfidf_a}")
print(f"TF-IDF for Document B: {tfidf_b}")