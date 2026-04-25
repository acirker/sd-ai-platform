def evaluate(input_text, rules):
    text = input_text.lower()
    for rule in rules:
        if rule["keyword"] in text:
            return {
                "decision": rule["decision"],
                "reason": rule["reason"],
                "policy": rule.get("policy", "No policy cited"),
                "matched_rule": rule["keyword"]
            }
    return {
        "decision": "REVIEW",
        "reason": "No rule matched",
        "policy": "No applicable policy found",
        "matched_rule": None
    }

def weighted_consensus(fi_results, fi_config):
    scores = {}
    explanation = []

    for fi, result in fi_results.items():
        decision = result["decision"]
        weight = fi_config[fi]["weight"]

        scores[decision] = scores.get(decision, 0) + weight

        explanation.append({
            "fi": fi,
            "decision": decision,
            "weight": weight,
            "policy": result["policy"]
        })

    final = max(scores, key=scores.get)

    return {
        "decision": final,
        "confidence": round(scores[final], 2),
        "scores": scores,
        "explanation": explanation
    }
