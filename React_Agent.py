
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
            

