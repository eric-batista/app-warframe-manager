from devtools.database import DatabaseAdapter

from warframe_manager.zaws.domain.entities import zaws as models
from warframe_manager.zaws.infra.database.repositories import \
    zaw as zaw_repository


class RegisterZaw:
    def __init__(self, zaw: models.Zaw, database_adapter: DatabaseAdapter):
        self._zaw = zaw
        self._database_adapter = database_adapter
        self._repository = zaw_repository.ZawRepositoryDB(self._database_adapter)

    def _persists_zaw_info(self):
        return self._repository.create_zaw(self._zaw)

    def _execute(self):
        return self._persists_zaw_info()

    def execute(self):
        try:
            return self._execute()
        except Exception as e:
            raise e


class RegisterZawStrike:
    def __init__(self, zaw: models.ZawStrike, database_adapter: DatabaseAdapter):
        self._zaw = zaw
        self._database_adapter = database_adapter
        self._repository = zaw_repository.ZawRepositoryDB(self._database_adapter)

    def _persists_zaw_info(self):
        return self._repository.create_strike(self._zaw)

    def _execute(self):
        return self._persists_zaw_info()

    def execute(self):
        try:
            return self._execute()
        except Exception as e:
            raise e


class RegisterZawLink:
    def __init__(self, zaw: models.ZawLink, database_adapter: DatabaseAdapter):
        self._zaw = zaw
        self._database_adapter = database_adapter
        self._repository = zaw_repository.ZawRepositoryDB(self._database_adapter)

    def _persists_zaw_info(self):
        return self._repository.create_link(self._zaw)

    def _execute(self):
        return self._persists_zaw_info()

    def execute(self):
        try:
            return self._execute()
        except Exception as e:
            raise e


class RegisterZawGrip:
    def __init__(self, zaw: models.ZawGrip, database_adapter: DatabaseAdapter):
        self._zaw = zaw
        self._database_adapter = database_adapter
        self._repository = zaw_repository.ZawRepositoryDB(self._database_adapter)

    def _persists_zaw_info(self):
        return self._repository.create_grip(self._zaw)

    def _execute(self):
        return self._persists_zaw_info()

    def execute(self):
        try:
            return self._execute()
        except Exception as e:
            raise e
