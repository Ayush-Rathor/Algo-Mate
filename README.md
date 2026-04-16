<div align="center">

# 🚀 AlgoMate

### *Master DSA. Code Smarter. Interview Ready.*

**AlgoMate** is a full-stack **Data Structures & Algorithms learning platform** that brings together structured notes, a live code compiler, and an AI-powered assistant — all in one place.

[![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://reactjs.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)

</div>

---

## ✨ Features

| Feature | Description |
|---|---|
| 📘 **DSA Notes** | Topic-wise structured content covering Arrays, Linked Lists, Trees, Stacks, Recursion, Sorting & more |
| 💻 **Online Compiler** | Run code directly in the browser with multi-language support via Judge0 API |
| 🤖 **AI Chatbot** | Powered by Gemini API — get instant explanations and help with coding doubts |
| 🎨 **Modern UI** | Clean, responsive interface built with React + Tailwind CSS |

---

## 🏗️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | React, Tailwind CSS |
| **Backend** | Flask (Python) |
| **AI** | Gemini API |
| **Compiler** | Judge0 via RapidAPI |

---

## 📂 Project Structure

```
AlgoMate/
├── backend/        # Flask API — chatbot & compiler endpoints
├── frontend/       # React application
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/AlgoMate.git
cd AlgoMate
```

---

### 2. Backend Setup

```bash
cd backend
```

**Create and activate a virtual environment:**

```bash
python3 -m venv venv
source venv/bin/activate        # macOS/Linux
# venv\Scripts\activate         # Windows
```

**Install dependencies:**

```bash
pip install -r requirements.txt
```

**Create a `.env` file in the `backend/` directory:**

```env
GEMINI_API_KEY=your_gemini_api_key
JUDGE0_API_KEY=your_rapidapi_key
GEMINI_MODEL=gemini-2.5-flash
```

**Start the backend server:**

```bash
python app.py
```

> 🟢 Backend runs at: `http://localhost:5000`

---

### 3. Frontend Setup

Open a **new terminal** and run:

```bash
cd frontend
npm install
```

**Create a `.env` file in the `frontend/` directory:**

```env
REACT_APP_BACKEND_URL=http://localhost:5000
```

**Start the frontend:**

```bash
npm start
```

> 🟢 Frontend runs at: `http://localhost:3000`

---

## 🔑 API Keys

### 🤖 Gemini API Key
- Get it from: [https://ai.google.dev/](https://ai.google.dev/)
- Used for: AI chatbot functionality

### 💻 Judge0 API Key (RapidAPI)
- Get it from: [RapidAPI — Judge0 CE](https://rapidapi.com/judge0-official/api/judge0-ce)
- Used for: In-browser code compilation
- Required headers:
  - `X-RapidAPI-Key`: your key
  - `X-RapidAPI-Host`: `judge0-ce.p.rapidapi.com`

---

## 🧪 Usage

1. Visit `http://localhost:3000`
2. Explore the three core sections:
   - 📘 **Notes** — Browse topic-wise DSA content
   - 💻 **Compiler** — Write and run code in the browser
   - 🤖 **Chatbot** — Ask coding questions powered by Gemini

---

## 📄 Environment File Examples

**`backend/.env.example`**
```env
GEMINI_API_KEY=your_key
JUDGE0_API_KEY=your_key
GEMINI_MODEL=gemini-2.5-flash
```

**`frontend/.env.example`**
```env
REACT_APP_BACKEND_URL=http://localhost:5000
```

---

## 🚀 Deployment

| Layer | Recommended Platforms |
|---|---|
| **Backend** | Render, Railway, AWS EC2 |
| **Frontend** | Vercel, Netlify |

After deploying the backend, update your frontend environment variable:

```env
REACT_APP_BACKEND_URL=https://your-backend-url.com
```

---

## ⚠️ Security Notes

- **Never commit `.env` files** to version control — add them to `.gitignore`
- Frontend environment variables are **exposed in the browser** — never store secrets there
- All API keys should be handled **server-side** through the Flask backend

---

<div align="center">

Built with ❤️ for students, developers, and interview preparation

</div>
