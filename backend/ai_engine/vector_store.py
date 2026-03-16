import faiss
import numpy as np

index = faiss.IndexFlatL2(384)

def store_vectors(vectors):

    index.add(np.array(vectors))