import knowledge_base
import evaluator
def test_rule_fires():
    kb = knowledge_base.KnowledgeBase()
    condition_our_team={"source":"fact","subject":"our_team","type":"weakness","value":"weak_against_high_press"}
    condition_opp_team={"source":"fact","subject":"opponent","type":"strength","value":"strong_against_high_press"}
    conditions=[condition_our_team,condition_opp_team]
    kb.add_fact(condition_our_team)
    kb.add_fact(condition_opp_team)
    rule_evaluator = evaluator.RuleEvaluator(kb)
    conclusion = "high_press_vulnerability"
    reason = "Our team has a recorded weakness against high pressing."
    severity = "high"
    print(kb.add_rule(conditions,conclusion,reason,severity))
    rule_evaluator.evaluate_rules()
    assert 1 in kb.results
    print(kb.results)
def test_rule_does_not_fires():
    kb = knowledge_base.KnowledgeBase()
    condition_our_team={"source":"fact","subject":"our_team","type":"weakness","value":"weak_against_high_press"}
    condition_opp_team={"source":"fact","subject":"opponent","type":"strength","value":"strong_against_high_press"}
    conditions=[condition_our_team,condition_opp_team]
    kb.add_fact(condition_our_team)
    rule_evaluator = evaluator.RuleEvaluator(kb)
    conclusion = "high_press_vulnerability"
    reason = "Our team has a recorded weakness against high pressing."
    severity = "high"
    print(kb.add_rule(conditions,conclusion,reason,severity))
    rule_evaluator.evaluate_rules()
    assert 1 not in kb.results
    print(kb.results)
def test_conclusion_fires():
    kb = knowledge_base.KnowledgeBase()
    condition_our_team={"source":"fact","subject":"our_team","type":"weakness","value":"weak_against_high_press"}
    condition_opp_team={"source":"fact","subject":"opponent","type":"strength","value":"strong_against_high_press"}
    kb.add_fact(condition_our_team)
    kb.add_fact(condition_opp_team)
    conditions=[condition_our_team,condition_opp_team]
    rule_evaluator = evaluator.RuleEvaluator(kb)
    conclusion = "high_press_vulnerability"
    reason = "Our team has a recorded weakness against high pressing."
    severity = "high"
    rule_id1=kb.add_rule(conditions,conclusion,reason,severity)
    print(rule_id1)
    condition_our_team1={"source":"conclusion","subject":"our_team","type":"weakness","value":"high_press_vulnerability"}
    conditions=[condition_our_team1]
    rule_evaluator = evaluator.RuleEvaluator(kb)
    conclusion = "press_resistance_needed"
    reason = "Our team has a recorded weakness against high pressing."
    severity = "high"
    rule_id2=kb.add_rule(conditions,conclusion,reason,severity)
    print(rule_id2)
    rule_evaluator.evaluate_rules()
    assert rule_id1 in kb.results and rule_id2 in kb.results
    print(kb.results)
def test_rule_order_independence():
    kb = knowledge_base.KnowledgeBase()
    condition_our_team1={"source":"conclusion","subject":"our_team","type":"weakness","value":"high_press_vulnerability"}
    conditions=[condition_our_team1]
    rule_evaluator = evaluator.RuleEvaluator(kb)
    conclusion1 = "press_resistance_needed"
    reason1 = "Our team has a recorded weakness against high pressing."
    severity1 = "high"
    condition_our_team={"source":"fact","subject":"our_team","type":"weakness","value":"weak_against_high_press"}
    condition_opp_team={"source":"fact","subject":"opponent","type":"strength","value":"strong_against_high_press"}
    kb.add_fact(condition_our_team)
    kb.add_fact(condition_opp_team)
    conditions2=[condition_our_team,condition_opp_team]
    conclusion2 = "high_press_vulnerability"
    reason2 = "Our team has a recorded weakness against high pressing."
    severity2 = "high"
    condition_our_team2={"source":"conclusion","subject":"our_team","type":"weakness","value":"press_resistance_needed"}
    conditions3=[condition_our_team2]
    rule_evaluator = evaluator.RuleEvaluator(kb)
    conclusion3 = "tactical_adjustment_needed"
    reason3= "Our team has a recorded weakness against high pressing."
    severity3= "high"
    rule_id3=kb.add_rule(conditions3,conclusion3,reason3,severity3)
    rule_id2=kb.add_rule(conditions,conclusion1,reason1,severity1)
    rule_id1=kb.add_rule(conditions2,conclusion2,reason2,severity2)
    print(rule_id1,rule_id2,rule_id3)
    rule_evaluator.evaluate_rules()
    assert rule_id2 in kb.results and rule_id1 in kb.results and rule_id3 in kb.results
    print(kb.results)
#test_conclusion_fires()
test_rule_order_independence()