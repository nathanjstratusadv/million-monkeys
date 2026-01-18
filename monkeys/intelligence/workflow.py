from dandy import Bot, Prompt


def million_monkeys_workflow(
        user_request: str
):
    response_intel = Bot().llm.prompt_to_intel(
        prompt=(
            Prompt()
            .text('Can you please use the user request below to describe a task that would be related to the user request?')
            .line_break()
            .sub_heading('User request')
            .text(user_request)
        )
    )

    return response_intel.text