from enum import Enum

from dandy import BaseIntel


class JudgementType(Enum):
    FAIL = 0
    PASS = 1


class JudgementIntel(BaseIntel):
    type: JudgementType
    reason: str
