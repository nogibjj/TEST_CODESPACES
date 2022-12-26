from pymodm import connect
from pymodm import MongoModel, fields
#from database_definition import Patient

connect("mongodb+srv://echodpp:WiKMRhwb3symh7bL@bme547.kgv09vh.mongodb.net/final_db?retryWrites=true&w=majority")

class Patient(MongoModel):
    rec_no = fields.IntegerField(primary_key=True)
    patient_name = fields.CharField()
    hr = fields.ListField()
    ECG_trace = fields.ListField()
    dt = fields.ListField()
    med_im = fields.ListField()

# this is select all the rec_no from the database
# and return a list of rec_no
def get_rec_no():
    rec_no_list = []
    for i in Patient.objects.all():
        rec_no_list.append(i.rec_no)
    return rec_no_list

def get_patient_hr(rec_no):
    patient_info = Patient.objects.raw({"_id": rec_no}).first()
    return patient_info.hr


if __name__ == "__main__":
    print(get_rec_no())
    print(get_patient_hr(1))
