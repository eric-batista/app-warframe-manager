from devtools.database import DatabaseAdapter

_adapter = DatabaseAdapter()


def get_database_adapter():
    return _adapter
