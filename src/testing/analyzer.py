import statistics


def analyze(samples: list) -> dict:
    if len(samples) < 2:
        return {"error": "not enough samples"}

    return {
        "mean": statistics.mean(samples),
        "median": statistics.median(samples),
        "std": statistics.stdev(samples),
        "min": min(samples),
        "max": max(samples),
    }