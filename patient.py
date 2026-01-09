class Patient:
    def __init__(self, patient_id, name, age, disease):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease

    def patient_type(self):
        return "Adult" if self.age >= 18 else "Minor"


if __name__ == "__main__":
    p = Patient(101, "Anusha", 20, "Fever")
    print("Patient ID :", p.patient_id)
    print("Name       :", p.name)
    print("Age        :", p.age)
    print("Disease    :", p.disease)
    print("Type       :", p.patient_type())