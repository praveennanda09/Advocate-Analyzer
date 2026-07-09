import json
import logging
from typing import Optional
import httpx

logger = logging.getLogger(__name__)

class BaseLLMClient:
    """Unified interface for LLM operations."""
    def generate(self, prompt: str) -> str:
        raise NotImplementedError()

class MockLLMClient(BaseLLMClient):
    """Answers questions based on keyword analysis of the prompt, mimicking a legal model."""
    
    def generate(self, prompt: str) -> str:
        prompt_lower = prompt.lower()
        
        # Extract context if present in prompt to produce a realistic response
        context_segment = ""
        if "context:" in prompt_lower:
            parts = prompt.split("Context:")
            if len(parts) > 1:
                context_segment = parts[1].split("Question:")[0].strip()
                
        # Simple heuristic response based on context keywords
        if "kuchi rajeswara sastry" in prompt_lower or "sastry" in prompt_lower:
            if "compare" in prompt_lower or "comparison" in prompt_lower:
                return (
                    "[LLM response (Mock Mode)]\n"
                    "Comparing Kuchi Rajeswara Sastry with John Doe based on eCourts data:\n"
                    "- Kuchi Rajeswara Sastry has a longer practice history starting in 1971, with 3 total cases (2 disposed, 1 pending) in Amalapuram Senior/Junior Civil Courts and the Andhra Pradesh High Court.\n"
                    "- John Doe has a profile registered in 1995, with 1 case (disposed) in Mumbai District Court.\n"
                    "- Confidence levels: Sastry (92.0% due to full case details), Doe (65.0% due to small case sample).\n"
                    "Sources: eCourts India, Profile AP/1042/1971 & Profile MH/2045/1995."
                )
            elif "how many cases" in prompt_lower or "count" in prompt_lower or "volume" in prompt_lower:
                return (
                    "[LLM response (Mock Mode)]\n"
                    "According to eCourts India records, Kuchi Rajeswara Sastry has handled 3 cases:\n"
                    "- 2 Disposed cases (O.S. 104/2021 and W.P. 5678/1974)\n"
                    "- 1 Pending case (O.S. 45/2022)\n"
                    "Sources: Senior Civil Court Amalapuram, Junior Civil Court Amalapuram, Andhra Pradesh High Court."
                )
            elif "outcome" in prompt_lower or "disposed" in prompt_lower:
                return (
                    "[LLM response (Mock Mode)]\n"
                    "Of Kuchi Rajeswara Sastry's 2 disposed matters:\n"
                    "1. Case O.S. 104/2021 (Allowed/Decreed): The partition suit was decreed on 2023-10-12 by Judge Sri K. Sree Rama Murthy.\n"
                    "2. Case W.P. 5678/1974 (Allowed/Quashed): The Writ Petition was allowed on 1976-11-22, quashing the sales tax assessment on market fees.\n"
                    "Sources: Senior Civil Court Amalapuram, High Court of Andhra Pradesh."
                )
            else:
                return (
                    "[LLM response (Mock Mode)]\n"
                    "Advocate Kuchi Rajeswara Sastry (Reg No: AP/1042/1971) practices primarily in East Godavari, Andhra Pradesh (Amalapuram Courts).\n"
                    "His case history includes civil partition suits (O.S.) and historical commercial tax writ petitions (W.P.).\n"
                    "Critical Cases:\n"
                    "- O.S. 104/2021: Garapati Venkata Nagendra Prasad Vs. Garapati Venkta Ramakrishna Rao (Disposed)\n"
                    "- O.S. 45/2022: Konda Surya Rao Vs. Konda Naga Lakshmi (Pending)\n"
                    "- W.P. 5678/1974: Krishna Coconut Company Vs. Market Committee (Disposed)\n"
                    "Sources: eCourts India advocate profiles."
                )
        
        # General response if no specific matched keyword
        if context_segment:
            return (
                "[LLM response (Mock Mode)]\n"
                f"Using the provided retrieved context, the answer is: The records show details matching your query.\n"
                f"Context snippet: {context_segment[:150]}..."
            )
            
        return "[LLM response (Mock Mode)] No advocate records found matching the prompt in current workspace."


class LLMClientManager:
    """Factory manager for initializing different LLM backends."""
    
    @staticmethod
    def get_client(provider: str = "mock", model_name: str = "gemini-1.5-flash", api_key: Optional[str] = None, temperature: float = 0.2) -> BaseLLMClient:
        provider = provider.lower()
        if provider == "mock":
            return MockLLMClient()
        elif provider == "gemini":
            try:
                import google.generativeai as genai
                class GeminiClient(BaseLLMClient):
                    def __init__(self, key: Optional[str], model: str, temp: float):
                        if key:
                            genai.configure(api_key=key)
                        self.model = genai.GenerativeModel(
                            model,
                            generation_config={"temperature": temp}
                        )
                    def generate(self, prompt: str) -> str:
                        resp = self.model.generate_content(prompt)
                        return resp.text
                return GeminiClient(api_key, model_name, temperature)
            except ImportError:
                logger.error("google-generativeai is missing.")
                raise
        elif provider == "openai":
            try:
                from openai import OpenAI
                class OpenAIClient(BaseLLMClient):
                    def __init__(self, key: Optional[str], model: str, temp: float):
                        self.client = OpenAI(api_key=key)
                        self.model = model
                        self.temp = temp
                    def generate(self, prompt: str) -> str:
                        resp = self.client.chat.completions.create(
                            model=self.model,
                            messages=[{"role": "user", "content": prompt}],
                            temperature=self.temp
                        )
                        return resp.choices[0].message.content or ""
                return OpenAIClient(api_key, model_name, temperature)
            except ImportError:
                logger.error("openai library is missing.")
                raise
        elif provider == "ollama":
            class OllamaClient(BaseLLMClient):
                def __init__(self, model: str, temp: float):
                    self.model = model
                    self.temp = temp
                    self.url = "http://localhost:11434/api/generate"
                def generate(self, prompt: str) -> str:
                    try:
                        payload = {
                            "model": self.model,
                            "prompt": prompt,
                            "stream": False,
                            "options": {"temperature": self.temp}
                        }
                        r = httpx.post(self.url, json=payload, timeout=60)
                        r.raise_for_status()
                        return r.json().get("response", "")
                    except Exception as e:
                        return f"Ollama connection error: {e}"
            return OllamaClient(model_name, temperature)
        else:
            logger.warning(f"Unknown LLM provider: {provider}. Defaulting to mock.")
            return MockLLMClient()
