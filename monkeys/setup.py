from monkeys.models import database, Monkey, UserRequest, Task

DATABASE_MODELS = [
    Monkey,
    UserRequest,
    Task
]

def setup():
    database.connect()

    database.create_tables(
        DATABASE_MODELS,
        safe=True
    )

    for model in DATABASE_MODELS:
        if not model.table_exists():
            message = f'Failed to validate {model.__name__.lower()} table'
            raise Exception(message)

    if not database.is_closed():
        database.close()
