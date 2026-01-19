from dandy import Bot, Prompt

from monkeys.intelligence.intel.result_intel import ResultIntel, ResultsIntel
from monkeys.intelligence.intel.team_intel import RoleIntel


class MonkeyBot(Bot):
    llm_intel_class = ResultIntel

    def __init__(self, *args, role_intel: RoleIntel, **kwargs):
        super().__init__(*args, **kwargs)

        self.role_intel = role_intel
        self.llm_role = role_intel.role
        self.llm_task = role_intel.task
        self.llm_guidelines = Prompt().list(role_intel.guidelines)

    def process(self, user_request: str, results_intel: ResultsIntel):
        result_intel = self.llm.prompt_to_intel(
            prompt=(
                Prompt()
                .heading('Task:')
                .text(user_request)
                .line_break()
                .heading('Completed Results:')
                .prompt(results_intel.to_prompt())
            ),
            exclude_fields={'role'}
        )

        result_intel.role = self.role_intel

        return result_intel