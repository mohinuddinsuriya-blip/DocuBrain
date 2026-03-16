from sklearn.metrics.pairwise import cosine_similarity

def find_relationships(embeddings):

    similarity = cosine_similarity(embeddings)

    return similarity