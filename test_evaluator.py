import knowledge_base
import evaluator
def test_rule_fires():
    kb = knowledge_base.KnowledgeBase()
    condition_our_team={"source": "fact",
    "subject": "our_team",
    "type": "strength",
    "value": "strong_at_maintaining_possession"}
    condition_opp_team={"source": "fact",
    "subject": "opponent",
    "type": "weakness",
    "value": "weak_at_defending_wide_areas"}
    conditions=[condition_our_team,condition_opp_team]
    kb.add_fact(condition_our_team)
    kb.add_fact(condition_opp_team)
    rule_evaluator = evaluator.RuleEvaluator(kb)
    conclusion = "wide_attack_opportunity"
    reason = "our team has an advantage over wide area"
    severity = "medium"
    category="attacking"
    print(kb.add_rule(conditions,conclusion,reason,severity,category))
    rule_evaluator.evaluate_rules()
    assert 1 in kb.results
    print(kb.results)
def test_rule_does_not_fires():
    kb = knowledge_base.KnowledgeBase()
    condition_our_team={"source": "fact",
    "subject": "our_team",
    "type": "strength",
    "value": "strong_at_maintaining_possession"}
    condition_opp_team={"source": "fact",
    "subject": "opponent",
    "type": "weakness",
    "value": "weak_at_defending_wide_areas"}
    conditions=[condition_our_team,condition_opp_team]
    kb.add_fact(condition_our_team)
    rule_evaluator = evaluator.RuleEvaluator(kb)
    conclusion = "wide_attack_opportunity"
    reason = "our team has an advantage over wide area"
    severity = "medium"
    category="attacking"
    print(kb.add_rule(conditions,conclusion,reason,severity,category))
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
    category1="defensive"
    rule_id1=kb.add_rule(conditions,conclusion,reason,severity,category1)
    print(rule_id1)
    condition_our_team1={"source":"conclusion","subject":"our_team","type":"weakness","value":"high_press_vulnerability"}
    conditions=[condition_our_team1]
    rule_evaluator = evaluator.RuleEvaluator(kb)
    conclusion = "press_resistance_needed"
    reason = "Our team has a recorded weakness against high pressing."
    severity = "high"
    category2="defensive"
    rule_id2=kb.add_rule(conditions,conclusion,reason,severity,category2)
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
    category1="defensive"
    condition_our_team={"source":"fact","subject":"our_team","type":"weakness","value":"weak_against_high_press"}
    condition_opp_team={"source":"fact","subject":"opponent","type":"strength","value":"strong_against_high_press"}
    kb.add_fact(condition_our_team)
    kb.add_fact(condition_opp_team)
    conditions2=[condition_our_team,condition_opp_team]
    conclusion2 = "high_press_vulnerability"
    reason2 = "Our team has a recorded weakness against high pressing."
    severity2 = "high"
    category2="defensive"
    condition_our_team2={"source":"conclusion","subject":"our_team","type":"weakness","value":"press_resistance_needed"}
    conditions3=[condition_our_team2]
    rule_evaluator = evaluator.RuleEvaluator(kb)
    conclusion3 = "tactical_adjustment_needed"
    reason3= "Our team has a recorded weakness against high pressing."
    severity3= "high"
    category3="defensive"
    rule_id3=kb.add_rule(conditions3,conclusion3,reason3,severity3,category3)
    rule_id2=kb.add_rule(conditions,conclusion1,reason1,severity1,category1)
    rule_id1=kb.add_rule(conditions2,conclusion2,reason2,severity2,category2)
    print(rule_id1,rule_id2,rule_id3)
    rule_evaluator.evaluate_rules()
    assert rule_id2 in kb.results and rule_id1 in kb.results and rule_id3 in kb.results
    print(kb.results)
def test_rule_circular():
    kb = knowledge_base.KnowledgeBase()
    condition_our_team1={"source":"conclusion","subject":"our_team","type":"weakness","value":"high_press_vulnerability"}
    conditions=[condition_our_team1]
    rule_evaluator = evaluator.RuleEvaluator(kb)
    conclusion1 = "press_resistance_needed"
    reason1 = "Our team has a recorded weakness against high pressing."
    severity1 = "high"
    category1="defensive"
    condition_our_team2={"source":"conclusion","subject":"our_team","type":"weakness","value":"press_resistance_needed"}
    conditions2=[condition_our_team2]
    conclusion2 = "high_press_vulnerability"
    reason2 = "Our team has a recorded weakness against high pressing."
    severity2 = "high"
    category2="defensive"
    rule_id2=kb.add_rule(conditions,conclusion1,reason1,severity1,category1)
    rule_id1=kb.add_rule(conditions2,conclusion2,reason2,severity2,category2)
    rule_evaluator.evaluate_rules()
    assert kb.results=={}
test_rule_fires()
test_rule_does_not_fires()
test_conclusion_fires()
test_rule_order_independence()
test_rule_circular()