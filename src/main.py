import os
from agents import Agent, Runner, set_tracing_disabled, set_default_openai_client
from openai import AsyncClient

from config import BASE_URL, logger, MAX_ITERATIONS
from agent_definition import reviewer_agent, critic_agent

ollama_client = AsyncClient(
    base_url=BASE_URL,
    api_key="ollama"
)

set_tracing_disabled(True)

set_default_openai_client(ollama_client)

def validate_env_variables():
    if os.getenv("REVIEWER_MODEL") is None: raise Exception("REVIEWER_MODEL is missing.")
    if os.getenv("CRITIC_MODEL") is None: raise Exception("CRITIC_MODEL is missing.")
    if os.getenv("BASE_URL") is None: raise Exception("BASE_URL is missing.")

validate_env_variables()

while True:
    user_input = input(">> ")
    if user_input in ['exit']:
        break

    iteration = 1
    while iteration < MAX_ITERATIONS:
        # format input
        input_items = [
            {"role": "user", "content": f"fetch and review pull request at {user_input}"}
        ]

        # call the reviewer to generate the review 
        review_result = Runner.run_sync(
            starting_agent=reviewer_agent,
            input=input_items
        )
        print(review_result.final_output)


    

    # call the critic and pass the review