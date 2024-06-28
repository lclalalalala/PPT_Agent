from autogen import ConversableAgent
from .LLM_config import llm_config

# human
human = ConversableAgent(
    name="user", llm_config=False, human_input_mode="ALWAYS"
)
# outline designer
outline_design = ConversableAgent(
    name="Presentation outline designer",
    system_message="You are a professional presentation maker.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

# critics
outline_design_critic = ConversableAgent(
    name="Presentation outline critic",
    system_message="You are a critic to examine the outline of a presentation. You will examine the oultine by these",
    llm_config=llm_config,
    human_input_mode="NEVER",
)


# planner
pm = ConversableAgent(
    name="Project Manager",
    system_message="""You are a professional project manager,
    you can analysis the presentation outline,
    and split it into small tasks,
    and distribute tasks to our writers.
    Tasks should be seperated by '---'.""",
    llm_config=llm_config,
    human_input_mode="NEVER",
)


# slide story maker

# critics


# summary agent
