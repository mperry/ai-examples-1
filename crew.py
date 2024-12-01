
from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama
import os
import time

os.environ["OPENAI_API_KEY"] = "NA"

llama3_model = "llama3"
llama2_model = "llama2"
tiny_model = "tinyllama"
current_model = llama2_model
can_delegate = True

# llm = ChatOpenAI(model = current_model, base_url = "http://localhost:11434/v1")
llm = Ollama(model=current_model)


def time_code(func):
    start_time = time.perf_counter()
    result = func()
    end_time = time.perf_counter()
    elapsed_time = round(end_time - start_time, 2)
    print(f"Elapsed time {elapsed_time}s")
    return result

maths = Agent(role = "Math Professor",
                      goal = "Provide the answer to the students who are asking mathematical questions.",
                      backstory = "You are an excellent math professor that likes to solve math questions in a way that everyone can understand your solution",
                      allow_delegation = can_delegate,
                      verbose = True,
                      llm = llm
)
fact_checker = Agent(role = "Fact Checker",
                     goal = "Check the maths to ensure it is correct and has not made any assumptions and answers the original question.",
                    backstory = "You are the world's best fact checker and love fact checking maths equations.",
                    allow_delegation = can_delegate,
                    verbose = True,
                    llm = llm
)

task = Task (description="What is 3 + 5?",
             agent = maths,
             expected_output="A number that solves the description."
)

crew = Crew(
    agents=[maths, fact_checker],
    tasks=[task],
    verbose=True
)



result = time_code(lambda : crew.kickoff())
# result = crew.kickoff()
print(f"result={result}")
