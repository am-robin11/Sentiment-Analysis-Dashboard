# 🧠 Sentiment Analysis Dashboard

A real-time sentiment analysis web app built with **FastAPI** and **HuggingFace DistilBERT** — featuring a live dashboard with confidence scores, trend chart, and batch analysis mode.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green)
![HuggingFace](https://img.shields.io/badge/HuggingFace-DistilBERT-yellow)

---

## 🚀 Features

- **Real-time analysis** — type text and get instant sentiment + confidence score
- **Batch mode** — paste multiple texts (one per line) and analyze all at once
- **Live dashboard** — doughnut chart updates as you analyze
- **History log** — scrollable list of all analyzed texts with color-coded badges
- **REST API** — documented endpoints via FastAPI's built-in Swagger UI at `/docs`

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | FastAPI + Uvicorn |
| ML Model | HuggingFace Transformers (DistilBERT) |
| Frontend | Vanilla JS + Chart.js |
| Templating | Jinja2 |

---

## 📦 Installation & Setup

```bash
# Clone the repo
git clone https://github.com/am-robin11/Sentiment-Analysis-Dashboard.git
cd Sentiment-Analysis-Dashboard

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run the app
python main.py
```

Then open your browser at `http://localhost:8000`

> **Note:** The first run will download the DistilBERT model (~268MB). This happens once and is cached automatically.

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Serves the dashboard UI |
| POST | `/analyze` | Analyze a single text |
| POST | `/analyze/batch` | Analyze multiple texts at once |

Full interactive docs available at `http://localhost:8000/docs`

### Example Request

```bash
curl -X POST "http://localhost:8000/analyze" \
  -H "Content-Type: application/json" \
  -d '{"text": "This is absolutely amazing!"}'
```

### Example Response

```json
{
  "label": "POSITIVE",
  "score": 0.9998,
  "text": "This is absolutely amazing!"
}
```

---

## 📸 Screenshots

### Mostly Positive Results
![Mostly Positive](screenshot1.png)

### Mixed Results
![Mixed Results](screenshot2.png)
---

## 🧠 Model Info

This project uses **distilbert-base-uncased-finetuned-sst-2-english** from HuggingFace — a lightweight, fast version of BERT fine-tuned on the Stanford Sentiment Treebank (SST-2) dataset.

- 40% smaller than BERT-base
- 60% faster inference
- Retains 97% of BERT's performance on sentiment tasks
- Runs entirely on CPU — no GPU required

---

## 📄 License

MIT