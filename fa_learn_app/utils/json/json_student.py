import json


with open('students.json') as json_file:
    data: dict = json.load(json_file)

data_students = data.get("students")


def save_dict_to_json():

    with open('students.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)