from .agents import *
import autogen


def flow_run():
    outline_result = planner.initiate_chat(
        human,
        message="I can make a presentation for you, what topic would like to talk about?",
        summary_method="total",
    )
    planner_critic.generate_reply(
        messages="Make some critics on this outline.", sender=planner
    )


def state_transition(last_speaker, groupchat):
    messages = groupchat.messages

    if last_speaker is human:
        return critics


groupchat = autogen.GroupChat(
    agents=[human, planner, planner_critic],
    messages=[],
    max_round=20,
    speaker_selection_method=state_transition,
)

manager = autogen.GroupChatManager(
    groupchat=groupchat,
    llm_config=llm_config,
)
