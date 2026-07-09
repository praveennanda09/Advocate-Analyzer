import hashlib
import numpy as np
import logging
from typing import List, Optional

logger = logging.getLogger(__name__)

class BaseEmbeddings:
    """Interface for text embeddings."""
    def embed_query(self, text: str) -> List[float]:
        raise NotImplementedError()
        
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        raise NotImplementedError()

class MockEmbeddings(BaseEmbeddings):
    """Deterministic, zero-dependency embedding model for tests and offline RAG."""
    
    def __init__(self, dimension: int = 384):
        self.dimension = dimension

    def embed_query(self, text: str) -> List[float]:
        # Generate a deterministic vector based on MD5 hash of input text
        hasher = hashlib.md5(text.encode("utf-8"))
        hash_bytes = hasher.digest()
        
        # Use seed from digest
        seed = int.from_bytes(hash_bytes[:4], byteorder="big")
        rng = np.random.default_rng(seed)
        
        # Draw random values
        vector = rng.standard_normal(self.dimension)
        # Normalize to unit length
        norm = np.linalg.norm(vector)
        if norm > 0:
            vector = vector / norm
            
        return vector.tolist()

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return [self.embed_query(t) for t in texts]


class EmbeddingsManager:
    """Factory manager for initializing different embedding models."""
    
    @staticmethod
    def get_embeddings(provider: str = "mock", api_key: Optional[str] = None) -> BaseEmbeddings:
        provider = provider.lower()
        if provider == "mock":
            return MockEmbeddings()
        elif provider == "openai":
            # Lazy import
            try:
                from openai import OpenAI
                class OpenAIEmbeddings(BaseEmbeddings):
                    def __init__(self, key: Optional[str]):
                        self.client = OpenAI(api_key=key)
                    def embed_query(self, text: str) -> List[float]:
                        resp = self.client.embeddings.create(input=[text], model="text-embedding-3-small")
                        return resp.data[0].embedding
                    def embed_documents(self, texts: List[str]) -> List[List[float]]:
                        resp = self.client.embeddings.create(input=texts, model="text-embedding-3-small")
                        return [item.embedding for item in resp.data]
                return OpenAIEmbeddings(api_key)
            except ImportError:
                logger.error("openai library is missing. Install using: pip install openai")
                raise
        elif provider == "gemini":
            try:
                import google.generativeai as genai
                class GeminiEmbeddings(BaseEmbeddings):
                    def __init__(self, key: Optional[str]):
                        if key:
                            genai.configure(api_key=key)
                    def embed_query(self, text: str) -> List[float]:
                        result = genai.embed_content(
                            model="models/embedding-001",
                            content=text,
                            task_type="retrieval_query"
                        )
                        return result['embedding']
                    def embed_documents(self, texts: List[str]) -> List[List[float]]:
                        result = genai.embed_content(
                            model="models/embedding-001",
                            content=texts,
                            task_type="retrieval_document"
                        )
                        return result['embedding']
                return GeminiEmbeddings(api_key)
            except ImportError:
                logger.error("google-generativeai library is missing. Install using: pip install google-generativeai")
                raise
        else:
            logger.warning(f"Unknown embedding provider: {provider}. Falling back to mock embeddings.")
            return MockEmbeddings()
