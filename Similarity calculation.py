lst = []
# using only common words in both query_counter and document_counter
for token in query_counter.values():
    lst.append(token)

for tokens in query_counter.keys() & document_counter.keys(): 
    print(tokens)

mylist = []
for token in query_counter.keys() & document_counter.keys(): 
    mylist.append(query_counter[token]*document_counter[token])

dot_product=sum(mylist)

query_magnitude = math.sqrt(sum(query_counter[token] ** 2 for token in query_counter))
document_magnitude = math.sqrt(sum(document_counter[token] ** 2 for token in document_counter))

similarity = (dot_product)/(query_magnitude*document_magnitude)

## OR combining all we get a new function

def cosine_similarity(query, document):
    # Tokenize and convert to lowercase
    query_tokens = query.lower().split(" ")
    document_tokens = document.lower().split(" ")

    # Create Counters for query and document
    query_counter = Counter(query_tokens)
    document_counter = Counter(document_tokens)

    # Calculate dot product
    dot_product = sum(query_counter[token] * document_counter[token] for token in query_counter.keys() & document_counter.keys())

    # Calculate magnitudes
    query_magnitude = math.sqrt(sum(query_counter[token] ** 2 for token in query_counter))
    document_magnitude = math.sqrt(sum(document_counter[token] ** 2 for token in document_counter))

    # Calculate cosine similarity
    similarity = dot_product / (query_magnitude * document_magnitude) if query_magnitude * document_magnitude != 0 else 0

    return similarity
