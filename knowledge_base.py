class KnowledgeBase:
    def __init__(self):
        self.facts={}
        self.rules=[]
        self.results={}
    def add_fact(self,fact):
        fact_id=len(self.facts)+1
        self.facts[fact_id]=fact
        return fact_id
    def add_rule(self,conditions,conclusion,reason,severity,category):
        if not conditions:
            return None
        rule_id=len(self.rules)+1
        rule={"id":rule_id,"conditions":conditions,"conclusion":conclusion,"reason":reason,"severity":severity,"category":category}
        self.rules.append(rule)
        return rule_id
    def get_conclusion_support(self):
        grp_conclusions={}
        for i in self.results:
            conclusion=self.results[i]["conclusion"]
            grp_conclusions.setdefault(conclusion,[])
            grp_conclusions[conclusion].append(i)
        return grp_conclusions

