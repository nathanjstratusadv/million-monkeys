from __future__ import annotations

from peewee import *

from monkeys.consts import VERSION
from monkeys.enums import UserRequestStatus, TaskStatus
from monkeys.fields import EnumField

DATABASE_PATH = f'million_monkeys_v{VERSION}.db'
database = SqliteDatabase(DATABASE_PATH)


class BaseModel(Model):
    class Meta:
        database = database


class Monkey(BaseModel):
    name = CharField()
    description = TextField()
    system_prompt = TextField()


class UserRequest(BaseModel):
    text = TextField()
    status = EnumField(UserRequestStatus, default=UserRequestStatus.NOT_STARTED)

    def append_task(self, description: str) -> Task:
        with database.atomic():
            last_task = self.get_last_task()
            return self.tasks.create(
                user_request=self,
                order=last_task.order + 1 if last_task else 0,
                description=description
            )

    def insert_task(self, description: str, order: int) -> Task:
        with database.atomic():
            for task in self.tasks.order_by(Task.order):
                if task.order >= order:
                    task.order += 1
                    task.save()

            return self.tasks.create(
                user_request=self,
                order=order,
                description=description
            )

    def get_last_task(self) -> Task:
        with database.atomic():
            return self.tasks.select().where(
                Task.user_request == self
            ).order_by(
                Task.order.desc()
            ).first()


class Task(BaseModel):
    user_request = ForeignKeyField(UserRequest, backref='tasks', on_delete='CASCADE')
    status = EnumField(TaskStatus, default=TaskStatus.PENDING)
    order = IntegerField()
    description = TextField()
    good_outcome = TextField(null=True)
    result = TextField(null=True)

    class Meta:
        order_by = ('order',)
