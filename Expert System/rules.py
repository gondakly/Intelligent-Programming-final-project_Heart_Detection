import collections
import collections.abc
collections.Mapping = collections.abc.Mapping
from experta import KnowledgeEngine, Rule, Fact, P


class HeartDiseaseExpert(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.prediction = 0 

    #10 RULES 
    
    # Rule 1: High Blood Pressure in Males
    @Rule(Fact(trestbps=P(lambda x: x >= 140)), Fact(sex=1))
    def rule_1(self): self.prediction = 1

    # Rule 2: High Cholesterol
    @Rule(Fact(chol=P(lambda x: x >= 240)))
    def rule_2(self): self.prediction = 1

    # Rule 3: Chest Pain (Any symptomatic type)
    @Rule(Fact(cp=P(lambda x: x > 0)))
    def rule_3(self): self.prediction = 1

    # Rule 4: Vessel Blockage (ca >= 1)
    @Rule(Fact(ca=P(lambda x: x >= 1)))
    def rule_4(self): self.prediction = 1

    # Rule 5: Exercise Induced Angina
    @Rule(Fact(exang=1))
    def rule_5(self): self.prediction = 1

    # Rule 6: Significant ST Depression (Oldpeak)
    @Rule(Fact(oldpeak=P(lambda x: x >= 2.0)))
    def rule_6(self): self.prediction = 1

    # Rule 7: Age/Sex Risk (Males over 45)
    @Rule(Fact(age=P(lambda x: x > 45)), Fact(sex=1))
    def rule_7(self): self.prediction = 1

    # Rule 8: High Fasting Blood Sugar
    @Rule(Fact(fbs=1))
    def rule_8(self): self.prediction = 1

    # Rule 9: Abnormal Thalassemia
    @Rule(Fact(thal=P(lambda x: x >= 2)))
    def rule_9(self): self.prediction = 1

    # Rule 10: Combined High Risk (BP + CP + Vessel)
    @Rule(Fact(cp=P(lambda x: x > 0)) & 
          Fact(trestbps=P(lambda x: x >= 140)) & 
          Fact(ca=P(lambda x: x >= 1)))
    def rule_10(self): self.prediction = 1