import time
from Ammeters.client import request_current_from_ammeter
from typing import Dict
from ..utils.config import load_config


class AmmeterTestFramework:
    def __init__(self, config_path: str = "config/config.yaml"):
        self.config = load_config(config_path)
        
    def run_test(self, ammeter_type: str) -> Dict:
        cfg = self.config["ammeters"][ammeter_type]
        s = self.config["testing"]["sampling"]
        interval = 1 / s["sampling_frequency_hz"]
        samples = []

        for _ in range(s["measurements_count"]):
            start = time.perf_counter()

            try:
                value = request_current_from_ammeter(cfg["port"], cfg["command"].encode())
                samples.append(value)
            except (OSError, ValueError) as e:
                print(f"Sample failed on {ammeter_type}: {e}")

            time.sleep(max(0, interval - (time.perf_counter() - start)))

        return samples