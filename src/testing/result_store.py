import json
import os
import uuid
from datetime import datetime


def save_result(results_dir: str, ammeter_type: str, samples: list, stats: dict) -> str:
    os.makedirs(results_dir, exist_ok=True)
    run_id = uuid.uuid4().hex[:8]
    data = {
        "run_id": run_id,
        "ammeter": ammeter_type,
        "timestamp": datetime.now().isoformat(),
        "samples": samples,
        "statistics": stats,
    }
    with open(os.path.join(results_dir, f"{run_id}.json"), "w") as f:
        json.dump(data, f, indent=2)
    return run_id

def load_results(results_dir: str, ammeter_type: str = None) -> list:
    runs = []
    for name in sorted(os.listdir(results_dir)):
        if name.endswith(".json"):
            with open(os.path.join(results_dir, name)) as f:
                data = json.load(f)
            if ammeter_type is None or data["ammeter"] == ammeter_type:
                runs.append(data)
    return runs
