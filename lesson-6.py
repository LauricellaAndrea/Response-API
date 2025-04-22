from openai import OpenAI
from dotenv import load_dotenv     
load_dotenv()

client = OpenAI()

input_messages = [
    {
        "role": "user", 
        "content": "Dove si trova la pizzeria?"
    }
]

tools = [
    {
        "type": "file_search", # questo è lo strumento datoci da OpenAI per fare ricerche su file con response api
        "vector_store_ids": ["vs_6807fa9e266481919a627afc513753fb"], # questo è l'id del nostro vector store, che abbiamo creato su platform.openai.com
        "max_num_results": 2

    }
]

response = client.responses.create(
    model="gpt-4o-mini",
    instructions="You are a helpful assistant.",
    input=input_messages,
    tools=tools
)

print("Agent Response:", response.output_text) # questo è il testo di risposta del modello

print("Annotation:") 
for output_item in response.output:
    if output_item.type == "message":
        for content_item in output_item.content:
            if content_item.type == "output_text":
                for annotation in content_item.annotations:
                    if annotation.type == "file_citation":
                        print(f"- Citation from file: {annotation.filename}")


              
            