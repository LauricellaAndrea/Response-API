from openai import OpenAI
from dotenv import load_dotenv     
load_dotenv()

client = OpenAI()

# JSON Model
input_message = [
    {
        "role": "user",
        "content": """
        Alice e mario stanno andando a lezione di scienze venerdì.
        Rispondi con un oggetto JSON che contiene le seguenti informazioni:
        {
            "subject": "name of subject",
            "day": "date of day",
            "participants": ["Name of participant"]
        }
        
        """
    }
]

response = client.responses.create(
    model= "gpt-4o-mini",
    instructions= "You are a helpful assistant.",
    input= input_message,
    text = {
        "format": {
            "type": "json_object",
        }
    }
)

print(response.output_text)

