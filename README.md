# 🏀 HotHand AI NBA

> AI-powered NBA analytics platform built for hackathon competition.

---

## Overview

HotHand AI NBA brings machine learning and real-time analytics to basketball. Built to surface insights, trends, and predictions that go beyond box scores.

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React, Recharts |
| Backend | FastAPI, Python |

---

## Getting Started

### Prerequisites

- Python 3.9+
- Node.js 18+

### Backend

```bash
cd backend
python -m pip install -r requirements.txt
python -m uvicorn main:app --port 8000
```

The API will be available at `http://localhost:8000`.  
Interactive docs at `http://localhost:8000/docs`.

### Frontend

```bash
npm install
npm run dev
```

The app will be available at `http://localhost:5173`.

---

## Project Structure

```
hothand-ai-nba/
├── backend/            # FastAPI server
├── src/                # React frontend source
├── index.html          # App entry point
├── package.json        # Frontend dependencies
└── .gitignore
```

---

## Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add my feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request

---
