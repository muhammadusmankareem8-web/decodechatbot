"""
=====================================================================
 RULE-BASED AI CHATBOT — STREAMLIT WEB APP VERSION
=====================================================================
 Same rule-based logic as chatbot.py (if-elif-else, dictionaries,
 no AI/ML libraries) but with a web-based chat UI powered by
 Streamlit instead of the terminal.

 Run with:
     streamlit run streamlit_app.py
=====================================================================
"""

import random
import streamlit as st


# ---------------------------------------------------------------
# SECTION 1: RESPONSE DICTIONARIES (identical rule-based logic)
# ---------------------------------------------------------------

GREETING_KEYWORDS = ["hi", "hello", "hey", "good morning",
                     "good afternoon", "good evening"]

GREETING_RESPONSES = [
    "Hello there! How can I help you today?",
    "Hi! Great to see you.",
    "Hey! What's on your mind?",
    "Greetings! I'm ready to chat.",
]

GENERAL_KNOWLEDGE_RESPONSES = {
    "python": "Python is a popular, beginner-friendly programming "
              "language known for its simple, readable syntax.",
    "ai": "AI (Artificial Intelligence) is the field of building "
          "machines that can perform tasks that normally need human "
          "intelligence.",
    "machine learning": "Machine Learning is a branch of AI where "
                         "computers learn patterns from data instead "
                         "of being explicitly programmed.",
    "chatbot": "A chatbot is a program that simulates conversation "
               "with users. This one is a simple rule-based chatbot!",
    "programming": "Programming means writing instructions (code) "
                   "that tell a computer exactly what to do.",
}

SMALL_TALK_RESPONSES = {
    "tell me a joke": [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the computer go to therapy? It had too many issues.",
        "I would tell you a UDP joke, but you might not get it.",
    ],
    "motivation": [
        "You're doing great! Keep pushing forward, one step at a time.",
        "Every expert was once a beginner. Keep coding!",
        "Believe in yourself — progress is progress, no matter how small.",
    ],
    "good night": [
        "Good night! Rest well and code more tomorrow.",
        "Sweet dreams! See you in the next session.",
    ],
    "good luck": [
        "Good luck! You've got this.",
        "Wishing you all the best!",
    ],
}

EXIT_KEYWORDS = ["exit", "quit", "bye"]


# ---------------------------------------------------------------
# SECTION 2: HELPER FUNCTIONS
# ---------------------------------------------------------------

def contains_any(user_input, keyword_list):
    """Check whether user_input contains any keyword from keyword_list."""
    for keyword in keyword_list:
        if keyword in user_input:
            return True
    return False


def get_response(user_input):
    """
    Core rule-based logic: takes normalized input and returns a
    reply string using if-elif-else checks, same as the CLI version.
    """

    # ---- Exit words are handled specially in the UI, but we still
    # give a friendly reply if the bot logic is asked directly ----
    if user_input in EXIT_KEYWORDS or "bye" in user_input:
        return "Goodbye! Thanks for chatting with me. Have a great day!"

    # ---- 1. GREETINGS ----
    elif contains_any(user_input, GREETING_KEYWORDS):
        return random.choice(GREETING_RESPONSES)

    # ---- 2. IDENTITY / STATUS QUESTIONS ----
    elif "how are you" in user_input:
        return "I'm just lines of code, but I'm running perfectly. Thanks for asking!"

    elif "who are you" in user_input or "what is your name" in user_input:
        return "I'm ChatBot, a simple rule-based chatbot built in Python."

    elif "what can you do" in user_input or user_input == "help":
        return ("I can greet you, answer basic questions about Python/AI, "
                "tell jokes, give motivation, and chat casually. "
                "Just type something and see!")

    elif "thanks" in user_input or "thank you" in user_input:
        return "You're welcome! Happy to help."

    # ---- 3. GENERAL KNOWLEDGE ----
    elif contains_any(user_input, GENERAL_KNOWLEDGE_RESPONSES.keys()):
        for keyword, fact in GENERAL_KNOWLEDGE_RESPONSES.items():
            if keyword in user_input:
                return fact

    # ---- 4. SMALL TALK ----
    elif contains_any(user_input, SMALL_TALK_RESPONSES.keys()):
        for keyword, replies in SMALL_TALK_RESPONSES.items():
            if keyword in user_input:
                return random.choice(replies)

    # ---- 5. UNKNOWN INPUT ----
    else:
        return "Sorry, I don't understand that. Try asking something else."


# ---------------------------------------------------------------
# SECTION 3: STREAMLIT PAGE CONFIG & SESSION STATE
# ---------------------------------------------------------------
# Streamlit re-runs the whole script on every interaction, so any
# data that must persist (chat history, question count, whether the
# chat has ended) is stored in st.session_state.
# ---------------------------------------------------------------

st.set_page_config(page_title="Rule-Based AI Chatbot", page_icon="🤖")

if "history" not in st.session_state:
    st.session_state.history = []       # list of (role, message) tuples

if "question_count" not in st.session_state:
    st.session_state.question_count = 0

if "chat_ended" not in st.session_state:
    st.session_state.chat_ended = False


# ---------------------------------------------------------------
# SECTION 4: PAGE HEADER
# ---------------------------------------------------------------

st.title("🤖 Rule-Based AI Chatbot")
st.caption(
    "A simple chatbot built with pure Python if-elif-else logic — "
    "no AI APIs or ML models. Type **exit**, **quit**, or **bye** to end the chat."
)

# Sidebar: live stats + reset button
with st.sidebar:
    st.header("📊 Session Stats")
    st.metric("Questions asked", st.session_state.question_count)
    if st.button("🔄 Reset conversation"):
        st.session_state.history = []
        st.session_state.question_count = 0
        st.session_state.chat_ended = False
        st.rerun()


# ---------------------------------------------------------------
# SECTION 5: RENDER EXISTING CHAT HISTORY
# ---------------------------------------------------------------
# Loop through everything stored so far and redraw it as chat
# bubbles (Streamlit re-runs top to bottom on every message).
# ---------------------------------------------------------------

for role, message in st.session_state.history:
    with st.chat_message(role):
        st.write(message)


# ---------------------------------------------------------------
# SECTION 6: CHAT INPUT & RESPONSE LOGIC
# ---------------------------------------------------------------

if st.session_state.chat_ended:
    st.info("The conversation has ended. Click **Reset conversation** in the "
            "sidebar to start a new chat.")
else:
    user_input_raw = st.chat_input("Type your message here...")

    if user_input_raw:
        # Normalize input exactly like the CLI version
        user_input = user_input_raw.lower().strip()

        # Show the user's message immediately
        with st.chat_message("user"):
            st.write(user_input_raw)
        st.session_state.history.append(("user", user_input_raw))
        st.session_state.question_count += 1

        # Get the bot's reply using the same rule-based logic
        bot_reply = get_response(user_input)

        with st.chat_message("assistant"):
            st.write(bot_reply)
        st.session_state.history.append(("assistant", bot_reply))

        # If the user said an exit word, end the chat session
        if user_input in EXIT_KEYWORDS or "bye" in user_input:
            st.session_state.chat_ended = True
            st.rerun()


# ---------------------------------------------------------------
# SECTION 7: CONVERSATION HISTORY EXPANDER (like the CLI printout)
# ---------------------------------------------------------------

with st.expander("📜 View full conversation history"):
    if not st.session_state.history:
        st.write("(No conversation yet.)")
    else:
        for i in range(0, len(st.session_state.history), 2):
            pair = st.session_state.history[i:i + 2]
            for role, msg in pair:
                label = "You" if role == "user" else "Bot"
                st.write(f"**{label}:** {msg}")
