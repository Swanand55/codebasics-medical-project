import re

from backend.src.parser_generic import MedicalDocParser


class PatientDetailParser(MedicalDocParser):
    def __init__(self,text):
        MedicalDocParser.__init__(self,text)

    def parse(self):
        return{
            'patient_name':self.get_field('patient_name'),
            'contact_number':self.get_field('contact_number'),
            'vaccination_status':self.get_field('vaccination_status'),
            'medical_problem':self.get_field('medical_problem')
        }


    def get_field(self,field_name):
        pattern_dict_one = {
            'patient_name': {'pattern': 'Birth Date\s*([a-zA-Z]*\s*[a-zA-Z]*)', 'flags': re.DOTALL},
            'contact_number': {'pattern': 'Birth Date\s*[a-zA-Z]*\s*[a-zA-Z]*\s*\S*\s*\d*\s*\d*\s*(\(\d{3}\)\s*\d{3}-*\s*\d{4})','flags': re.DOTALL},
        }
        pattern_dict_two = {
            'vaccination_status': {'pattern': 'vaccination\?\s*:\s*([a-zA-Z]*)|vaccination\?\s*([a-zA-Z]*)', 'flags': re.DOTALL},
            'medical_problem': {'pattern': 'headaches\S*\s*([a-zA-Z]*\/[a-zA-Z]*)|headaches\S*\s*([a-zA-Z]*)','flags': re.DOTALL}
        }

        pattern_obj_one=pattern_dict_one.get(field_name)
        pattern_obj_two=pattern_dict_two.get(field_name)
        if pattern_obj_one:
            matches=re.findall(pattern_obj_one['pattern'],self.text,pattern_obj_one['flags'])
            if len(matches)>0:
                return matches[0]
        elif pattern_obj_two:
            matches=re.search(pattern_obj_two['pattern'],self.text,pattern_obj_two['flags'])
            matches=matches.groups()
            res = []
            for val in matches:
                if val != None:
                    res.append(val)
            return res[0]