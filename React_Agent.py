import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env
load_dotenv()

# Get the API key from the environment
api_key = os.environ.get("GROQ_API_KEY")

print("Current API Key:", os.environ.get("GROQ_API_KEY"))


# Check if the API key is loaded properly
if not api_key:
    raise ValueError("API key not found. Make sure GROQ_API_KEY is set in the .env file.")

print(api_key)
# Initialize Groq client
client = Groq(api_key=api_key)

# Make a chat completion request
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama3-70b-8192",
    stream=False,
)

# Print the response
print(chat_completion.choices[0].message.content)


class Agent:
    def __init__(self,client,system):
        self.client=client
        self.system=system
        self.messages=[]
        if self.system is not None:
            self.messages.append({'role':'system','content':self.system})
        
    def __call__(self,message):
        if message:
            self.messages.append({'role':'system','content':message})
        result=self.execute()
        self.messages.append({'role':'assistant','content':result})
        return result
    
    def execute(self):
        completion=client.chat.completions.create(
        messages=self.messages,
        model="llama3-70b-8192",
        stream=False,
        )
        return completion.choices[0].message.content
            