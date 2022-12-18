from typing import List, Dict, Optional
import uuid
from fa_learn_app.utils.json.json_group import data_groups, save_dict_to_json
from fa_learn_app.models.group import GroupStorage, BaseGroup
from fa_learn_app.utils.group_repository_utils import convert_group_in_to_storage, update_group_in_to_storage_to_out, convert_group_dict_to_storage

class BaseProductRepository:
    """ Базовый класс для реализации функционала работы с продуктами """

    def get_by_id(self, id :uuid.UUID | int) -> GroupStorage:
        raise NotImplementedError

    def get_all(self, limit :int, skip :int) -> List[GroupStorage]:
        raise NotImplementedError

    def create(self, group :BaseGroup) -> GroupStorage:
        raise NotImplementedError

    def update_group(self, id : uuid.UUID, group :BaseGroup) -> GroupStorage:
        raise NotImplementedError

    def delete(self, id :uuid.UUID) -> GroupStorage:
        raise NotImplementedError

class GroupTmpRepository(BaseProductRepository):
    """ Реализация продукта с временным хранилищем в json """

    def get_by_id(self, id :uuid.UUID) -> Optional[GroupStorage]:
        """ Получение продукта по id """

        group :GroupStorage = data_groups.get(str(id), None)
        if group is None:
            return None
        group_out = convert_group_dict_to_storage(group)
        return group_out

    def get_all(self, limit :int, skip :int) -> List[GroupStorage]:
        """ Получение всех продуктов """

        group_out_list :List[GroupStorage] = []
        for _, group in data_groups.items():
            if group == "":
                group_out_list.append(convert_group_dict_to_storage(group))
            elif group.get("groups") == group:
                group_out_list.append(convert_group_dict_to_storage(group))
        return  group_out_list[skip:skip+limit]

    def create(self, group: BaseGroup) -> GroupStorage:
        """ Создание продукта """

        group_storage: GroupStorage = convert_group_in_to_storage(group)
        data_groups.update({str(group_storage.id): group_storage.dict()})
        save_dict_to_json()
        return group_storage

    def update_group(self, id: uuid.UUID, new_group: BaseGroup) -> Optional[GroupStorage]:
        """ Изменение продукта """

        group: GroupStorage = data_groups.get(str(id))
        if group is None:
            return None
        group_update: GroupStorage = update_group_in_to_storage_to_out(id, new_group)
        data_groups.update({str(group_update.id): group_update.dict()})
        save_dict_to_json()
        return group_update

    def delete(self, id: uuid.UUID) -> str:
        """ Удаление продукта """

        group: GroupStorage = data_groups.get(str(id))
        if group is None:
            return None
        data_groups.pop(str(id), None)
        save_dict_to_json()
        return "Группа удалена"