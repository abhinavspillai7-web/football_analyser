import knowledge_base
import evaluator
def rule_fires():
    kb = knowledge_base.KnowledgeBase()
    condition_our_team={"subject":"our_team","type":"weakness","value":"weak_against_high_press"}
    condition_opp_team={"subject":"opponent","type":"strength","value":"strong_against_high_press"}
    conditions=[condition_our_team,condition_opp_team]
    our_teamid=kb.add_fact(condition_our_team)
    opp_teamid=kb.add_fact(condition_opp_team)
    rule_evaluator = evaluator.RuleEvaluator(kb)
    conclusion = "high_press_vulnerability"
    reason = "Our team has a recorded weakness against high pressing."
    severity = "high"
    print(kb.add_rule(conditions,conclusion,reason,severity))
    rule_evaluator.evaluate_rules()
    assert 1 in kb.results
    print(kb.results)
def rule_not_fires():
    kb = knowledge_base.KnowledgeBase()
    condition_our_team={"subject":"our_team","type":"weakness","value":"weak_against_high_press"}
    condition_opp_team={"subject":"opponent","type":"strength","value":"strong_against_high_press"}
    conditions=[condition_our_team,condition_opp_team]
    our_teamid=kb.add_fact(condition_our_team)
    rule_evaluator = evaluator.RuleEvaluator(kb)
    conclusion = "high_press_vulnerability"
    reason = "Our team has a recorded weakness against high pressing."
    severity = "high"
    print(kb.add_rule(conditions,conclusion,reason,severity))
    rule_evaluator.evaluate_rules()
    assert 1 not in kb.results
    print(kb.results)
rule_fires()
rule_not_fires()