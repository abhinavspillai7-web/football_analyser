class KnowledgeBase:
    def __init__(self):
        self.facts={}
        self.rules=[]
        self.results={}
    def add_fact(self,fact):
        fact_id=len(self.facts)+1
        self.facts[fact_id]=fact
        return fact_id
    def add_rule(self,conditions,conclusion,reason,severity):
        if not conditions:
            return None
        rule_id=len(self.rules)+1
        rule={"id":rule_id,"conditions":conditions,"conclusion":conclusion,"reason":reason,"severity":severity}
        self.rules.append(rule)
        return rule_id