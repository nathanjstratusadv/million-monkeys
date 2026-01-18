from dandy import Bot


def million_monkeys_workflow(
        user_request: str
):
    response_intel = Bot().llm.prompt_to_intel(user_request)
    return response_intel.text