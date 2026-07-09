# 🚀 Permind AI

> **An AI-powered Interview Preparation Assistant leveraging Retrieval-Augmented Generation (RAG), Semantic Search, FAISS, FastAPI, Streamlit, and Gemini AI.**

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![FAISS](https://img.shields.io/badge/FAISS-Vector_Search-orange)
![Gemini](https://img.shields.io/badge/Gemini-AI-blueviolet)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 📌 Overview

Permind AI is an intelligent interview preparation platform designed to help students and job seekers prepare for technical and HR interviews using Artificial Intelligence.

The system combines semantic search, Retrieval-Augmented Generation (RAG), and Google's Gemini model to retrieve relevant interview questions, generate high-quality answers, and provide an interactive interview preparation experience.

Unlike traditional interview question repositories, Permind AI understands the user's query semantically and retrieves the most relevant interview knowledge before generating AI-assisted responses.

---

# ✨ Features

- 📚 Multi-source interview dataset collection
- 🔍 Semantic Search using Sentence Transformers
- 🧠 Retrieval-Augmented Generation (RAG)
- ⚡ FastAPI backend
- 🎨 Streamlit frontend
- 📊 Exploratory Data Analysis (EDA)
- 🧹 Automated dataset preprocessing
- 📝 Dataset validation and standardization
- 📈 Retrieval evaluation reports
- 🤖 Gemini AI integration
- 📂 Modular project architecture
- 🚀 Deployment-ready project structure

---

# 🛠 Tech Stack

### Programming Language

- Python

### Backend

- FastAPI

### Frontend

- Streamlit

### AI / Machine Learning

- Sentence Transformers
- FAISS
- TF-IDF
- RAG
- Gemini API

### Data Processing

- Pandas
- NumPy

### Visualization

- Matplotlib
- Seaborn

### Development Tools

- Git
- GitHub
- VS Code

---

# 📁 Project Structure

```
permind-ai/

├── datasets/
│   ├── raw/
│   ├── processed/
│   ├── merged/
│   ├── final/
│   └── features/
│
├── docs/
│
├── models/
│
├── notebooks/
│
├── reports/
│
├── src/
│   ├── api/
│   ├── eda/
│   ├── evaluation/
│   ├── feature_engineering/
│   ├── modeling/
│   ├── preprocessing/
│   ├── rag/
│   ├── retrieval/
│   ├── standardization/
│   └── ui/
│
├── requirements.txt
└── README.md
```

---

# 📂 Dataset Pipeline

The project follows a structured data engineering workflow:

1. Data Collection
2. Dataset Validation
3. Dataset Cleaning
4. Standardization
5. Data Preprocessing
6. Exploratory Data Analysis
7. Feature Engineering
8. Semantic Search
9. RAG Pipeline
10. Evaluation

---

# 📊 Dataset Sources

Interview datasets were collected from multiple sources including:

- Hugging Face
- Kaggle
- Custom datasets

The datasets include:

- Technical Interviews
- HR Interviews
- AI Interviews
- Programming Interviews
- Software Engineering Interviews
- Resume & Job Description Matching

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/subhra12-commits/permind-ai.git
```

Move into the project directory

```bash
cd permind-ai
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

### Start the FastAPI backend

```bash
uvicorn src.api.main:app --reload
```

FastAPI Docs

```
http://127.0.0.1:8000/docs
```

---

### Start the Streamlit frontend

```bash
streamlit run src/ui/app.py
```

---

# 🌐 API

Current APIs include:

- Health Check
- Semantic Search
- Interview Question Retrieval
- RAG Response Generation

Additional endpoints will be added in future versions.

---

# 📊 Evaluation

The project evaluates:

- Retrieval Accuracy
- RAG Quality
- Search Latency
- Semantic Similarity

Evaluation reports are stored in

```
reports/evaluation/
```

---

# 📈 Current Project Progress

| Phase | Status |
|---------|--------|
| Data Collection | ✅ |
| Data Validation | ✅ |
| Data Cleaning | ✅ |
| Exploratory Data Analysis | ✅ |
| Data Preprocessing | ✅ |
| Feature Engineering | ✅ |
| Semantic Search | ✅ |
| RAG Pipeline | ✅ |
| FastAPI Backend | ✅ |
| Streamlit UI | ✅ |
| Evaluation | ✅ |
| Deployment | 🚧 In Progress |

---

# 🚀 Future Improvements

- User authentication
- Resume parsing
- AI interview scoring
- Voice interview simulation
- Personalized feedback
- Dashboard analytics
- Docker deployment
- Cloud deployment (AWS / Azure / GCP)
- CI/CD pipeline
- Multi-language interview support

---

# 🤝 Contributing

Contributions are welcome.

If you'd like to contribute:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push your branch
5. Open a Pull Request

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Subhradeep Saha**

B.Tech Computer Science (Artificial Intelligence & Machine Learning)

- GitHub: https://github.com/subhra12-commits
- LinkedIn: *(Add your LinkedIn profile URL)*
- Email: *(Add your professional email)*

---

⭐ If you found this project useful, consider giving it a star!
