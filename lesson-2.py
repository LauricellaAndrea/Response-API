from openai import OpenAI
import base64

from dotenv import load_dotenv # In questo modo carichiamo le variabili d'ambiente dal file .env per maggiore sicurezza
load_dotenv()

# Funzione per convertire un'immagine in una stringa base64
# Questo è necessario per poter inviare l'immagine tramite API come testo codificato
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
    
# Codifica l'immagine specificata e la salva nella variabile base64_image    
base64_image = encode_image("./image.jpg")


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
                "image_url": f"data:image/jpeg;base64,{base64_image}"
            } 
        ]
    }
]

response = client.responses.create( 
    model="gpt-4o-mini",
    input=input_messages,
)

print(response.output_text)