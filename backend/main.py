from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json, datetime
from engine import evaluate, weighted_consensus
from simulation import run_batch

app = FastAPI()
POLICY_FILE = "policies.json"
AUDIT_FILE = "audit_log.json"

class SimulationInput(BaseModel):
    inputs: list[str]

def load_policies():
    with open(POLICY_FILE) as f:
        return json.load(f)

def save_policies(data):
    with open(POLICY_FILE, "w") as f:
        json.dump(data, f, indent=2)

def log_change(old, new):
    with open(AUDIT_FILE) as f:
        history = json.load(f)

    history.append({
        "timestamp": str(datetime.datetime.utcnow()),
        "old": old,
        "new": new
    })

    with open(AUDIT_FILE, "w") as f:
        json.dump(history, f, indent=2)

@app.get("/")
def root():
    return {"status": "live"}

@app.get("/evaluate")
def run(input: str):
    FI_RULES = load_policies()
    results = {}

    for fi, config in FI_RULES.items():
        results[fi] = evaluate(input, config["rules"])

    return {
        "input": input,
        "fi_results": results,
        "resolution": weighted_consensus(results, FI_RULES)
    }

@app.post("/simulate")
def simulate(data: SimulationInput):
    FI_RULES = load_policies()
    return run_batch(data.inputs, FI_RULES)

from fastapi.responses import HTMLResponse

@app.get("/ui", response_class=HTMLResponse)
def ui():
    with open("ui.html") as f:
        return f.read()
