from typing import Any

from dandy import Bot, Prompt

from monkeys.intelligence.intel.team_intel import TeamIntel


class TeamBot(Bot):
    llm_role = 'Team Planner'
    llm_task =  'Read through a user request and create a team of roles to achieve the goal.'
    llm_guidelines = (
        Prompt()
        .heading('Team Guidelines')
        .list([
            'Read through the user request and create roles that would assist in accomplishing the purpose of the request.',
            'Make sure these roles work together in an order that would create a highly refined final result.',
            'These roles should be unique and reflect the part of the user request they will be responsible for.',
            'The roles should also be able to work independently of each other and benefit from the previous roles work.',
            'Make sure there is roles at the beginning to ensure the that instructions for the user request are detailed.',
        ])
    )
    llm_intel_class = TeamIntel

    def process(self, user_request: str) -> TeamIntel:
        return self.llm.prompt_to_intel(
            prompt=user_request,
            exclude_fields={'roles': {'task': True, 'guidelines': True}},
        )
