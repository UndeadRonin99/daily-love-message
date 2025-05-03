import os
import random
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_TOKEN")
twilio_number = os.getenv("TWILIO_FROM")
recipient_number = os.getenv("TWILIO_TO")

# List of love messages
love_messages = [
    "I love you more than words can ever say. 💖",
    "Good morning, my perfect person. Hope your day is as beautiful as you. ☀️",
    "You're my favorite everything. 💕",
    "I hope your day is filled with sunshine and happiness — just like you bring to my life. 🌼",
    "You’re smart, kind, gorgeous, and mine. What a combo. 🥰",
    "Every moment with you is a blessing. ❤️",
    "Have the most amazing day, my angel! 😘",
    "You make my heart smile. I love you!",
    "Just a reminder that you're the best thing that's ever happened to me. 💌",
    "You're loved more than you know — always. 💫"
    # Add up to 200 messages here...
]

# Load messages from file
with open("love_messages.txt", "r", encoding="utf-8") as f:
    love_messages = f.readlines()

# Pick a random message and strip newline
selected_message = random.choice(love_messages).strip()

# Send the SMS
client = Client(account_sid, auth_token)

message = client.messages.create(
    body=selected_message,
    from_=twilio_number,
    to=recipient_number
)

print(f"Message sent! SID: {message.sid}")
