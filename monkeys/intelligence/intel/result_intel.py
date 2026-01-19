from dandy import BaseIntel, BaseListIntel, Prompt

from monkeys.intelligence.intel.team_intel import RoleIntel


class ResultIntel(BaseIntel):
    content: str
    role: RoleIntel | None = None

    def to_prompt(self) -> Prompt:
        return (
            Prompt()
            .sub_heading(f'{self.role.role} Output:')
            .text(self.content)
        )

class ResultsIntel(BaseListIntel):
    results: list[ResultIntel]

    def to_prompt(self) -> Prompt:
        prompt = Prompt()

        for result_intel in self.results:
            prompt.prompt(result_intel.to_prompt())
            prompt.line_break()

        return prompt

