# Production-Grade Legal Knowledge Base & RAG Platform

This repository is a production-ready legal data ingestion, analytics, and Retrieval-Augmented Generation (RAG) platform tailored for eCourts India lawyer profiles and case history records.

It defaults to an **Offline Mock Mode** to facilitate testing, and fully supports live scraping via **Direct HTTP Simulation** or **Stealth Browser Automation (Playwright/Selenium)** when deployed in environment setups that support web drivers.

---

## Key Features

1. **Hybrid Ingestion Layer**: Combines Mock data, HTTP client (with randomized User-Agent/headers, caching, and rate limiting), and dynamic browser engines.
2. **Standardized Parser & Cleaners**: Parses messy HTML profiles and case logs, standardizing names, dates (ISO format YYYY-MM-DD), and courts while maintaining metadata trace details.
3. **Pydantic Validation**: Strong schema enforcement and automatic completeness calculation.
4. **Relational & Analytical Storage**: Implements the Repository Pattern supporting SQLite (for transactional logs), JSON lines (for raw backups), and Apache Parquet (for analytics).
5. **RAG Pipeline**: Semantic chunking, local FAISS vector indexing, and templates directing LLMs (OpenAI, Gemini, Anthropic, Ollama) to answer queries with explicit evidence citations.
6. **Analytics Engine**: Aggregates court presence, judge frequencies, case categories, average disposal times, and classifies outcomes based on evidence.
7. **Advocate Comparison**: Evaluates two advocates side-by-side, benchmarking practice areas, timelines, and generating data confidence metrics.

---

## Project Structure

```text
repo/
│
├── config/             # YAML configuration parser
├── cache/              # Request caching layer (SQLite cache)
├── api_client/         # HTTP client with headers rotation
├── browser/            # Playwright and Selenium managers
├── scraper/            # Ingestion manager (HTTP vs Browser vs Mock)
├── parser/             # BeautifulSoup parser
├── cleaner/            # Normalization utilities (dates, court names, advocates)
├── validator/          # Pydantic schemas and quality validation
├── storage/            # Repository pattern (SQLite, JSON, Parquet)
├── indexing/           # Chunker and document creator
├── embeddings/         # Embedding interface (Gemini, OpenAI, Mock)
├── vectorstore/        # Vector store interface (FAISS)
├── rag/                # RAG pipeline with context window packing
├── analytics/          # Statistics, outcome classification
├── comparison/         # Multi-advocate comparison and scoring
├── llm/                # LLM client abstractions (Ollama, OpenAI, Claude, Gemini)
├── monitoring/         # Metrics, logging, progress tracker
├── scheduler/          # Scheduler daemon for periodic updates
├── tests/              # Unit and integration tests
├── run.py              # CLI entrypoint
└── requirements.txt    # Python dependencies
```

---

## Installation & Setup

### Prerequisites
- Python 3.10+
- (Optional) Astral `uv` for ultra-fast, self-contained Python environments.

### 1. Install Dependencies
```bash
# Using standard virtual environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Or using Astral uv (Recommended)
uv venv --python 3.11
uv pip install -r requirements.txt
```

### 2. Configuration
Modify `config/config.yaml` to configure crawling targets, modes, database paths, and LLM credentials:
- **`crawler.mode`**: Set to `"mock"` for offline verification, or `"http"` / `"browser"` for live extraction.
- **`rag.llm_provider`**: Set to `"mock"` for offline QA, or `"gemini"`, `"openai"`, `"ollama"`.

---

## Example Workflows (Command CLI)

All workflows are coordinated through the main command CLI `run.py`.

### 1. Crawl & Ingest Advocate Case History
Fetches profile information, scrapes case logs, sanitizes inputs, writes files, and indexes context into FAISS:
```bash
# Crawl the default target (Kuchi Rajeswara Sastry) in mock mode
python run.py crawl --mode mock

# Ingest John Doe's profile
python run.py crawl --advocate john-doe --mode mock
```

### 2. Generate Analytics Dashboard
Computes aggregate metrics, timelines, judge distribution, and evidence-backed outcomes:
```bash
python run.py analytics --advocate kuchi-rajeswara-sastry
```

### 3. Compare Two Advocates
Standardizes comparative volumes, practice specialties, average timelines, and confidence scores:
```bash
python run.py compare --advocates "kuchi-rajeswara-sastry,john-doe"
```

### 4. Query RAG System
Search matching database chunks and query the LLM for evidence-backed answers:
```bash
python run.py ask --query "How many disposed cases did Kuchi Rajeswara Sastry handle?"
```

### 5. Start Scheduled Crawler Daemon
Trigger automatic incremental updates and log metrics periodically:
```bash
python run.py scheduler --interval 60
```

---

## Running Tests
Run the test suite using pytest to verify parser, cleaner, database, analytics, and RAG operations:
```bash
python -m pytest tests/
```
