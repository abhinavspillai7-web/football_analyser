import knowledge_base
class RuleEvaluator:
    def __init__(self,kb):
        self.kb=kb
    def evaluate_rules(self):
        for i in self.kb.rules:
            rule_counter=0
            for j in i["conditions"]:
                for k in self.kb.facts.values():
                    if j["subject"] == k["subject"] and j["type"] == k["type"] and j["value"] == k["value"]:
                        rule_counter+=1
                        break
            if len(i["conditions"])== rule_counter and len(i["conditions"])!=0:
                self.kb.results[i["id"]]={"conclusion":i["conclusion"],"reason":i["reason"],"severity":i["severity"]}






