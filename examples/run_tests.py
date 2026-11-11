from src.testing.test_framework import AmmeterTestFramework
from src.testing.analyzer import analyze
from src.testing.result_store import save_result

def main():
    # יצירת מסגרת הבדיקות
    framework = AmmeterTestFramework()
    
    # הרצת בדיקות לכל סוגי האמפרמטרים
    ammeter_types = ["greenlee", "entes", "circutor"]
    results = {}
    
    for ammeter_type in ammeter_types:
        print(f"Testing {ammeter_type} ammeter...")
        results[ammeter_type] = framework.run_test(ammeter_type)
        
    # השוואת תוצאות
    for ammeter_type, result in results.items():
        stats = analyze(result)
        run_id = save_result("results", ammeter_type, result, stats)
        print(f"\nResults for {ammeter_type} (run {run_id}): {stats}")

if __name__ == "__main__":
    main() 