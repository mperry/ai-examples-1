
from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
import os

os.environ["OPENAI_API_KEY"] = "NA"

llm = ChatOpenAI(model = "tinyllama", base_url = "http://localhost:11434/v1")

general_agent = Agent(role = "Math Professor",
                      goal = "Provide the answer to the students who are asking mathematical questions.",
                      backstory = "You are an excellent math professor that likes to solve math questions in a way that everyone can understand your solution",
                      allow_delegation = False,
                      verbose = True,
                      llm = llm
)
task = Task (description="What is 3 + 5?",
             agent = general_agent,
             expected_output="A number"
)

crew = Crew(
    agents=[general_agent],
    tasks=[task],
    verbose=2
)

result = crew.kickoff()
print(f"result={result}")
