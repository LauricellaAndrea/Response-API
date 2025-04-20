from openai import OpenAI
from dotenv import load_dotenv 
load_dotenv()

client = OpenAI()

def chat_loop():
    while True:
        # Get user input
        user_input = input("You: ")

        if user_input.lower() in ["exit", "bye", "quit"]:
            print("goodbye!")
            break
    
        response = client.responses.create(
            model="gpt-4o-mini",
            input=user_input,  
        )

        # Print the response
        print("Bot:", response.output_text)


if __name__ == "__main__":
    chat_loop()       





