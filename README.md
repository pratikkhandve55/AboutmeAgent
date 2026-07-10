# 🤖 Digital Twin AI

An AI-powered **Digital Twin chatbot** that represents my professional profile and answers questions about my **career, skills, projects, and experience**. Built using **Gradio** and the **Google Gemini API (OpenAI-compatible endpoint)**, the chatbot can also collect visitor contact details using AI Function Calling.

---

## 🌐 Live Demo

🚀 **Try it here:**  
https://aboutmeagent-1.onrender.com/

---

## 📸 Screenshots

### 🏠 Home Page

![Home Page](https://raw.githubusercontent.com/pratikkhandve55/AboutmeAgent/main/Screenshots/homescreen.png)

---

### 💬 Chat Interface

![Chat Interface](https://raw.githubusercontent.com/pratikkhandve55/AboutmeAgent/main/Screenshots/interface.png)

---

## 🚀 Features

- 💬 Interactive AI chatbot with a modern Gradio interface
- 🧠 Powered by **Google Gemini 2.5 Flash Lite**
- 📄 Reads LinkedIn profile information from a PDF
- 📝 Uses a custom career summary as context
- 📧 Collects visitor email addresses through AI Function Calling
- 🔔 Sends notifications using the Pushover API
- 🛠️ Supports OpenAI-compatible Tool Calling
- 🌐 Deployable on Render

---

## 🛠️ Tech Stack

- Python 3.12
- Gradio
- Google Gemini API
- OpenAI Python SDK
- PyPDF
- Requests
- Python-dotenv

---

## 📂 Project Structure

```text
AboutmeAgent/
│
├── app.py
├── context.py
├── tools.py
├── style.py
├── summary.txt
├── linkedin.pdf
├── requirements.txt
├── README.md
└── Screenshots/
    ├── homescreen.png
    └── interface.png
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/pratikkhandve55/AboutmeAgent.git
cd AboutmeAgent
```

Create a virtual environment:

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
Gemini_API_KEY=YOUR_GEMINI_API_KEY

PUSHOVER_USER=YOUR_PUSHOVER_USER

PUSHOVER_TOKEN=YOUR_PUSHOVER_TOKEN
```

---

## ▶️ Run the Project

```bash
python app.py
```

or (if using uv)

```bash
uv run app.py
```

---

## ☁️ Deployment

The application is deployed on **Render**.

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
python app.py
```

---

## 📌 How It Works

1. Loads career information from `summary.txt`.
2. Reads LinkedIn profile data from `linkedin.pdf`.
3. Creates a Digital Twin system prompt.
4. Sends conversations to the Gemini API.
5. Uses AI Function Calling to:
   - Record visitor email addresses.
   - Record unanswered questions.
6. Sends notifications through the Pushover API.

---

## 🔮 Future Improvements

- 🧠 Conversation memory
- 🎤 Voice interaction
- 🌍 Multi-language support
- 📄 Resume upload support
- 📊 Admin dashboard for visitor analytics
- 🎨 Additional UI themes

---

## 👨‍💻 Author

**Pratik Bapusaheb Khandve**

- GitHub: https://github.com/pratikkhandve55
- LinkedIn: https://www.linkedin.com/in/pratik-khandve-b2340a300/

---

## ⭐ If you like this project

If you found this project useful, consider giving it a ⭐ on GitHub!
