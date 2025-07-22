from database import appointments
from datetime import datetime
import openai
import os

# Instantiate OpenAI client (use Streamlit secret automatically)
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def process_message(user_input: str) -> str:
    prompt = f"""
You are a smart hospital assistant. Help the patient book, cancel, or reschedule an appointment.
Current Appointments: {appointments}

Patient: "{user_input}"
Assistant:
"""

    try:
        completion = client.chat.completions.create(
            model="gpt-4o",  # You can also use "gpt-3.5-turbo" for cheaper calls
            messages=[
                {"role": "system", "content": "You are a helpful hospital booking assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        reply = completion.choices[0].message.content.strip()
    except Exception as e:
        reply = f"⚠️ Error contacting OpenAI API: {str(e)}"

    # Simulate agent logic
    if "book" in user_input.lower():
        appointments.append({
            "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "status": "Booked"
        })
    elif "cancel" in user_input.lower() and appointments:
        appointments[-1]["status"] = "Cancelled"

    return reply
