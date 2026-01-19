from dandy import Bot, Prompt

from monkeys.intelligence.bots.judge_bot import JudgeBot
from monkeys.intelligence.bots.monkey_bot import MonkeyBot
from monkeys.intelligence.bots.teacher_bot import TeacherBot
from monkeys.intelligence.bots.team_bot import TeamBot
from monkeys.intelligence.intel.judgement_intel import JudgementType
from monkeys.intelligence.intel.result_intel import ResultsIntel

ATTEMPT_LIMIT = 10


def million_monkeys_workflow(
        user_request: str
):
    for _ in range(ATTEMPT_LIMIT):

        print(f'{user_request=}')

        team_intel = TeamBot().process(
            user_request=user_request
        )

        for index, role_intel in enumerate(team_intel):
            taught_role_intel = TeacherBot().process(
                user_request=user_request,
                role_intel=role_intel
            )

            print(taught_role_intel)
            print('\n')

            team_intel[index] = taught_role_intel

        results_intel = ResultsIntel(
            results=[]
        )

        for role_intel in team_intel:
            result_intel = MonkeyBot(
                role_intel=role_intel
            ).process(
                user_request=user_request,
                results_intel=results_intel
            )

            results_intel.append(result_intel)

            print(f"{role_intel.role} Monkey:")
            print(result_intel.content)
            print('\n')

        judgement_intel = None

        if results_intel:
            judgement_intel = JudgeBot().process(
                user_request=user_request,
                results_intel=results_intel
            )

            print('Final Judgement:')
            print(judgement_intel)
            print('\n')

            if judgement_intel.type == JudgementType.FAIL:
                continue

        if results_intel[-1]:
            print(f'{results_intel[-1].content=}')
            return results_intel[-1].content


    return None