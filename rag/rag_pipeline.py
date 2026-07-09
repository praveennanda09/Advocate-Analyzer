import logging
from typing import Dict, Any, List
from vectorstore.store import FAISSStore
from llm.llm_client import BaseLLMClient

logger = logging.getLogger(__name__)

RAG_PROMPT_TEMPLATE = """You are a professional legal AI assistant. Your goal is to answer the user's question accurately using only the retrieved context below.

Rules:
1. Every statement you make must be directly backed by the provided context.
2. If the context contains a case status, CNR number, judge, or dates, always cite them.
3. NEVER make up wins, losses, or final legal outcomes. If the outcome is not stated, say "Unknown Outcome".
4. Cite the specific CNR numbers and court names as the source of your information.
5. If the context does not contain enough information to answer the question, state that clearly and do not fabricate an answer.

Context:
{context}

Question:
{question}

Answer:"""

class RAGPipeline:
    """Orchestrates document retrieval and LLM context packing to execute RAG queries."""
    
    def __init__(self, vector_store: FAISSStore, llm_client: BaseLLMClient):
        self.vector_store = vector_store
        self.llm_client = llm_client

    def answer_query(self, query: str, k: int = 4) -> Dict[str, Any]:
        """Perform semantic search, format context, and generate a backed answer."""
        logger.info(f"RAG Query: '{query}'")
        
        # 1. Retrieve relevant chunks
        results = self.vector_store.similarity_search(query, k=k)
        
        # 2. Format context
        context_blocks = []
        sources = []
        
        for idx, (doc, score) in enumerate(results, 1):
            text = doc["text"]
            meta = doc["metadata"]
            cnr = meta.get("cnr", "Unknown CNR")
            case_num = meta.get("case_number", "Unknown Case")
            
            block = f"[Chunk {idx}] (Source Case: {case_num}, CNR: {cnr})\n{text}"
            context_blocks.append(block)
            
            sources.append({
                "cnr": cnr,
                "case_number": case_num,
                "score": score
            })
            
        context_str = "\n\n".join(context_blocks)
        
        if not context_str:
            context_str = "[No context found in vector store]"
            
        # 3. Assemble prompt
        prompt = RAG_PROMPT_TEMPLATE.format(context=context_str, question=query)
        
        # 4. Generate answer
        answer = self.llm_client.generate(prompt)
        
        return {
            "query": query,
            "answer": answer,
            "sources": sources,
            "context_used": context_str
        }
