from openai import OpenAI
from dotenv import load_dotenv  
load_dotenv()

client = OpenAI()

input_messages = [
 
 {
     "role": "user",
     "content": "Quali sono le ultime notizie di openai?",
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

#print(response.model_dump_son(indent=4)) # in questo modo vediamo le citazioni della nostra ricerca web ma in formato json

print("AI Response:", response.output_text)
print("\nCitazioni:")

for block in response.output:
    if not hasattr(block, "content"): # Se non ha l'attributo content, non ci interessa
        continue\

    for content_item in block.content:
        if not hasattr(content_item, "citazioni"): # Se non ha l'attributo citationi, non ci interessa
            continue

        for citazioni in content_item.citationi:
            if citazioni.type == "url_citazioni": 
                print(f"URL: {citazioni.title} :{citazioni.url}")
