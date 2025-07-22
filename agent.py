from database import appointments
from datetime import datetime
import openai
import os

client = openai.OpenAI(api_key="OPENAI_API_KEY")  # Or set via environment variable


def process_message(user_input: str) -> str:
    prompt = f"""
You are a hospital assistant helping users book, reschedule, or cancel appointments.
Current Appointments: {appointments}

User: "{user_input}"
Assistant:
"""

    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": prompt}
    ]
    )

    reply = completion.choices[0].message.content

    # Basic logic for booking/cancellation
    if "book" in user_input.lower():
        appointments.append({
            "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "status": "Booked"
        })
    elif "cancel" in user_input.lower() and appointments:
        appointments[-1]["status"] = "Cancelled"

    return reply
