import streamlit as st
from agent import process_message
from database import appointments

st.set_page_config(page_title="HealthCare Booking Agent 🤖", layout="wide")
st.title("🏥 Agentic AI — Appointment Assistant Bot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("💬 Talk to your AI Assistant:", "", key="input")

if user_input:
    response = process_message(user_input)
    st.session_state.chat_history.append((user_input, response))

# Chat history display
for user_text, bot_reply in reversed(st.session_state.chat_history):
    st.markdown(f"🧑‍💬 **You:** {user_text}")
    st.markdown(f"🤖 **Bot:** {bot_reply}")

# Appointments display
st.markdown("## 📅 Booked Appointments")
for i, appt in enumerate(appointments):
    st.write(f"{i+1}. Time: {appt['time']} | Status: {appt['status']}")
