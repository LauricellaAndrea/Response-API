from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

from pydantic import BaseModel, ConfigDict 
from typing import List

# Create the Pydantic class
class Event(BaseModel): # Definiamo la classe Event che estende BaseModel di Pydantic
    model_config = ConfigDict(extra="forbid") #Ci consente di definire un oggetto JSON Schema con proprietà aggiuntive

    # Definiamo le proprietà dell'oggetto JSON Schema

    name: str
    date: str
    location: str
    attendees: List[str] #Ciascun elemento della lista è una stringa, quindi non serve definire il tipo di dato

schema = Event.model_json_schema()


# Initial messages
input_messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "input_text",
                "text": "Alice and Bob are going to a science fair in New York on Friday."
            },
        ]
    }
]


client = OpenAI()

response = client.responses.create(
    model="gpt-4o-mini",
    instructions="Extract the event information.",
    input=input_messages,
    text={
        "format": {
            "type": "json_schema",
            "name": "event_info",
            "schema": schema,
            "strict": True
        }
    }
)

print(response.output_text)