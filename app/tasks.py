from app.celery import app
from monkeys.intelligence.workflow import million_monkeys_workflow


@app.task
def solve_user_request(user_request: str):
    return million_monkeys_workflow(
        user_request=user_request
    )
