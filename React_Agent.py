from confiq import client 

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
            

system_prompt = """
You run in a loop of Thought, Action, PAUSE, Observation.
At the end of the loop you output an Answer
Use Thought to describe your thoughts about the question you have been asked.
Use Action to run one of the actions available to you - then return PAUSE.
Observation will be the result of running those actions.

Your available actions are:

calculate:
e.g. calculate: 4 * 7 / 3
Runs a calculation and returns the number - uses Python so be sure to use floating point syntax if necessary

get_planet_mass:
e.g. get_planet_mass: Earth
returns weight of the planet in kg

Example session:

Question: What is the mass of Earth times 2?
Thought: I need to find the mass of Earth
Action: get_planet_mass: Earth
PAUSE 

You will be called again with this:

Observation: 5.972e24

Thought: I need to multiply this by 2
Action: calculate: 5.972e24 * 2
PAUSE

You will be called again with this: 

Observation: 1,1944×10e25

If you have the answer, output it as the Answer.

Answer: The mass of Earth times 2 is 1,1944×10e25.

Now it's your turn:
""".strip()
