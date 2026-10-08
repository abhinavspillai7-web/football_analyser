class KnowledgeBase:
    def __init__(self):
        self.facts={}
        self.rules=[]
        self.conclusions={}
        self.reasons={}
    def add_fact(self,fact):
        fact_id=len(self.facts)+1
        self.facts[fact_id]=fact
        return fact_id
kb=KnowledgeBase()
fact=kb.add_fact({"subject": "opponent", "type": "strength", "value": "quick_counter_attack"})
fact2=kb.add_fact({"subject": "opponent", "type": "strength", "value": "slow_counter_attack"})
print(kb.facts)