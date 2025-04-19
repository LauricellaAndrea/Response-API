from openai import OpenAI
from dotenv import load_dotenv # In questo modo carichiamo le variabili d'ambiente dal file .env per maggiore sicurezza
load_dotenv()

client = OpenAI()

input_messages = [
    {
        "role": "user", # cambiato da "assistant" a "user" perchè assistant non accetta input 
        "content": [
            {
                "type": "input_text",
                "text": "Per favore, descrivi questa immagine:",
            },
            {
                "type": "input_image",
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Ginger_european_cat.jpg/250px-Ginger_european_cat.jpg"
            } # URL di un'immagine di un gatto, in output ci aspettiamo una descrizione dell'immagine
        ]
    }
]

response = client.responses.create(
    model="gpt-4o-mini",
    input=input_messages,
)

print(response.output_text)