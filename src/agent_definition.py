from agents import Agent
from prompts import REVIEWER_SYSTEM_PROMPT, CRITIC_SYSTEM_PROMPT
from config import REVIEWER_MODEL, CRITIC_MODEL

reviewer_agent = Agent(
    name="review_agent",
    instructions=REVIEWER_SYSTEM_PROMPT,
    tools=[],
    model=REVIEWER_MODEL
)

critic_agent = Agent(
    name="critic_agent",
    instructions=CRITIC_SYSTEM_PROMPT,
    model=CRITIC_MODEL
)