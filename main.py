from confiq import client
from React_Agent import Agent,system_prompt
from tools import calculate,get_planet_mass

carl_sagan=Agent(client,system_prompt) 
result=carl_sagan("What is the mass of Jupyter times 5?")
print(result)

carl_sagan.messages