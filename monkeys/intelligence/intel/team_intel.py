from dandy import BaseIntel, BaseListIntel


class RoleIntel(BaseIntel):
    role: str
    task: str | None = None
    guidelines: list[str] | None = None


class TeamIntel(BaseListIntel):
    roles: list[RoleIntel]
