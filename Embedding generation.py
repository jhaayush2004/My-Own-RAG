from collections import Counter
import math

query_tokens=user_query.lower().split(" ")
documents_tokens=corpus.lower().split(" ")

query_counter=Counter(query_tokens)
document_counter=Counter(documents_tokens)

lst = []
for token in query_counter.values():
    lst.append(token)
