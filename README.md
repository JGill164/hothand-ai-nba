# 🏀 HotHand AI NBA

> AI-powered NBA analytics platform built for hackathon competition.

🔗 **Live Demo:** [hothand-ai-nba.vercel.app](https://hothand-ai-nba.vercel.app)

---


## Overview

HotHand AI NBA is a full-stack analytics platform that brings the power of artificial intelligence to professional basketball. Built for a hackathon, it goes far beyond traditional box scores — combining a Python-powered backend with a responsive React frontend to deliver real-time insights, predictive analytics, and interactive data visualizations.

The platform is designed to help fans, analysts, and enthusiasts explore NBA data in a smarter way. Whether you're tracking a player's performance over a season, identifying trends across teams, or looking for AI-generated predictions, HotHand puts it all in one place with a clean, fast interface.

The name comes from the "hot hand" phenomenon in basketball — the idea that a player who has made several shots in a row is more likely to make the next one. HotHand AI puts that concept to the test with real data.

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

## Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add my feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request

---
