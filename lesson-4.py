from openai import OpenAI
from dotenv import load_dotenv     
load_dotenv()

client = OpenAI()

# Structured Output Models
input_message = [
    {
        "role": "user",
        "content": " Alice e mario stanno andando a lezione di scienze venerdì"
    }
]

response = client.responses.create(
    model="gpt-4o-mini",
    instructions="Extract the event information.",
    input=input_message,
    text = {
        "format": { # Importante utilizzare il campo format per definire il formato di output, altrimenti non funziona
            "type": "json_schema",
            "name": "calendar_event",
            "schema": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                    },
                    "date": {
                        "type": "string",
                    },
                    "location": {
                        "type": "string",
                    },
                    "attendees": {
                        "type": "array",
                        "items": {
                            "type": "string",
                        },
                    },
                },
                "required": ["name", "date", "location", "attendees"],
                "additionalProperties": False,
            },
            "strict": True,
        }
    }
    
)

print(response.output_text)

