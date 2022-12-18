from fa_learn_app.repositories.group import GroupTmpRepository

TMP_GROUP_REPOSITORY = GroupTmpRepository()

def get_group_repo() -> GroupTmpRepository:
    """ Получение group репозитория """

    return TMP_GROUP_REPOSITORY
