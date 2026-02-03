import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("API Key not valid")

# Create Gemini client
client = genai.Client(api_key=API_KEY)

print("Our Healthcare Assistant bot is ready to use....")

SYSTEM_PROMPT = """
You are a healthcare assistant.
Answer ONLY health, medical, fitness, yoga, nutrition related questions.
If user asks anything outside healthcare, reply strictly:
"Sorry, I can answer only healthcare-related questions."
"""

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Bot: Take care! 👋")
        break

    response = client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=f"{SYSTEM_PROMPT}\nUser: {user_input}"
    )

    print("Bot:", response.text)
