import datetime
import uuid
from fa_learn_app.models.student import StudentIn, StudentOut, StudentStorage

def convert_student_dict_to_storage(student_dict: dict) -> StudentStorage:
    """ Производит преобразование dict --> StudentStorage """

    student_storage = StudentStorage(**student_dict)
    return student_storage


def convert_student_storage_to_out(student: StudentStorage) -> StudentOut:
    """ Производит конвертацию ProductSrorage --> ProductOut """

    tmp_dict: dict = student.dict()
    tmp_dict.pop("password", None)
    return StudentOut(**tmp_dict)


def convert_student_in_to_storage(student: StudentIn) -> StudentStorage:
    """ Производит конвертацию ProductIn --> PrductStorage """

    tmp_dict: dict = student.dict()
    birth_date = str(tmp_dict.get('birth_date'))
    tmp_dict.update({'birth_date': birth_date})
    student_storage = StudentStorage(id=str(uuid.uuid4()),
                                     **tmp_dict)
    return student_storage


def update_student_in_to_storage_to_out(same_id :uuid.UUID, new_student: StudentIn) -> StudentStorage:
    """ Производит обновление ProductIn --> PrductStorage """

    tmp_dict: dict = new_student.dict()
    product_storage = StudentStorage(id=str(same_id),
                                     **tmp_dict)

    return product_storage