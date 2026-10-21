import knowledge_base
class RuleEvaluator:
    def __init__(self,kb):
        self.kb=kb
    def evaluate_rules(self):
        self.kb.results.clear()
        new_results_added = True
        while new_results_added:
            new_results_added=False
            for i in self.kb.rules:
                rule_counter=0
                for j in i["conditions"]:
                    if j["source"]=="fact":
                        for k in self.kb.facts.values():
                            if j["subject"] == k["subject"] and j["type"] == k["type"] and j["value"] == k["value"]:
                                rule_counter+=1
                                break
                    elif j["source"]=="conclusion":
                        if j["value"] in self.kb.get_conclusion_support():
                            rule_counter+=1

                if len(i["conditions"])== rule_counter and len(i["conditions"])!=0 and  i["id"] not in self.kb.results:
                    self.kb.results[i["id"]]={"conclusion":i["conclusion"],"reason":i["reason"],"severity":i["severity"]}
                    new_results_added=True
