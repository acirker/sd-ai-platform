from engine import evaluate, weighted_consensus

def run_batch(inputs, FI_RULES):
    results = []

    for item in inputs:
        fi_results = {}

        for fi, config in FI_RULES.items():
            fi_results[fi] = evaluate(item, config["rules"])

        results.append({
            "input": item,
            "fi_results": fi_results,
            "resolution": weighted_consensus(fi_results, FI_RULES)
        })

    return results
