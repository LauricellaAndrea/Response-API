from openai import OpenAI
from dotenv import load_dotenv # In questo modo carichiamo le variabili d'ambiente dal file .env per maggiore sicurezza
load_dotenv()

client = OpenAI()

input_messages = [
    {
        "role": "assistant",
        "content": "Perchè il cielo è blu?"
    }
]

response = client.responses.create(
    model="o3-mini",
    input=input_messages,
    reasoning={
        "effort" : "medium"   
    }
)

print(response.output_text)

# With Stream 

#full_response = ""

#for event in response:
#    if event.type == "response.output_text.delta":
#       print(event.delta, end="", flush=True) # end="" serve per non andare a capo e flush=True serve per forzare l'output
#       full_response += event.delta

#print("\n\n\nFull reponse:", full_response) # aggiungiamo nnnn per andare a capo e stampiamo la risposta completa

#In questo modo possiamo vedere il risultato in tempo reale, mentre il modello sta generando la risposta, come accade con ChatGPT