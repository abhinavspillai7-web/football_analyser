def register_tactical_rules(kb):
    condition1={"source": "fact",
    "subject": "our_team",
    "type": "strength",
    "value": "strong_passing"}
    condition2={"source": "fact",
    "subject": "our_team",
    "type": "strength",
    "value": "strong_ball_retention"}
    conditions=[condition1,condition2]
    conclusion = "possible_possession_oriented_tendency"
    reason = "Strong passing and ball retention support maintaining possession and building attacks through passing."
    severity = "low"
    category="tactical_tendency"
    kb.add_rule(conditions,conclusion,reason,severity,category)
