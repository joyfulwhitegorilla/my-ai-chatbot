# 1. Import the groq library
import groq
import os
from dotenv import load_dotenv

# 2. Paste your API key (between the quotes)
client = groq.Groq(api_key="your-ap-key")

# Or use environment variables
# load_dotenv()
# client = groq.Groq(api_key=os.getenv("GROQ_API_KEY"))

# 3. Welcome message
print("👋 Welcome to your AI Chatbot! Type 'exit' to stop.")

# 4. Add sample questions and answers
sample_questions = [
    "What is your favourite Netflix series?"
    "Who is your favourite character in the series?"
]

# 5. Start chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    # 6. Send input to groq
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are a very discerning individual who aims to look at things from different perspectives rather than just the way they are presented."},
            {"role": "user", "content": user_input}
        ]
    )

    # 7. Get the chatbot's reply
    reply = response.choices[0].message.content
    print("AI:", reply)
