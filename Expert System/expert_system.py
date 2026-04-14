from rules import HeartDiseaseExpert
import collections
import collections.abc
collections.Mapping = collections.abc.Mapping
from experta import KnowledgeEngine, Rule, Fact, P

# THE METRIC METHOD
def calculate_knowledge_accuracy(engine, session_data):
    if not session_data:
        return 0.0
    
    correct_count = 0
    for record in session_data:
        engine.reset()
        engine.prediction = 0
        # Send everything except the 'label' to the engine
        features = {k: v for k, v in record.items() if k != 'label'}
        engine.declare(Fact(**features))
        engine.run()
        
        if engine.prediction == record['label']:
            correct_count += 1
            
    return (correct_count / len(session_data)) * 100

# MAIN EXECUTION LOOP
def run_expert_system():
    engine = HeartDiseaseExpert()
    session_records = []  # Stores user inputs to calculate accuracy over time

    print("=== HEART DISEASE EXPERT SYSTEM (CONSOLE MODE) ===")
    
    while True:
        try:
            print("\n--- ENTER PATIENT DATA ---")
            data = {
                "age": float(input("Age: ")),
                "sex": int(input("Sex (1=M, 0=F): ")),
                "trestbps": float(input("Blood Pressure: ")),
                "chol": float(input("Cholesterol: ")),
                "cp": int(input("Chest Pain (0-3): ")),
                "ca": int(input("Vessels (0-3): ")),
                "exang": int(input("Angina (1=Y, 0=N): ")),
                "oldpeak": float(input("Oldpeak: ")),
                "fbs": int(input("FBS > 120 (1=Y, 0=N): ")),
                "thal": int(input("Thal (1, 2, 3): "))
            }
            
            # Since the user is entering data for "testing," we need the ground truth
            actual_label = int(input("Actual Health Status (1=Heart Disease, 0=Healthy): "))
            data['label'] = actual_label
            
            # 1. Store in session for accuracy calculation
            session_records.append(data)

            # 2. Run Single Prediction for current input
            engine.reset()
            engine.prediction = 0
            features_only = {k: v for k, v in data.items() if k != 'label'}
            engine.declare(Fact(**features_only))
            engine.run()
            
            diagnosis = "HIGH RISK" if engine.prediction == 1 else "LOW RISK"
            print(f"\n[ENGINE RESULT]: {diagnosis}")

            # 3. Calculate and Display Knowledge Accuracy for all entered data
            accuracy = calculate_knowledge_accuracy(engine, session_records)
            
            print(f"KNOWLEDGE ACCURACY (Session): {accuracy:.2f}%")
            print(f"Total Patients Evaluated: {len(session_records)}")

            cont = input("\nEvaluate another patient? (y/n): ").lower()
            if cont != 'y':
                break

        except ValueError:
            print("\nERROR: Invalid numeric input. Try again.")

if __name__ == "__main__":
    run_expert_system()