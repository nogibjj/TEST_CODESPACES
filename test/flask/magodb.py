def find_patient(patient_id):
    from pymodm import errors as pymodm_errors
    try:
        found_patient = Patient.objects.raw({'_id': id_no }).first()
    except pymodm_errors.DoesNotExist:
        return False
    return found_patient

def add_test_worker(in_data)