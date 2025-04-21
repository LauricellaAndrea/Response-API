from openai import OpenAI
from dotenv import load_dotenv  
load_dotenv()

client = OpenAI()

input_messages = [
 
 {
     "role": "user",
     "content": "Qual è il meteo di oggi da me?"
 }
]

tools = [
    {
        "type": "web_search_preview", # questo è lo strumento datoci da OpenAI per fare ricerche sul web con response api
        "user_location" : { # questo è il campo che ci permette di definire la posizione dell'utente
            "type": "approximate",
            "country": "IT",
            "city": "Nardò",
            "region": "Puglia"
        }
    }
]

response = client.responses.create(
    model="gpt-4o-mini",
    instructions="Please provide a weather forecast for the user's location.", # tramite un system prompt possiamo definire il comportamento del modello
    input=input_messages,
    tools= tools,
)

print(response.output_text)