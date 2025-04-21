from openai import OpenAI
from dotenv import load_dotenv     
import base64
load_dotenv()

client = OpenAI()

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

base64_image = encode_image("./menu.png")

# Structured Output Models
input_message = [
    {
        "role": "user",
         "content": [
            {
                "type": "input_text",
                "text": "Please extract all menu items from the image."
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
    instructions="Extract the event information.",
    input=input_message,
    text = {
        "format": { # Importante utilizzare il campo format per definire il formato di output, altrimenti non funziona
            "type": "json_schema",
            "name": "menu_items",
            "schema": {
                "type": "object",
                "properties": {
                    "menu_items": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "item_name": {
                                    "type": "string"
                                },
                                "item_price": {
                                    "type": "number"
                                }
                            },
                            "required": ["item_name", "item_price"], #definiamo le proprietà richieste, a noi ci interessa estrarre il nome e il prezzo del piatto
                            "additionalProperties": False,
                        },
                    },
                },
                "required": ["menu_items"], # Anche qui definiamo le proprietà richieste perchè abbiamo definito un oggetto, questa è il root object
                "additionalProperties": False,
            },
            "strict": True,
        }
    }
    
)

print(response.output_text)

