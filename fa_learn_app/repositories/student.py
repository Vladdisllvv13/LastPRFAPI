from typing import List, Dict, Optional
import uuid
from fa_learn_app.utils.json.json_student import data_students, save_dict_to_json
from fa_learn_app.models.student import StudentIn, StudentOut, StudentStorage
from fa_learn_app.utils.student_repository_utils import convert_student_in_to_storage, update_student_in_to_storage_to_out, convert_student_dict_to_storage, convert_student_storage_to_out

class BaseProductRepository:
    """ Базовый класс для реализации функционала работы с продуктами """

    def get_by_id(self, id :uuid.UUID | int) -> StudentOut:
        raise NotImplementedError

    def get_all(self, group :str, limit :int, skip :int) -> List[StudentOut]:
        raise NotImplementedError

    def create(self, student :StudentIn) -> StudentOut:
        raise NotImplementedError

    def update_student(self, id : uuid.UUID, student :StudentIn) -> StudentStorage:
        raise NotImplementedError

    def delete(self, id :uuid.UUID) -> StudentOut:
        raise NotImplementedError

class StudentTmpRepository(BaseProductRepository):
    """ Реализация продукта с временным хранилищем в json """

    def get_by_id(self, id :uuid.UUID) -> Optional[StudentOut]:
        """ Получение продукта по id """

        student :StudentStorage = data_students.get(str(id), None)
        if student is None:
            return None
        student = convert_student_dict_to_storage(student)
        student_out: StudentOut = convert_student_storage_to_out(student)
        return student_out

    def get_all(self, group :str, limit :int, skip :int) -> List[StudentOut]:
        """ Получение всех продуктов """

        student_out_list :List[StudentOut] = []
        for _, student in data_students.items():
            if group == "":
                student = convert_student_dict_to_storage(student)
                student_out_list.append(convert_student_storage_to_out(student))
            elif student.get("group") == group:
                student = convert_student_dict_to_storage(student)
                student_out_list.append(convert_student_storage_to_out(student))
        return student_out_list[skip:skip + limit]

    def create(self, student: StudentIn) -> StudentOut:
        """ Создание продукта """

        student_storage: StudentStorage = convert_student_in_to_storage(student)
        data_students.update({str(student_storage.id): student_storage.dict()})
        save_dict_to_json()
        student_out: StudentOut = convert_student_storage_to_out(student_storage)
        return student_out

    def update_student(self, id: uuid.UUID, new_student: StudentIn) -> Optional[StudentOut]:
        """ Изменение продукта """

        student: StudentStorage = data_students.get(str(id))
        if student is None:
            return None
        student_update: StudentStorage = update_student_in_to_storage_to_out(id, new_student)
        data_students.update({str(student_update.id): student_update.dict()})
        save_dict_to_json()
        student_out: StudentOut = convert_student_storage_to_out(student_update)
        return student_out

    def delete(self, id: uuid.UUID) -> str:
        """ Удаление продукта """

        student: StudentStorage = data_students.get(id)
        if student is None:
            return None
        data_students.pop(str(id), None)
        save_dict_to_json()
        return "Группа удалена"