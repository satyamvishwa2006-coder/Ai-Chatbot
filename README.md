🤖 AI Chatbot

A beginner-friendly AI chatbot built with Python, FastAPI, React, and NLP.

This project combines a Python-based chatbot backend with a modern React frontend to provide an interactive chat experience. The project is designed as a foundation that can be extended with AI APIs, web search, RAG, document processing, and multimodal capabilities.

✨ Features

- 💬 Interactive chatbot
- 🧠 NLP-based intent recognition
- ⚡ FastAPI backend
- ⚛️ React + Vite frontend
- 🔄 Frontend ↔ Backend API communication
- 🌐 CORS enabled
- 📦 Python virtual environment support
- 🔒 ".gitignore" configured to protect unnecessary files
- 🧩 Modular project structure
- 🚀 Ready for further AI/API integration

🛠️ Tech Stack

Frontend

- React
- Vite
- JavaScript
- CSS

Backend

- Python
- FastAPI
- Uvicorn
- NLTK
- PyTorch

Development Tools

- VS Code
- Git
- GitHub

📁 Project Structure

Ai-Chatbot/
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── app.py
├── chat.py
├── model.py
├── train.py
├── nltk_utils.py
├── intents.json
├── data.pth
├── requirements.txt
├── .gitignore
└── README.md

⚙️ Installation

1. Clone the repository

git clone https://github.com/satyamvishwa2006-coder/Ai-Chatbot.git
cd Ai-Chatbot

2. Create a virtual environment

python -m venv venv

3. Activate the virtual environment

Windows PowerShell:

venv\Scripts\Activate.ps1

4. Install Python dependencies

pip install -r requirements.txt

🚀 Run the Backend

Start the FastAPI server:

uvicorn app:app --reload

The backend will run at:

http://127.0.0.1:8000

API documentation:

http://127.0.0.1:8000/docs

🎨 Run the Frontend

Open another terminal:

cd frontend
npm install
npm run dev

The frontend will normally be available at:

http://localhost:5173

🔌 API

Health Check

GET /

Example response:

{
  "message": "MyChatbot API is running!"
}

Chat

POST /chat

Example request:

{
  "message": "Hello"
}

The API processes the message and returns the chatbot's response.

🧠 How It Works

The chatbot follows a simple NLP-based architecture:

User
  ↓
React Frontend
  ↓
FastAPI Backend
  ↓
NLP Processing
  ↓
Intent Classification Model
  ↓
Response Selection
  ↓
FastAPI
  ↓
React UI
  ↓
User

The model is trained using the intents defined in "intents.json".

📚 Training the Model

If you modify "intents.json", retrain the chatbot model using:

python train.py

This generates the trained model file:

data.pth

🔐 Environment Variables

When adding external AI APIs, never upload API keys directly to GitHub.

Use a ".env" file:

OPENAI_API_KEY=your_api_key_here

And keep ".env" inside ".gitignore".

🚧 Future Improvements

The project is currently being developed and can be extended with:

- [ ] OpenAI API integration
- [ ] Google Gemini integration
- [ ] Hugging Face models
- [ ] Chat history
- [ ] Web search
- [ ] RAG architecture
- [ ] PDF/document upload
- [ ] Document question answering
- [ ] Image input
- [ ] Multimodal responses
- [ ] Voice input and output
- [ ] Improved UI/UX
- [ ] Streaming AI responses
- [ ] Deployment

🎯 Project Goal

The goal of this project is to gradually transform a basic NLP chatbot into a more capable AI-powered multimodal chatbot with modern AI technologies such as LLMs, RAG, web search, and document processing.

👨‍💻 Author

Satyam Vishwakarma

GitHub:
https://github.com/satyamvishwa2006-coder

---

⭐ If you find this project useful, consider giving the repository a star!
