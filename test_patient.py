from patient import Patient

def test_adult_patient():
    p = Patient(102, "Ravi", 25, "Cold")
    assert p.patient_type() == "Adult"

def test_minor_patient():
    p = Patient(103, "Kiran", 12, "Flu")
    assert p.patient_type() == "Minor"