from enum import Enum


class UserRequestStatus(Enum):
    NOT_STARTED = 'not_started'
    IN_PROGRESS = 'in_progress'
    ERRORED = 'errored'
    COMPLETED = 'completed'


class TaskStatus(Enum):
    PENDING = 'pending'
    PLANNING = 'planning'
    READY = 'ready'
    EXECUTING = 'executing'
    DONE = 'done'