# Design

## Decisions
- Config-driven: ports, commands, sample count, duration and frequency live in config/config.yaml, nothing is hardcoded.
- Separation: sampling (test_framework), analysis (analyzer) and storage (result_store) are separate modules. examples/run_tests.py is only a thin runner.
- Error handling: a failed sample (OSError, ValueError) is logged and skipped, the run continues. The analyzer returns an error result when fewer than 2 samples exist.
- Storage: each run is a JSON file with a unique ID (uuid), easy to inspect and reload.
- Dependencies: only pyyaml. The original requirements.txt listed numpy, scipy, matplotlib, seaborn and pandas, but the spec asks to minimize libraries and they are not used.

## Bugs found and fixed
1. Ports: main.py starts the emulators on 5001-5003, the README said 5000-5002. Config now uses 5001-5003.
2. Commands: the README omitted the "-current" suffix for CIRCUTOR. Fixed in config.
3. Client: it returned None when no data arrived, which broke later steps. It now raises ConnectionError.
4. run_tests.py: it called run_test() without the required argument. Fixed.