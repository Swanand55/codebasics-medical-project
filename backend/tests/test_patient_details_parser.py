from backend.src.parser_patient_details import PatientDetailParser
import pytest

@pytest.fixture()
def kathy_details():
    document_test='97/12{2020  Patient Medical Record  Patient Information Birth Date  Kathy Crawford May 6 1972  (737) 988-0851 Weight’  9264 Ash Dr 95  New York City, 10005 :  United States Height: 190  In Case of Emergency , ee —EE— Simeone Crawford 9266 Ash Dr New York City, New York, 10005 Home phone United States (990) 375-4621 Work phone Genera! Medical History I ee IMMUNE  IMMUNE Have you had the Hepatitis B vaccination?  No  List any Medical Problems (asthma, seizures, headaches}:  Migraine '

    return PatientDetailParser(document_test)

@pytest.fixture()
def jerry_details():
    document_test='17/12/2020  Patient Medical Record  Patient Information Birth Date  Jerry Lucas May 2 1998  (279) 920-8204 Weight:  4218 Wheeler Ridge Dr 57  Buffalo, New York, 14201 sa,  United States Height: 170  In Case of Emergency eee  Joe Lucas 4218 Wheeler Ridge Dr Buffalo, New York, 14201 Home phone . United States Work phone  General Medical History  Chicken Pox (Varicella): Measles:  IMMUNE NOT IMMUNE  Have you had the Hepatitis B vaccination?  : Yes  List any Medical Problems (asthma, seizures, headaches): N/A '

    return PatientDetailParser(document_test)

def test_get_pname(kathy_details,jerry_details):
    assert kathy_details.get_field('patient_name')=='Kathy Crawford'
    assert jerry_details.get_field('patient_name')=='Jerry Lucas'

def test_get_pnumber(kathy_details,jerry_details):
    assert kathy_details.get_field('contact_number')=='(737) 988-0851'
    assert jerry_details.get_field('contact_number')=='(279) 920-8204'

def test_get_vaccination_status(kathy_details,jerry_details):
    assert kathy_details.get_field('vaccination_status')=='No'
    assert jerry_details.get_field('vaccination_status')=='Yes'

def test_get_medical_problem(kathy_details,jerry_details):
    assert kathy_details.get_field('medical_problem')=='Migraine'
    assert jerry_details.get_field('medical_problem')=='N/A'

def test_parse(kathy_details,jerry_details):
    record_kathy=kathy_details.parse()
    assert record_kathy=={
        'patient_name':'Kathy Crawford',
        'contact_number':'(737) 988-0851',
        'vaccination_status':'No',
        'medical_problem':'Migraine'
    }

    record_jerry=jerry_details.parse()
    assert record_jerry == {
        'patient_name': 'Jerry Lucas',
        'contact_number': '(279) 920-8204',
        'vaccination_status': 'Yes',
        'medical_problem': 'N/A'
    }