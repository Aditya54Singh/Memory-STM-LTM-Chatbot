# 🧠 LangGraph STM/LTM Memory Chatbot

> A terminal-based AI chatbot built with **LangGraph** that demonstrates how Large Language Models can maintain both **Short-Term Memory (STM)** and **Long-Term Memory (LTM)** across conversations. The project showcases persistent memory, semantic retrieval, and intelligent memory management using LangGraph's checkpointing and storage capabilities.

---

## 📖 Overview

Most LLM-powered chatbots are stateless. Once the conversation exceeds the model's context window or the application restarts, the chatbot forgets everything about the user.

This project addresses that limitation by implementing a **dual-memory architecture**, inspired by how humans process information:

* **Short-Term Memory (STM)** retains the current conversation context.
* **Long-Term Memory (LTM)** stores meaningful user information that should persist across sessions.

During every interaction, the chatbot retrieves relevant long-term memories, combines them with the ongoing conversation, and generates responses that remain personalized even after restarting the application.

The project is designed as a **proof of concept for persistent AI memory systems**, focusing on architecture and workflow rather than frontend development.

---

# ✨ Features

* 🧠 Human-inspired dual-memory architecture
* 💬 Persistent conversations across sessions
* 📚 Semantic retrieval of long-term memories
* 🔄 Automatic memory extraction
* 🚫 Duplicate memory detection
* ⚖️ Memory conflict resolution
* 🧩 LangGraph workflow orchestration
* 🗄️ PostgreSQL-backed persistent storage
* 💻 Interactive terminal-based chatbot
* 🏗️ Modular and extensible project structure

---

# 🎯 Objectives

This project was built to explore how conversational AI systems can:

* Maintain context during a conversation
* Remember important user information across sessions
* Retrieve only relevant memories when needed
* Avoid storing unnecessary information
* Mimic human-like memory behavior using LangGraph

---

# 🛠️ Tech Stack

| Category          | Technology              |
| ----------------- | ----------------------- |
| Language          | Python                  |
| AI Framework      | LangGraph               |
| LLM Framework     | LangChain               |
| LLM               | Groq                    |
| Short-Term Memory | LangGraph PostgresSaver |
| Long-Term Memory  | LangGraph PostgresStore |
| Database          | PostgreSQL              |

---

# 🏗️ Architecture

```text
                    User
                      │
                      ▼
             Terminal Interface
                      │
                      ▼
               LangGraph Workflow
                      │
      ┌───────────────┴───────────────┐
      │                               │
      ▼                               ▼
Short-Term Memory             Long-Term Memory
(PostgresSaver)               (PostgresStore)
      │                               │
      └───────────────┬───────────────┘
                      ▼
              Prompt Construction
                      │
                      ▼
                  Groq LLM
                      │
                      ▼
             Generated Response
                      │
                      ▼
              Memory Extraction
                      │
      ┌───────────────┴───────────────┐
      │                               │
Duplicate Detection          Conflict Resolution
      │                               │
      └───────────────┬───────────────┘
                      ▼
            Store New Long-Term Memory
```

---

# 🧠 Memory Design

## Short-Term Memory (STM)

Short-Term Memory maintains the active conversation.

It is implemented using **LangGraph PostgresSaver**, which automatically checkpoints conversation state.

Responsibilities:

* Current conversation history
* Multi-turn reasoning
* Conversation continuity
* Temporary conversational context

STM exists only to support the current interaction and is continuously updated as the conversation progresses.

---

## Long-Term Memory (LTM)

Long-Term Memory stores information that remains useful across future conversations.

Examples include:

* User preferences
* Personal goals
* Skills and interests
* Ongoing projects
* Career aspirations
* Frequently used technologies

Unlike STM, Long-Term Memory persists even after the chatbot is restarted.

---

# 🔄 Workflow

Every conversation follows the same sequence:

### Step 1

The user enters a message through the terminal.

↓

### Step 2

LangGraph restores the latest conversation checkpoint from Short-Term Memory.

↓

### Step 3

Relevant memories are retrieved from Long-Term Memory using semantic search.

↓

### Step 4

The chatbot combines:

* Current conversation context
* Retrieved memories
* User query

into a single prompt.

↓

### Step 5

The prompt is sent to the Groq LLM.

↓

### Step 6

The generated response is displayed to the user.

↓

### Step 7

The conversation is analyzed to determine whether any important information should be stored permanently.

↓

### Step 8

Duplicate and conflicting memories are handled before storing new information.

---

# 🧩 Memory Extraction

A key challenge in persistent AI systems is deciding **what should actually be remembered**.

Instead of storing every conversation, the chatbot selectively saves only meaningful information.

### Stored Examples

```text
I prefer Python.

I am preparing for backend interviews.

I enjoy learning FastAPI.

I recently started a Hybrid RAG project.
```

### Ignored Examples

```text
Hello

Thank you

Tell me a joke

What's the weather today?
```

This selective approach prevents Long-Term Memory from becoming noisy and improves retrieval quality.

---

# 🚫 Duplicate Detection

Before saving a new memory, the chatbot checks whether similar information already exists.

### Existing Memory

```text
User prefers Python.
```

### Incoming Memory

```text
Python is my favorite programming language.
```

Instead of storing duplicate information, the chatbot recognizes the similarity and avoids redundant entries.

---

# ⚖️ Conflict Resolution

The chatbot also handles situations where newly extracted information contradicts previously stored memories.

### Existing Memory

```text
User lives in Delhi.
```

### New Memory

```text
I recently moved to Bangalore.
```

The outdated memory is replaced with the latest valid information, ensuring the chatbot always works with up-to-date knowledge.

---

# 📂 Project Structure

```text
memory-chatbot/
│
├── app/
│   │
│   ├── config.py                 # Application configuration
│   ├── graph.py                  # LangGraph workflow definition
│   ├── state.py                  # Shared graph state
│   │
│   ├── database/
│   │   ├── connection.py         # PostgreSQL connection
│   │   └── embeddings.py         # Embedding store configuration
│   │
│   ├── llm/
│   │   └── ...                   # Groq LLM initialization
│   │
│   ├── models/
│   │   └── memory.py             # Memory data models
│   │
│   ├── nodes/
│   │   └── ...                   # LangGraph nodes
│   │
│   ├── prompts/
│   │   ├── chatbot.py            # Chatbot prompts
│   │   └── memory.py             # Memory extraction prompts
│   │
│   ├── services/
│   │   ├── retrieval.py          # Long-term memory retrieval
│   │   ├── memory_service.py     # Memory management
│   │   ├── deduplication.py      # Duplicate memory detection
│   │   └── updater.py            # Memory update & conflict resolution
│   │
│   ├── utils/
│   │   └── ...                   # Helper utilities
│   │
│   └── __init__.py
│
├── main.py                       # Entry point
├── requirements.txt
├── .env
├── README.md
└── .gitignore
```

> **Note:** File names may vary depending on your implementation. The project follows a modular structure separating workflow, memory management, configuration, and utilities.

---

# 🚀 Getting Started

## Clone the repository

```bash
git clone https://github.com/your-username/langgraph-memory-chatbot.git

cd langgraph-memory-chatbot
```

---

## Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment.

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configure environment variables

Create a `.env` file.

```env
GROQ_API_KEY=your_api_key

DATABASE_URL=your_postgresql_connection_string
```

---

## Run the chatbot

```bash
python chatbot.py
```

---

# 💬 Example Conversation

```text
You:
Hi! My name is Aditya.

AI:
Hello Aditya! Nice to meet you.

--------------------------------------

You:
I am preparing for backend interviews.

AI:
Got it. I'll remember that you're preparing for backend interviews.

--------------------------------------

(Restart the chatbot)

--------------------------------------

You:
What should I study today?

AI:
Since you're preparing for backend interviews, I'd recommend revising FastAPI, SQLAlchemy, and system design concepts.
```

This demonstrates that the chatbot successfully retrieves relevant information from Long-Term Memory even after restarting the application.

---

# 📚 What I Learned

Through this project, I gained practical experience with:

* LangGraph workflow orchestration
* Persistent conversational memory
* Short-Term vs Long-Term Memory design
* Semantic memory retrieval
* Prompt engineering with contextual memories
* PostgreSQL integration
* AI system architecture
* Building modular Python applications

---

# 🔮 Future Improvements

* Memory importance scoring
* Automatic memory aging and pruning
* Memory editing and deletion
* Multi-user support
* Memory visualization dashboard
* Docker containerization
* Unit and integration tests
* LLM evaluation metrics

---

# 🤝 Acknowledgements

This project was built as a learning exercise to understand how modern conversational AI systems can implement persistent memory using **LangGraph**, **PostgreSQL**, and **Large Language Models**. It focuses on the architectural concepts behind memory-enabled AI assistants rather than user interface development.

---

## ⭐ If you found this project interesting, consider giving it a star!
