from dandy import Bot, Prompt

from monkeys.intelligence.intel.team_intel import RoleIntel


class TeacherBot(Bot):
    llm_role = 'Teacher'
    llm_task = 'Read through the role provided and create a suitable task and guidelines for the role to help with the user request.'
    llm_guidelines = None
    llm_intel_class = RoleIntel

    def process(self, user_request: str, role_intel: RoleIntel) -> RoleIntel:
        return self.llm.prompt_to_intel(
            prompt=(
                Prompt()
                .heading('Role:')
                .text(role_intel.role)
                .line_break()
                .heading('User Request:')
                .text(user_request)
            ),
            intel_object=role_intel,
            exclude_fields={'role'},
        )
