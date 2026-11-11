# Ammeter Testing Framework

Tests three ammeter emulators (Greenlee, ENTES, CIRCUTOR): samples measurements, analyzes them, and archives each run.

## Setup
pip install pyyaml

## Run
Terminal 1 (emulators): python main.py
Terminal 2 (tests):     python -m examples.run_tests

## Configuration
All settings are in config/config.yaml: sampling (count, duration, frequency), ammeter ports and commands, statistics, results directory.

## Structure
- Ammeters/client.py: sends a command to an emulator, returns the current as float
- src/testing/test_framework.py: sampling per ammeter, with error handling
- src/testing/analyzer.py: mean, median, std, min, max
- src/testing/result_store.py: saves each run as JSON with a unique ID, and loads past runs
- examples/run_tests.py: runs all three ammeters, analyzes, saves

## Results
Every run is saved in results/<run_id>.json (ID, time, samples, statistics).