import os
import pickle
import numpy as np
import faiss
import logging
from typing import List, Dict, Any, Tuple
from embeddings.embeddings_manager import BaseEmbeddings

logger = logging.getLogger(__name__)

class FAISSStore:
    """A local vector store using FAISS to index and search case document chunks."""
    
    def __init__(self, embeddings: BaseEmbeddings, dimension: int = 384):
        self.embeddings = embeddings
        self.dimension = dimension
        self.index = faiss.IndexFlatIP(dimension)  # Inner Product (Cosine similarity if normalized)
        self.documents: List[Dict[str, Any]] = []

    def add_documents(self, documents: List[Dict[str, Any]]):
        """Add list of documents. Each document must have a 'text' and 'metadata' field."""
        if not documents:
            return
            
        texts = [doc["text"] for doc in documents]
        vectors = self.embeddings.embed_documents(texts)
        
        # Convert to float32 numpy array and normalize for Cosine Similarity
        np_vectors = np.array(vectors, dtype=np.float32)
        faiss.normalize_L2(np_vectors)
        
        self.index.add(np_vectors)
        self.documents.extend(documents)
        logger.info(f"Added {len(documents)} document chunks to FAISS index.")

    def similarity_search(self, query: str, k: int = 4) -> List[Tuple[Dict[str, Any], float]]:
        """Search for top K most relevant document chunks for the query."""
        if not self.documents:
            return []
            
        query_vector = self.embeddings.embed_query(query)
        np_query = np.array([query_vector], dtype=np.float32)
        faiss.normalize_L2(np_query)
        
        # Search index
        scores, indices = self.index.search(np_query, min(k, len(self.documents)))
        
        results = []
        for score, idx in zip(scores[0], indices[0]):
            if idx == -1 or idx >= len(self.documents):
                continue
            results.append((self.documents[idx], float(score)))
            
        return results

    def save(self, directory: str):
        """Persist FAISS index and documents metadata to disk."""
        os.makedirs(directory, exist_ok=True)
        index_path = os.path.join(directory, "faiss.index")
        metadata_path = os.path.join(directory, "documents.pkl")
        
        faiss.write_index(self.index, index_path)
        with open(metadata_path, "wb") as f:
            pickle.dump(self.documents, f)
        logger.info(f"Persisted vector index to {directory}")

    def load(self, directory: str):
        """Load FAISS index and documents metadata from disk."""
        index_path = os.path.join(directory, "faiss.index")
        metadata_path = os.path.join(directory, "documents.pkl")
        
        if not os.path.exists(index_path) or not os.path.exists(metadata_path):
            logger.warning(f"Vector store files not found in {directory}. Starting with an empty index.")
            return
            
        self.index = faiss.read_index(index_path)
        with open(metadata_path, "rb") as f:
            self.documents = pickle.load(f)
        logger.info(f"Successfully loaded vector index with {len(self.documents)} chunks from {directory}")
