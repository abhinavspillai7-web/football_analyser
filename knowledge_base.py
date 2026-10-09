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
    def add_rule(self,conditions,conclusion,reason,severity):
        rule_id=len(self.rules)+1
        rule={"id":rule_id,"conditions":conditions,"conclusion":conclusion,"reason":reason,"severity":severity}
        self.rules.append(rule)
        return rule_id
kb=KnowledgeBase()
conditions=["our_team_vulnerable_to_counter_attacks", "opponent_strong_at_counter_attacks"]
conclusion="counter_attacking_threat"
reason="opponent_strength_targets_our_weakness"
severity="high"
conditions1=["our_left_back_weak_at_defending", "opponent_right_winger_strong_at_dribbling"]
conclusion1="left_flank_defensive_threat"
reason1="opponent_winger_can_exploit_left_back_weakness"
severity1="medium"
kb.add_rule(conditions,conclusion,reason,severity)
kb.add_rule(conditions1,conclusion1,reason1,severity1)
print(kb.rules)