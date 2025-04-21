from openai import OpenAI
from dotenv import load_dotenv  
load_dotenv()

client = OpenAI()

input_messages = [
 
 {
     "role": "user",
     "content": "Qual è il meteo di oggi a nardò?"
 }
]

tools = [
    {
        "type": "web_search_preview" # questo è lo strumento datoci da OpenAI per fare ricerche sul web con response api
    }
]

response = client.responses.create(
    model="gpt-4o-mini",
    input=input_messages,
    tools= tools,
)

print(response.output_text)