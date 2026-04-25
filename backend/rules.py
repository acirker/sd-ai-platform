FI_RULES = {
    "FI_A": {
        "weight": 0.7,
        "rules": [
            {"keyword": "gym", "decision": "APPROVE", "reason": "Wellness benefit allowed"},
            {"keyword": "wheelchair", "decision": "APPROVE", "reason": "Medical equipment covered"},
            {"keyword": "vacation", "decision": "DENY", "reason": "Not an eligible expense"}
        ]
    },
    "FI_B": {
        "weight": 0.3,
        "rules": [
            {"keyword": "gym", "decision": "REVIEW", "reason": "May be considered recreational"},
            {"keyword": "wheelchair", "decision": "APPROVE", "reason": "Medical necessity"},
            {"keyword": "vacation", "decision": "DENY", "reason": "Personal expense not allowed"}
        ]
    }
}
