# 🤖 Rule-Based AI Chatbot

A simple, beginner-friendly chatbot built entirely with **core Python** —
no AI APIs, no machine learning libraries, no external services. It uses
only `if-elif-else` logic, loops, functions, and dictionaries to hold a
conversation.

The project ships with **two interfaces** that share the exact same
rule-based logic:

- 🖥️ **`chatbot.py`** — a terminal/CLI chatbot
- 🌐 **`streamlit_app.py`** — a web-based chat UI built with Streamlit

---

## 📋 Features

- Runs continuously until the user types `exit`, `quit`, or `bye`
- Recognizes multiple variations of greetings (`hi`, `hello`, `hey`, `good morning`, etc.)
- Answers identity/status questions (`how are you`, `who are you`, `what can you do`, `help`, `thanks`)
- Shares general knowledge facts about `python`, `ai`, `machine learning`, `chatbot`, `programming`
- Handles small talk: jokes, motivation, `good night`, `good luck`
- Gracefully handles unrecognized input with a fallback message
- Normalizes all input using `.lower().strip()` so casing/spacing doesn't matter
- Counts how many messages/questions the user sent during the session
- Stores the entire conversation and displays it (in the terminal at exit, or
  in a collapsible panel in the web app)
- Friendly welcome and goodbye messages
- 20+ predefined responses across multiple categories
- Web version adds: chat bubble UI, sidebar live stats, and a one-click
  **Reset conversation** button

---

## 🛠️ Technologies Used

- **Python 3** (standard library only) for the core logic
- `random` module (built-in) — used only to pick between a few pre-written
  replies, still 100% rule-based (no AI/ML involved)
- **Streamlit** — for the optional web-based chat interface

No other external packages are required.

---

## 📁 Project Structure

```
rule_based_chatbot/
│
├── chatbot.py           # Terminal/CLI chatbot
├── streamlit_app.py      # Web-based chatbot (Streamlit UI)
├── README.md              # Project documentation (this file)
└── screenshots/            # Folder for demo screenshots
```

---

## ▶️ How to Run

### Option 1: Terminal Version (`chatbot.py`)

1. Make sure Python 3 is installed:
   ```bash
   python3 --version
   ```
2. Navigate to the project folder:
   ```bash
   cd rule_based_chatbot
   ```
3. Run the chatbot:
   ```bash
   python3 chatbot.py
   ```
4. Start chatting! Type `exit`, `quit`, or `bye` to end the session.

### Option 2: Web Version (`streamlit_app.py`)

1. Install Streamlit (one-time setup):
   ```bash
   pip install streamlit
   ```
2. Navigate to the project folder:
   ```bash
   cd rule_based_chatbot
   ```
3. Launch the web app:
   ```bash
   streamlit run streamlit_app.py
   ```
4. Your browser will open automatically at `http://localhost:8501`.
5. Chat using the input box at the bottom. Type `exit`, `quit`, or `bye`
   to end the session, or use the **Reset conversation** button in the
   sidebar to start over.

---

## 💬 Sample Conversation (Terminal Version)

```
============================================================
 WELCOME TO THE RULE-BASED AI CHATBOT
============================================================
Type 'exit', 'quit', or 'bye' anytime to end the chat.
Try greetings, questions, or ask about python/ai/chatbot!

You: hello
ChatBot: Hi! Great to see you.
You: what is your name
ChatBot: I'm ChatBot, a simple rule-based chatbot built in Python.
You: python
ChatBot: Python is a popular, beginner-friendly programming language known for its simple, readable syntax.
You: tell me a joke
ChatBot: Why do programmers prefer dark mode? Because light attracts bugs!
You: motivation
ChatBot: You're doing great! Keep pushing forward, one step at a time.
You: asdkjasd
ChatBot: Sorry, I don't understand that. Try asking something else.
You: bye

ChatBot: Goodbye! Thanks for chatting with me. Have a great day!
============================================================
 Total questions asked: 7
============================================================
 CONVERSATION HISTORY
============================================================
1. You : hello
   Bot : Hi! Great to see you.
2. You : what is your name
   Bot : I'm ChatBot, a simple rule-based chatbot built in Python.
3. You : python
   Bot : Python is a popular, beginner-friendly programming language known for its simple, readable syntax.
4. You : tell me a joke
   Bot : Why do programmers prefer dark mode? Because light attracts bugs!
5. You : motivation
   Bot : You're doing great! Keep pushing forward, one step at a time.
6. You : asdkjasd
   Bot : Sorry, I don't understand that. Try asking something else.
7. You : bye
   Bot : Goodbye!
============================================================
```

## 🌐 Sample Conversation (Web Version)

In the Streamlit app, the same exchange appears as chat bubbles:

- **You:** hello → **Bot:** Hi! Great to see you.
- **You:** python → **Bot:** Python is a popular, beginner-friendly programming language known for its simple, readable syntax.
- **You:** bye → **Bot:** Goodbye! Thanks for chatting with me. Have a great day!

The sidebar shows a live **Questions asked** counter, and an expander at
the bottom of the page shows the full conversation history.

---

## 🎓 Learning Outcomes

By building and studying this project, you will understand:

- How to structure a Python project with clean, commented, modular code
- How `if-elif-else` chains are used to implement decision-making logic
- How infinite `while True` loops work and how to break out of them safely
- How to use functions to organize code into reusable, readable blocks
- How to use dictionaries and lists to store and organize data efficiently
- How to normalize and process user input (`.lower().strip()`)
- How to maintain state across a program's runtime (counters, history lists)
- How to reuse the same core logic across two different interfaces (CLI vs. web)
- How Streamlit's `session_state` is used to persist data across reruns
- The foundational logic behind how real chatbots (even AI-powered ones)
  route input to responses — before adding NLP/ML on top

---

## 🚀 Future Improvements

1. **NLP-based intent matching** — use libraries like spaCy or NLTK to handle
   typos, synonyms, and sentence structure instead of exact substring matching.
2. **Machine learning classifier** — train a simple intent classifier (e.g.,
   scikit-learn's Naive Bayes/SVM on labeled example phrases) so the bot
   generalizes beyond hardcoded keywords.
3. **LLM integration** — connect to a model like Claude via the Anthropic API
   for open-ended, context-aware conversation instead of fixed replies.
4. **Persistent memory** — save conversation history to a file or database
   (SQLite/JSON) so the bot remembers users across sessions.
5. **Voice interface** — add speech-to-text input and text-to-speech output
   (e.g., `speech_recognition` + `pyttsx3`) to turn it into a voice assistant.
