
import uuid
from fa_learn_app.models.group import GroupStorage, BaseGroup


def convert_group_dict_to_storage(group_dict: dict) -> GroupStorage:
    """ Производит преобразование dict --> GroupStorage """

    group_storage = GroupStorage(**group_dict)
    return group_storage


def convert_group_in_to_storage(group: BaseGroup) -> GroupStorage:
    """ Производит конвертацию BaseGroup --> GroupStorage """

    tmp_dict: dict = group.dict()
    group_storage = GroupStorage(id=str(uuid.uuid4()),
                                     **tmp_dict)
    return group_storage


def update_group_in_to_storage_to_out(same_id :uuid.UUID, new_group: BaseGroup) -> GroupStorage:
    """ Производит обновление BaseGroup --> GroupStorage """

    tmp_dict: dict = new_group.dict()
    group_storage = GroupStorage(id=str(same_id),
                                     **tmp_dict)
    return group_storage