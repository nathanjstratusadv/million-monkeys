from dandy import Bot, Prompt

from monkeys.intelligence.intel.judgement_intel import JudgementIntel
from monkeys.intelligence.intel.result_intel import ResultsIntel


class JudgeBot(Bot):
    llm_role = 'Judge'
    llm_task = 'Evaluate the results of the workflow and provide feedback on the quality of the results.'
    llm_guidelines = Prompt().list([
        'Evaluate the results of the workflow and provide feedback on the quality of the results.',
        'Determine if the last result is a pass or fail to be sent back to the user.'
    ])
    llm_intel_class = JudgementIntel

    def process(self, user_request: str, results_intel: ResultsIntel) -> JudgementIntel:
        return self.llm.prompt_to_intel(
            prompt=(
                Prompt()
                .heading('User Request:')
                .text(user_request)
                .line_break()
                .heading('Completed Results:')
                .prompt(results_intel.to_prompt())
            )
        )
